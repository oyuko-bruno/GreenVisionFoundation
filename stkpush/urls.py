from django.urls import path

from stkpush import views


app_name = "stkpush"

urlpatterns = [
    path('home', views.home, name="home"),
    path('token', views.token, name='token'),
    path('pay', views.pay, name='pay'),
    path('', views.stk, name="stk")

]
