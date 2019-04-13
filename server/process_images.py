# Function to be imported for preprocessing / live-streaming

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

import numpy as np

import requests
import base64

class ImageProcessor:
	# shelf objects will be hardcoded
	def __init__ (self, store_objects):
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
		self.attributes="gender,age,ethnicity"

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
		import pdb;pdb.set_trace()

	def query_facepp(self, image_file):
		img64 = base64.b64encode(image_file.read())
		json_resp = requests.post(self.http_url,
		      data = { 
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
		pass

	def count_item_frames(self, customer_objects):
		""" Update the number of frames where a customer is near a store item """
		for store_object in self.store_objects:
			for customer in customer_objects:
				# TODO: rewrite to take in key and x, y
				#if self.distance(customer, store_object) < self.closeness_threshold:
				#	customer.item_frames[store_object[0]] += 1
		return customer_objects

	def distance(self, obj1_coord, obj2_coord):
		"""Return distance of two given objects in the [item, x, y] format."""
		return np.sqrt((obj1_coord[0] - obj2_coord[0])**2 + (obj1_coord[1] - obj2_coord[1])**2)


