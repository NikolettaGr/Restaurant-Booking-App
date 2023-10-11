from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    
    list_display = ('user', 'full_name',
                    'date', 'time',
                    'table', 'phone_number')
    search_fields = ('full_name',
                     'date', 'time',
                     'phone_number')
    list_filter = ('full_name',
                   'date', 'time', 'table',
                   'phone_number')