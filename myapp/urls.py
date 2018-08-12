from django.conf.urls import url,include
from django.contrib import admin
import myapp.urls

urlpatterns = [
    url(r'^',include(myapp.urls)),
]