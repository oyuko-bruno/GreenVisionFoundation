from django.urls import path
from .views import *
from homeapp import views
from django.urls import include, path
from stkpush import views 
from .views import act
from .views import about
from .views import service
from .views import blog
from .views import gallery
from .views import green
from .views import form_submission

app_name = "homeapp"

urlpatterns = [
    path('', green, name='homepage'),
    path('index-2.html', green, name='homepage'),
    path('act-now.html', act, name='actpage'),
    path('about-1.html', about, name='aboutpage'),
    path('service.html', service, name='servicepage'),
    path(' blog-full-with-right-sidebar.html',blog ,name='blogpage'),
    path('gallery-3-columns-without-caption.html', gallery, name='gallarypage'),
    path('submit-form/', form_submission, name='form_submission'),
]
  





   