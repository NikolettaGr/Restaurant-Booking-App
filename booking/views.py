from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import BookingForm




def index(request):
     """
    Function enables user to view the home page.
    """
    return render(request, 'home.html')



@login_required
def add_booking(request):
    """
    Function enables user to make a booking
    and add it to the database.
    """
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()
            booking.user = request.user
            booking.save()
            messages.success(request, 'Booking successful.')
            return redirect('my_bookings')
        else:
            messages.error(request, 'Booking date must be in the future.')
    form = BookingForm()
    context = {
        'form': form
        }
    return render(request, 'booking.html', context)



