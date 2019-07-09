from django.urls import path, re_path

from . import views

urlpatterns = [
	path('', views.home, name='home'),
	re_path('apply/.*', views.parser, name='apply')
]