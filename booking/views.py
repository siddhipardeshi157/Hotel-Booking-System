from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Booking
from main.models import Room
from datetime import datetime


def booking_page(request):
    rooms = Room.objects.all()
    return render(request, "booking/booking.html", {"rooms": rooms})

def create_booking(request):

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        room_id = request.POST.get("room")
        check_in = request.POST.get("check_in")
        check_out = request.POST.get("check_out")
        number_of_rooms = int(request.POST.get("number_of_rooms"))

        if not room_id:
            return HttpResponse("Please select a room ❌")

        try:
            room = Room.objects.get(id=room_id)
        except Room.DoesNotExist:
            return HttpResponse("Room not found ❌")

        check_in_date = datetime.strptime(check_in, "%Y-%m-%d").date()
        check_out_date = datetime.strptime(check_out, "%Y-%m-%d").date()

        nights = (check_out_date - check_in_date).days

        total_price = float(nights) * float(room.price) * float(number_of_rooms)

        print("DEBUG TOTAL PRICE:", total_price, type(total_price))

        existing_bookings = Booking.objects.filter(
            room=room,
            check_in__lt=check_out_date,
            check_out__gt=check_in_date
        )

        booked_rooms = sum(b.number_of_rooms for b in existing_bookings)

        if booked_rooms + number_of_rooms <= 20:

            booking = Booking.objects.create(
                name=name,
                email=email,
                phone=phone,
                room=room,
                check_in=check_in_date,
                check_out=check_out_date,
                number_of_rooms=number_of_rooms,
                total_price=total_price   
            )

            
            send_mail(
                subject="Booking Confirmed - Golden Tulip",
                message=f"""
            Hi {name},

            Your booking is confirmed!

            Room: {room.name}
            Check-in: {check_in_date}
            Check-out: {check_out_date}
            Rooms: {number_of_rooms}

            Total Price: ₹{total_price}

            Thank you for choosing us!🤗
            """,
                from_email='your_email@gmail.com',
                recipient_list=[email],
                fail_silently=True,
)
            return redirect("confirmation", booking_id=booking.id)

        else:
            rooms = Room.objects.all()
            return render(request, "booking/booking.html", {
                "rooms": rooms,
                "error": "Only limited rooms available for selected dates."
            })

    return redirect("booking")

def booking(request):
    rooms = Room.objects.all()
    return render(request, "booking/booking.html", {
        "rooms": rooms
    })

def confirmation(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    return render(request, "booking/confirmation.html", {
        "booking": booking
    })
