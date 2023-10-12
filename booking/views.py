from django.shortcuts import render
from django.contrib.auth.models import User



def index(request):
    return render(request, 'index.html')



def login(request):
    return render(request, 'login.html')

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
    return render(request, 'restaurant/booking.html', context)



