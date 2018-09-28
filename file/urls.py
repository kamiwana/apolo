from django.conf.urls import url
from .views import *

urlpatterns = [
 url(r'^delete/', delete),
 url(r'^$', FileView.as_view()),
 url(r'^(?P<file_key>.+)/$', FileView.as_view()),

]