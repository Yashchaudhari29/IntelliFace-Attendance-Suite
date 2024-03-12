
from django.urls import path
from User.views import *
urlpatterns = [
    path('',U_home,name='U_home'),
    path('empty_database/', empty_db, name='empty_db'),
    path('video_feed/', video, name='video_feed'),
    # path('capture/', capture, name='capture'),
    # path('Capture_image/', Capture_image, name='Capture_image'),
]