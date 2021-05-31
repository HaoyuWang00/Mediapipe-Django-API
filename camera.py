import cv2
from script.hand_video_detector import hand_video
import time

# basically take camera input and convert it into a cv object
# in this version it returns bytes
# later to be processed by gen()
class VideoCamera(object):
	def __init__(self):
		self.video = cv2.VideoCapture(0)
		
	def __del__(self):
		self.video.release()

	def get_frame(self):
		success, image = self.video.read()
		if success:
			image = hand_video(success, image)
		image_bytes = cv2.imencode('.jpg', image)[1].tobytes()
		return image_bytes
