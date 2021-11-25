from datetime import datetime

from django.db.models import Q
from django.utils.dateparse import parse_date
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet

from rest_framework.status import *
from listings.serializers import *


class Listings(ModelViewSet):
    serializer_class = BookingInfoSerializer

    def get_queryset(self):
        try:
            check_in = self.request.GET['check_in']
            check_out = self.request.GET['check_out']
            price = int(self.request.GET['max_price'])
        except:
            return Response({"msg": "Invalid Arguments"}, status=HTTP_400_BAD_REQUEST)

        # obj = Blocked.objects.filter(
        #      Q(check_in__gte=check_in, check_in__lte=check_out) or
        #      Q(check_out__gte=check_in, check_out__lte=check_out) or
        #      Q(check_in__lte=check_in, check_out__gte=check_out)
        # ).values_list("hotel_room")

        c1 = Blocked.objects.filter(check_in__gte=check_in, check_in__lte=check_out).values_list("hotel_room")
        c2 = Blocked.objects.filter(check_out__gte=check_in, check_out__lte=check_out).values_list("hotel_room")
        c3 = Blocked.objects.filter(check_in__lte=check_in, check_out__gte=check_out).values_list("hotel_room")

        ls = list(c1)
        ls.extend(list(c2))
        ls.extend(list(c3))
        print(ls)
        queryset = BookingInfo.objects.exclude(listing_id__in=ls).filter(price__lte=price)# .order_by("price")
        return queryset


class HotelRoomTypes(ModelViewSet):
    serializer_class = HotelRoomTypeSerializer
    queryset = HotelRoomType.objects.all()


class HotelRooms(ModelViewSet):
    serializer_class = HotelRoomSerializer
    queryset = HotelRoom.objects.all()


class BookingInfos(ModelViewSet):
    serializer_class = BookingInfoSerializer
    queryset = BookingInfo.objects.all()


class Bookings(ModelViewSet):
    serializer_class = BookingSerializer
    queryset = Blocked.objects.all()

    def create(self, request, *args, **kwargs):
        data = request.data
        c1 = Blocked.objects.filter(hotel_room=data['hotel_room'], check_in__gte=data['check_in'], check_in__lte=data['check_out']).exists()
        c2 = Blocked.objects.filter(hotel_room=data['hotel_room'], check_out__gte=data['check_in'], check_out__lte=data['check_out']).exists()
        c3 = Blocked.objects.filter(hotel_room=data['hotel_room'], check_in__lte=data['check_in'], check_out__gte=data['check_out']).exists()

        if c1 or c2 or c3:
            return Response({"msg": "room already booked "}, status=HTTP_400_BAD_REQUEST)
        else:
            serializer = BookingSerializer(data=data)

            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.error_messages, status=HTTP_400_BAD_REQUEST)

            return Response({"msg": "Created"}, status=HTTP_200_OK)
