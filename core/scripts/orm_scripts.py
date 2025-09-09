from core.models import Restaurant,Rating,Sale
from django.utils import timezone
from django.db import connection
from django.contrib.auth.models import User
from pprint import pprint
def run():

    #restaurant = Restaurant()
    #restaurant.name = 'My Italian Restaurant'
    #restaurant.date_opened = timezone.now()
    #restaurant.latitude = 50.2
    #restaurant.longitude = 50.2
    #restaurant.restaurant_type = Restaurant.TypeChoices.ITALIAN

    #restaurant.save()
    
    #restaurant = Restaurant.objects.all()
    #print(restaurant)
    #print(connection.queries)

    #restaurant = Restaurant.objects.first()
    #print(restaurant)
    #print(connection.queries)

    #restaurant = Restaurant.objects.all()[0]
    #print(restaurant)
    #print(connection.queries)

    #Restaurant.objects.create(
        #name = "Pizza Shop",
        #date_opened = timezone.now(),
        #restaurant_type = Restaurant.TypeChoices.ITALIAN,
        #latitude = 51.2,
        #longitude = 51.2)#
    #print(connection.queries)
    
    #print(Restaurant.objects.count())
    #print(connection.queries)

    #print(Restaurant.objects.last())
    #print(connection.queries)

    #restaurant = Restaurant.objects.first()
    #user = User.objects.first()
    #Rating.objects.create(user=user, restaurant=restaurant,rating =3)

    #print(Rating.objects.all())

    #print(Rating.objects.filter(rating=3))
    #print(Rating.objects.filter(rating=3))
    #print(Rating.objects.filter(rating=5))
    #print(connection.queries)
    
    #print(Rating.objects.exclude(rating__lte=3))
    #print(connection.queries)

    #restaurant = Restaurant.objects.first()
    #print(restaurant.name)

    #restaurant.name = 'hgdgdgdwdgwg'
    #restaurant.save()

    #pprint(connection.queries)

    #rating = Rating.objects.first()
    #print(rating.rating)
    #pprint(connection.queries)

    #rating = Rating.objects.first()
    #print(rating.restaurant)
    #pprint(connection.queries)

    #restaurant = Restaurant.objects.first()
    #print(restaurant.ratings.all())

    #Sale.objects.create(
        #restaurant = Restaurant.objects.first(),
        #income = 2.33,
        #datetime = timezone.now()


    #Sale.objects.create(
        #restaurant = Restaurant.objects.first(),
        #income = 5.33,
        #datetime = timezone.now()

    #Sale.objects.create(
        #restaurant = Restaurant.objects.first(),
        #income = 8.33,
        #datetime = timezone.now()
    #restaurant = Restaurant.objects.first()
    #print(restaurant.sales.all())

    user = User.objects.first()
    restaurant = Restaurant.objects.first()
    print(Rating.objects.get_or_create(
        restaurant = restaurant,
        user = user,
        rating = 4
    ))

    pprint(connection.queries)