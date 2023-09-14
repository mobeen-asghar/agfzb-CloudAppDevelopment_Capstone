from django.db import models
from django.utils.timezone import now

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
class CarMake(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.name

# <HINT> Create a Car Model model `class CarModel(models.Model):`:
class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    type_c = models.CharField(max_length=10, choices=(('Sedan', 'Sedan',), ('SUV', 'SUV'), ('HATCHBACK', 'HATCHBACK'),('WAGON', 'WAGON')))
    dealer_id = models.IntegerField()
    year = models.DateField()

    def __str__(self):
        return self.name


# <HINT> Create a plain Python class `CarDealer` to hold dealer data
class CarDealer:
    def __init__(self, address, city, full_name, id, lat, long, short_name, st, zip):
        self.address = address
        self.city = city
        self.full_name = full_name
        self.id = id
        self.lat = lat
        self.long = long
        self.short_name = short_name
        self.st = st
        self.zip = zip

    def __str__(self):
        return "Dealer name: " + self.full_name

# <HINT> Create a plain Python class `DealerReview` to hold review data
class DealerReview:
    def __init__(self, dealership, name, purchase, review, purchase_date, car_make, car_model, car_year, sentiment, id):
        self.dealership = dealership
        self.name = name
        self.purchase = purchase
        self.review = review
        self.purchase_date = purchase_date
        self.car_make = car_make
        self.car_model = car_model
        self.car_year = car_year
        self.sentiment = sentiment
        self.id = id