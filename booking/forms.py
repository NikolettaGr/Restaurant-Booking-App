from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['full_name', 'phone_number', 'date', 'time', 'table', 'questions']

    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        help_text='Select a date',
    )