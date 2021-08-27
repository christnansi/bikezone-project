from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField

# Create your models here.

class Bike(models.Model):

    state_choice = (
        ('AL', 'Alabama'),
        ('AK', 'Alaska'),
        ('AZ', 'Arizona'),
        ('AR', 'Arkansas'),
        ('CA', 'California'),
        ('CO', 'Colorado'),
        ('CT', 'Connecticut'),
        ('DE', 'Delaware'),
        ('DC', 'District Of Columbia'),
        ('FL', 'Florida'),
        ('GA', 'Georgia'),
        ('HI', 'Hawaii'),
        ('ID', 'Idaho'),
        ('IL', 'Illinois'),
        ('IN', 'Indiana'),
        ('IA', 'Iowa'),
        ('KS', 'Kansas'),
        ('KY', 'Kentucky'),
        ('LA', 'Louisiana'),
        ('ME', 'Maine'),
        ('MD', 'Maryland'),
        ('MA', 'Massachusetts'),
        ('MI', 'Michigan'),
        ('MN', 'Minnesota'),
        ('MS', 'Mississippi'),
        ('MO', 'Missouri'),
        ('MT', 'Montana'),
        ('NE', 'Nebraska'),
        ('NV', 'Nevada'),
        ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'),
        ('NY', 'New York'),
        ('NC', 'North Carolina'),
        ('ND', 'North Dakota'),
        ('OH', 'Ohio'),
        ('OK', 'Oklahoma'),
        ('OR', 'Oregon'),
        ('PA', 'Pennsylvania'),
        ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'),
        ('SD', 'South Dakota'),
        ('TN', 'Tennessee'),
        ('TX', 'Texas'),
        ('UT', 'Utah'),
        ('VT', 'Vermont'),
        ('VA', 'Virginia'),
        ('WA', 'Washington'),
        ('WV', 'West Virginia'),
        ('WI', 'Wisconsin'),
        ('WY', 'Wyoming'),
    )

    year_choice = []
    for r in range(2000, (datetime.now().year+1)):
        year_choice.append((r,r))

    features_choices = (
        ('Integrated Braking System', 'Integrated Braking System'),
        ('i3s Technology', 'i3s Technology'),
        ('Speedometer', 'Speedometer'),
        ('Odometer', 'Odometer'),
        ('Tripmeter', 'Tripmeter'),
        ('Alarm System', 'Alarm System'),
        ('Passenger Footrest', 'Passenger Footrest'),
        ('Power Steering', 'Power Steering'),
        ('XSens Technology', 'XSens Technology'),
        ('Direct Fuel Injection', 'Direct Fuel Injection'),
        ('Auto Start/Stop', 'Auto Start/Stop'),
        ('Wind Deflector', 'Wind Deflector'),
    )


    bike_title = models.CharField(max_length=255)
    state = models.CharField(choices=state_choice, max_length=100)
    city = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField(('year'), choices=year_choice)
    condition = models.CharField(max_length=100)
    price = models.IntegerField()
    description = RichTextField()
    bike_photo = models.ImageField(upload_to='photos/%Y/%m/')
    bike_photo1 = models.ImageField(upload_to='photos/%Y/%m/')
    bike_photo2 = models.ImageField(upload_to='photos/%Y/%m/')
    bike_photo3 = models.ImageField(upload_to='photos/%Y/%m/')
    bike_photo4 = models.ImageField(upload_to='photos/%Y/%m/')
    bike_photo5 = models.ImageField(upload_to='photos/%Y/%m/', blank=True)
    features = MultiSelectField(choices=features_choices, max_length=200)
    engine = models.CharField(max_length=100)
    transmission = models.CharField(max_length=100)
    body_type = models.CharField(max_length=100)
    brakes = models.CharField(max_length=50)
    power = models.CharField(max_length=50)
    miles = models.IntegerField()
    vin_no = models.CharField(max_length=150)
    milage = models.IntegerField()
    No_of_cylinders = models.IntegerField()
    fuel_capacity = models.CharField(max_length=50)
    tyre_type = models.CharField(max_length=50)
    No_of_owners = models.IntegerField()
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)



    def __str__(self):
        return self.bike_title
