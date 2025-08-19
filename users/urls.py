from django.urls import path
from. import views

urlpattern = [
   path('', views.all_user, name="all_user")
]