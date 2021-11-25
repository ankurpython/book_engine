# Django & Django REST framework test project.
The test project won't be used in any real environment.


## Summary:

Extend Django Project with Django REST Framework for a simple prebuild booking app that have:
- Listing object with two types - **booking_engine.models** :
    - Apartment(single_unit) have booking information (price) directly connected to it.
    - Hotels(multi-unit) have booking information (price) connected to each of their HotelRoomTypes.
- filtering through Listings and returning JSON response with available units based on search criterias.
- should handle large dataset of Listings.

1. There is a pre-build structure for Hotels/Apartments (could be changed or extended). Database is prefilled with information - **db.sqlite3**.
    - superuser
        - username: **admin**
        - password: **admin**

2. We should be able to **block days** ( make reservations ) for each **Apartment** or **HotelRoom**.
    - **new** Model for blocked (reserved) days must be created

3. NEW **endpoint** where we will get available Apartments and Hotels based on:
	- **available days** (date range ex.: "from 2021-12-09 to 2021-12-12")
            - Apartment should not have any blocked day inside the range
            - Hotel should have at least 1 Hotel Room available from any of the HotelRoomTypes
     - **max_price** (100):
		- Apartment price must be lower than max_price.
		- Hotel should have at least 1 Hotel Room without any blocked days in the range with price lower than max_price.

	- returned objects should be **sorted** from lowest to highest price.
		-  hotels should display the price of the **cheapest HotelRoomType** with **available HotelRoom**.


## Initial Project setup
    git clone https://bitbucket.org/staykeepersdev/bookingengine.git
    python -m venv venv
    pip install -r requirements.txt
    python manage.py runserver


## Test Case example:

For covering more test cases we are going to need at least one hotel with 3 Hotel Room Types:

- First with price=50 (below max_price) with blocked day inside the search criteria for all rooms(could be 1 room)

- Second with price=60 (below max_price) with blocked day insde the search criteria for one out of few rooms

- Third with price 200 (above max_price) 


## End points:

http://127.0.0.1:8000/listing/?max_price=100&check_in=2021-12-09&check_out=2021-12-12

Some additional endpoints:

    "hotel_room_types": "http://127.0.0.1:8000/hotel_room_types/",
    "hotel_room": "http://127.0.0.1:8000/hotel_room/",
    "booking_info": "http://127.0.0.1:8000/booking_info/",
    "booking": "http://127.0.0.1:8000/booking/"



## Screenshot

### 1. **Listing**

![Screenshot from 2021-11-25 15-19-32](https://user-images.githubusercontent.com/48859058/143432719-8e89f94a-1f14-42e4-9f75-82bed6823cba.png)




### 2.a. **Hotel Room Types and list**

![Screenshot from 2021-11-25 15-19-50](https://user-images.githubusercontent.com/48859058/143433152-88871ba1-9447-4b43-882a-309d69305cdb.png)



### 2.b **Hotel Room List**

![Screenshot from 2021-11-25 15-20-06](https://user-images.githubusercontent.com/48859058/143433375-ae11dbad-5175-437f-b4b7-63004e1b358d.png)


### 3.a **Booking Information**

![Screenshot from 2021-11-25 15-20-21](https://user-images.githubusercontent.com/48859058/143433657-15c6799a-a0a7-43d6-a0a2-023752b89246.png)


### 3.b **Booking Information**
![Screenshot from 2021-11-25 15-20-30](https://user-images.githubusercontent.com/48859058/143433746-eb04432f-f2d5-4549-aa10-21c72b8c768f.png)


## Thank you
