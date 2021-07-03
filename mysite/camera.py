import cv2
from script.hand_video_detector import hand_video
import time

# basically take camera input and convert it into a cv object
# later to be processed by gen()
class VideoCamera(object):
	def __init__(self):
		self.video = cv2.VideoCapture(0)
		
	def __del__(self):
		self.video.release()

	def get_frame(self):
		success, image = self.video.read()
		if success:
			# call the detection here
			image = hand_video(success, image)

		return image


# generator that saves the video captured if flag is set
def gen(camera, flag):
	if flag == True:
		# time information
		time_now = time.localtime()
		current_time = time.strftime("%H:%M:%S", time_now)
		# default format
		fourcc = cv2.VideoWriter_fourcc(*'XVID')
		# output which is a cv writer, given the name and format, and resolution
		out = cv2.VideoWriter('output_' + str(current_time) + '.avi',fourcc, 20.0, (640,480))

		while True:
			# cv object to jpg
			ret, jpeg = cv2.imencode('.jpg', camera.get_frame())
			# jpg to bytes
			frame =  jpeg.tobytes()
			# generator yielding the bytes
			yield (b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

			cv_frame = camera.get_frame()
			out.write(cv_frame)
	
	else:
		while True:
			ret, jpeg = cv2.imencode('.jpg', camera.get_frame())
			frame =  jpeg.tobytes()
			yield (b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
