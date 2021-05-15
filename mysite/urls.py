from os import name
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from mysite.core import views


urlpatterns = [
    path('', views.Home.as_view(), name='home'),

    path('image_upload/', views.image_upload_view, name='image_upload'),
    path('video_input/', views.video_input, name='video_input'),
    path('video_input/video_stream', views.video_stream, name='video_input/video_stream'),
    path('video_input/video_save', views.video_save, name='video_input/video_save'),

    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
