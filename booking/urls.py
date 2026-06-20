from django.urls import path
from . import views

urlpatterns = [
    path("", views.booking, name="booking"),
    path("create/", views.create_booking, name="create_booking"),
    path('confirmation/<int:booking_id>/', views.confirmation, name='confirmation')
    ]