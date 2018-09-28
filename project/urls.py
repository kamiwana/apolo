from django.conf.urls import url
from .views import *

urlpatterns = [
 url(r'^$', ProjectView.as_view()),
 url(r'^(?P<project_key>.+)/$', ProjectView.as_view()),
]