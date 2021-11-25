from rest_framework.serializers import ModelSerializer

from listings.models import *


class ListingSerializer(ModelSerializer):
    class Meta:
        model = Listing
        fields = '__all__'


class HotelRoomTypeSerializer(ModelSerializer):
    class Meta:
        model = HotelRoomType
        fields = '__all__'


class HotelRoomSerializer(ModelSerializer):
    class Meta:
        model = HotelRoom
        fields = '__all__'


class BookingInfoSerializer(ModelSerializer):
    class Meta:
        model = BookingInfo
        fields = '__all__'
        depth = 1


class BookingSerializer(ModelSerializer):
    class Meta:
        model = Blocked
        fields = '__all__'