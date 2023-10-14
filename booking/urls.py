from django.urls import path
from .views import home, add_booking, view_booking, edit_booking

urlpatterns = [
    path('', home, name='home'),
    path('booking/', add_booking, name='booking'),
    path('view_booking/', view_booking, name='view_booking'),
    path('edit_booking/<int:booking_id>/', edit_booking, name='edit_booking'),
]

