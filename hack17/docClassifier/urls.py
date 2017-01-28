from django.conf.urls import url, include
import django.contrib.auth.views
from . import views

urlpatterns = [
	url(r'^upload', views.upload_file, name='upload'),
]