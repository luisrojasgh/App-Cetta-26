
from django.urls import path
from comercial.views import login

urlpatterns = [
    path('login/',login,name="login"),
   
]