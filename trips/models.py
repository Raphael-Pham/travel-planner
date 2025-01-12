from django.db import models

# Create your models here.
class Trip(models.Model):
    # ! add field to link a trip to a user or multiple users once shared
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Transportation(models.Model):
    MODE_CHOICES = [
        ('plane', 'Plane'),
        ('train', 'Train'),
        ('bus', 'Bus'),
        ('car', 'Car'),
        ('boat', 'Boat'),
        ('bike', 'Bike'),
        ('walk', 'Walk'),
    ]

    trip = models.ForeignKey(Trip, related_name='transportations', on_delete=models.CASCADE)
    mode = models.CharField(max_length=1, choices=MODE_CHOICES)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    departure_location = models.CharField(max_length=255)
    arrival_location = models.CharField(max_length=255)
    details = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.mode} from {self.departure_location} to {self.arrival_location}"
    
class Accomodation(models.Model):
    trip = models.ForeignKey(Trip, related_name='accomodations', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    details = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} at {self.address} from {self.check_in} to {self.check_out}"