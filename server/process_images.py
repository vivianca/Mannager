# Function to be imported for preprocessing / live-streaming

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

import numpy as np

import requests
import base64
import io
import os
from google.cloud import vision
from google.cloud.vision import types
import random


iou_threshold = 0.8
total_count = 0


class Person():
    def __init__(pose, box, alive=True):
        """pose = (x,y)
           box = (x1,y1,x2,y2)
        """
        self.uid = None
        self.alive = alive
        self.pose.x = pose[0]
        self.pose.y = pose[1]
        self.box = box


class ImageProcessor:
	# shelf objects will be hardcoded
	def __init__(self, store_objects):
		self.client = vision.ImageAnnotatorClient()
		self.config = {}
		self.prev_objects = None

		# for detecting how long someone is at a place
		self.store_objects = store_objects
		self.closeness_threshold = 10

		# BAD PRACTICE - ONLY USED FOR DEMO for FACE++ API
		self.http_url = 'https://api-us.faceplusplus.com/facepp/v3/detect'
		self.key = "P8KFCk6ySapKMQRqpEV1bFrJxXxJ8isc"
		self.secret = "MtufTWUadCOQ2bfWOwOL8hwGnA-BNQu2"
		self.attributes = "gender,age,ethnicity"

	"""
	Takes an image file, sends it to the server, get it back, run bezzie code,
	and then return an image + overall data
	"""

	def process(self, image_file):
		content = image_file.read()
		g_image = types.Image(content=content)
		# Query VISION API
		response = self.client.object_localization(image=g_image)
		objects = response.localized_object_annotations
		# Analyze image
		frame_data = self.analyze(self.prev_objects, objects)
		self.prev_objects = objects

		# if there is a new person, run query
		image_file.seek(0)
		facepp_data = self.query_facepp(image_file)

		print(objects, facepp_data)
		import pdb; pdb.set_trace()

	def query_facepp(self, image_file):
		img64 = base64.b64encode(image_file.read())
		json_resp = requests.post(self.http_url,
		      data={
		          'api_key': self.key,
		          'api_secret': self.secret,
		          'image_base64': img64,
		          'return_attributes': self.attributes
		      }
		)
		return json_resp

	# TODO
	def process_batch(self, image_file_list):
		pass

	def analyze(self, prev_objects, new_objects):
		pass

	def draw(self, image_file, objects):
		"""Note: Image should be PIL image"""
	    plt.imshow(image_file)
	    for obj in objects:
	        if obj.name == "Person":
	            box_left, box_right, box_top, box_bottom, box_width, box_height = get_box(obj, image_file)
	            plt.gca().add_patch(Rectangle((box_left, box_top), box_width,
	                                          box_height, linewidth=2, edgecolor='white', facecolor='none'))
	            person_x = (box_right + box_left)/2.0
	            person_y = (box_top + box_bottom)/2.0
	            plt.gca().add_patch(Rectangle((person_x - 10, person_y - 10), 20,
	                                          20, linewidth=1, edgecolor='orange', facecolor='orange'))
	    plt.show()

	def count_item_frames(self, customer_objects):
		""" Update the number of frames where a customer is near a store item """
		for store_object in self.store_objects:
			for customer in customer_objects:
				# TODO: rewrite to take in key and x, y
				# if self.distance(customer, store_object) < self.closeness_threshold:
				#	customer.item_frames[store_object[0]] += 1
		return customer_objects


	def iou(self, box1, box2):
	    """Implement the intersection over union (IoU) between box1 and box2

	    Arguments:
	    box1 -- first box, list object with coordinates (x1, y1, x2, y2)
	    box2 -- second box, list object with coordinates (x1, y1, x2, y2)
	    """

	    # Calculate the (y1, x1, y2, x2) coordinates of the intersection of box1 and box2. Calculate its Area.
	    xi1 = max(box1[0], box2[0])
	    yi1 = max(box1[1], box2[1])
	    xi2 = min(box1[2], box2[2])
	    yi2 = min(box1[3], box2[3])
	    inter_area = (xi2 - xi1) * (yi2 - yi1)

	    # Calculate the Union area by using Formula: Union(A,B) = A + B - Inter(A,B)
	    box1_area = (box1[2] - box1[0]) * (box1[3] - box1[1])
	    box2_area = (box2[2] - box2[0]) * (box2[3] - box2[1])
	    union_area = box1_area + box2_area - inter_area

	    # compute the IoU
	    iou = inter_area / union_area

	    return iou


	def get_box(self, obj, image):
	    # Normalized Coordinates
	    image_width, image_height = image.size
	    box_norm_left = obj.bounding_poly.normalized_vertices[0].x
	    box_norm_right = obj.bounding_poly.normalized_vertices[2].x
	    box_norm_top = obj.bounding_poly.normalized_vertices[0].y
	    box_norm_bottom = obj.bounding_poly.normalized_vertices[2].y
	    # Convert to real coordinates
	    box_left = image_width * box_norm_left
	    box_right = image_width * box_norm_right
	    box_top = image_height * box_norm_top
	    box_bottom = image_height * box_norm_bottom
	    box_width = box_right - box_left
	    box_height = box_bottom - box_top
	    return box_left, box_right, box_top, box_bottom, box_width, box_height



	def distance(self, obj1_coord, obj2_coord):
		"""Return distance of two given objects in the [item, x, y] format."""
		return np.sqrt((obj1_coord[0] - obj2_coord[0])**2 + (obj1_coord[1] - obj2_coord[1])**2)
