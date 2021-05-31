from django.http.response import HttpResponse, HttpResponseServerError
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy

from .forms import  ImageForm

import urllib
import numpy as np
from script.hand_image_detector import hand_detection
import cv2

from mysite.camera import VideoCamera #, gen
from django.http import StreamingHttpResponse
import time


class Home(TemplateView):
    template_name = 'home.html'


def image_upload_view(request):
    """Process images uploaded by users"""
    data = {"success": False}
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if request.FILES.get("image", None) is not None:
            image = _grab_image(stream=request.FILES["image"])
            annotated_image = hand_detection(image)
            cv2.imshow("output", annotated_image)
            cv2.waitKey(0)

            form.save()
            img_obj = form.instance
            return render(request, 'image_upload.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'image_upload.html', {'form': form})


# a helper function to convert img.url into a cv.img object
# for image upload and detection only
def _grab_image(path=None, stream=None, url=None):
	if path is not None:
		image = cv2.imread(path)
	else:	
		if url is not None:
			resp = urllib.urlopen(url)
			data = resp.read()
		elif stream is not None:
			data = stream.read()
		# convert the image to a NumPy array and then read it into
		# OpenCV format
		image = np.asarray(bytearray(data), dtype="uint8")
		image = cv2.imdecode(image, cv2.IMREAD_COLOR)
 
	# return the image
	return image

# for video input and detection
def video_stream(request):
    try:
        vid = StreamingHttpResponse(gen(VideoCamera(), False), 
        content_type='multipart/x-mixed-replace; boundary=frame')
        return vid
    except Exception as e:
        # pass
        return 'error in views.video_stream'

def video_save(request):
    try:
        vid = StreamingHttpResponse(gen(VideoCamera(), True), 
        content_type='multipart/x-mixed-replace; boundary=frame')
        return vid
    except HttpResponseServerError.streaming as e:
        pass
        # return HttpResponseServerError(e.message)

def video_input(request):
    return render(request, 'video_input.html')

# generator that saves the video captured if flag is set
def gen(camera, flag):
	if flag == True:
		time_now = time.localtime()
		current_time = time.strftime("%H:%M:%S", time_now)
		fourcc = cv2.VideoWriter_fourcc(*'XVID')
		out = cv2.VideoWriter('output_' + str(current_time) + '.avi',fourcc, 20.0, (640,480))

		while True:
                    frame = camera.get_frame()
                    nparr = np.fromstring(frame, np.uint8)
                    cv_frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
                    yield (b'--frame\r\n'
                        b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
                    out.write(cv_frame)
			
	else:
		while True:
                    frame = camera.get_frame()
                    yield (b'--frame\r\n'
                        b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')