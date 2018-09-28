from django.conf.urls import url
from .views import *
from . import views

urlpatterns = [
    url(r'^login/', login),
    url(r'^get/', get),
    url(r'^set/', set),
    url(r'^delete/', delete),
    url(r'^$', UserView.as_view()),
]