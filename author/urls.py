
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('register/', views.register , name= 'register'),
    path('log_in/', views.log_in , name= 'log_in'),
    path('log_out/', views.log_out , name= 'log_out'),
    path('profile/', views.profile , name= 'profile'),
    path('edit_profile/', views.edit_profile , name= 'edit_profile'),
    path('pass_change/', views.pass_change , name= 'pass_change'),
 
]
