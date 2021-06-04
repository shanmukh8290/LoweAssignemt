from django.contrib import admin
from django.urls import path
from .views import createUsers, getUser, deleteUser, updateUser

urlpatterns = [
    path('create/', createUsers),
    path('userDetails/', getUser),
    path('deleteUser/', deleteUser),
    path('updateUser/', updateUser),
]