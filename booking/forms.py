from django import forms
from .models import Booking
from main.models import Room

class BookingForm(forms.ModelForm):

    room = forms.ModelChoiceField(
        queryset=Room.objects.all(),
        empty_label="Select Room Type"
    )

    class Meta:
        model = Booking
        fields = [
            'name',
            'email',
            'phone',
            'room',
            'check_in',
            'check_out',
            'num_rooms'
        ]