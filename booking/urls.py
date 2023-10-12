from django.urls import path
from .views import index, login, add_booking

urlpatterns = [
    path('', index),
    path('login/', login),
    path('booking/', add_booking)
]

