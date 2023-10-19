from django import forms
from .models import Booking
from django.utils import timezone

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['full_name', 'phone_number', 'date', 'time', 'table', 'questions']

    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        help_text='Select a date',
    )
    
    def clean_date(self):
        date = self.cleaned_data.get('date')
        current_time = timezone.now().date()
        
        if date < current_time:
            raise forms.ValidationError('Booking date must be in the future.')

        return date