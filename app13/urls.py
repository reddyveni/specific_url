from django.urls import path
from app13.views import *
app_name='moyamoya'
urlpatterns=[
    path('dad/',dad,name='dad'),
]