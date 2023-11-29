from django.urls import path
from .views import *
# dreg/urls.py
# dreg/urls.py

from django.urls import path
from .views import donorregdisplay, updateData, delete



urlpatterns = [
    path('', donorregdisplay, name='dregsite'),
    path('donors/', donorregdisplay, name='dregdisplay'),
    path('donorreg/update/<int:id>/', updateData, name='updateData'),
    path('delete/<int:id>/', delete, name='deleteData'),
]

