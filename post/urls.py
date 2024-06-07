
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('post/', views.post_form , name= 'add_post'),
    path('edit/<int:id>', views.edit_post , name= 'edit_post'),
    path('delete/<int:id>', views.delete , name= 'delete_post'),
 
]
