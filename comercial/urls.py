
from django.urls import path
from comercial.views import login_ususrio, logout_ususrio

urlpatterns = [
    path('login/',login_ususrio,name="login"),
    path('logout/',logout_ususrio,name="logout"),
   
]