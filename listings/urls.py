from django.urls import path, include
from rest_framework.routers import DefaultRouter

from listings.views import *

router = DefaultRouter()
router.register('listing', Listings, basename='listing')
router.register('hotel_room_types', HotelRoomTypes, basename='hotel_room_types')
router.register('hotel_room', HotelRooms, basename='hotel_room')
router.register('booking_info', BookingInfos, basename='booking_info')
router.register('booking', Bookings, basename='booking')
urlpatterns = router.urls
