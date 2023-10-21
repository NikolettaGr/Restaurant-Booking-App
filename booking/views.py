from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import BookingForm
from .models import Booking


def home(request):
    """Function enables user to view the home page."""
    return render(request, 'booking/home.html')


def menu(request):
    """Function enables user to view the menu page."""
    return render(request, 'booking/menu.html')


def contact(request):
    """Function enables user to view the contact page."""
    return render(request, 'booking/contact.html')


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
            return redirect('view_booking')
        else:
            messages.error(request, 'Booking date must be in the future.')
    form = BookingForm()
    context = {
        'form': form
        }
    return render(request, 'booking/booking.html', context)


@login_required
def view_booking(request):
    """
    Function enables user to view a booking after
    it has been made and added to the database.
    """
    bookings = Booking.objects.filter(user__in=[request.user])
    context = {
        'bookings': bookings
    }
    return render(request, 'booking/view_booking.html', context)


@login_required
def edit_booking(request, booking_id):
    """
    Function enables user to edit a booking after
    it has been made and added to the database.
    """
    book = get_object_or_404(Booking, id=booking_id)
    if request.method == "POST":
        form = BookingForm(request.POST, instance=book)
        if form.is_valid():
            booking = form.save()
            booking.user = request.user
            booking.save()
            messages.success(request, 'Your booking has been updated.')
            return redirect('view_booking')
        else:
            messages.error(request, 'Booking date must be in the future.')
    form = BookingForm(instance=book)
    context = {
        'form': form
    }
    return render(request, 'booking/edit_booking.html', context)


@login_required
def delete_booking(request, booking_id):
    """Function enables the user to delete a booking."""
    booking = get_object_or_404(Booking, id=booking_id)

    if request.method == "POST":
        booking.delete()
        messages.success(request, 'Your booking has been deleted.')
        return redirect('view_booking')

    context = {
        'booking': booking
    }
    return render(request, 'booking/delete_booking.html', context)
