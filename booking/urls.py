from django.urls import path
from .views import index, add_booking

urlpatterns = [
    path('', index),
    path('booking/', add_booking, name='booking'),

]

