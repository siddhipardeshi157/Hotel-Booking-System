from django.shortcuts import render
from .models import Room, Contact

def home(request):
    return render(request, "main/home.html")

def rooms(request):
    rooms = Room.objects.all()
    return render(request, "main/rooms.html", {"rooms": rooms})

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        Contact.objects.create(
            name=name,
            email=email,
            message=message
        )

        return render(request, "main/contact.html", {
            "success": "Message sent successfully!"
        })

    return render(request, "main/contact.html")