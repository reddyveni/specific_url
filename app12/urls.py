from django.urls import path
from app12.views import *
app_name='something'
urlpatterns=[
    path('mom/',mom,name='mom'),
]