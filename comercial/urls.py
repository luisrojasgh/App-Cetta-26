
from django.urls import path
from comercial.views import login_ususrio

urlpatterns = [
    path('login/',login_ususrio,name="login"),
   
]