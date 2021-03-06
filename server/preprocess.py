from process_images import ImageProcessor
import os

# hardcoded local variable
YH_VIDEO_PATH = "/home/seahyh/repo/hackathon/yc/video"
YH_OUTPUT_PATH = "/home/seahyh/repo/hackathon/yc/output"

def main():
	store_objects = {"shampoo":(100,150), "soap":(100,200)}
	p = ImageProcessor(store_objects)

	for v_path in next(os.walk(YH_VIDEO_PATH))[1]:
		full_video_path = os.path.join(YH_VIDEO_PATH, v_path)
		full_output_path = os.path.join(YH_OUTPUT_PATH, v_path)

		#os.mkdir(full_output_path)

		frames = os.listdir(full_video_path)
		frames.sort()

		for frame in frames:
			full_frame_path = os.path.join(full_video_path, frame)
			full_output_frame_path = os.path.join(full_output_path, frame)

			with open(full_frame_path, 'rb') as image_file:
				p.process(image_file)
				# save image and json output

	# with open('test.jpg', 'rb') as image_file:
	# 	p.process(image_file)

if __name__ == '__main__':
	main()