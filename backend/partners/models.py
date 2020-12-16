from django.db import models

# Bakim merkezi tablosunu olusturma

class Partner(models.Model):

    class Gender(models.TextChoices):
        WOMEN = 'W'
        MEN = 'M'
        BOTH = 'B'

    brandName = models.CharField(max_length=50)
    owner = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=Gender.choices)
    locationID = models.CharField(max_length=50)
    availability = models.BooleanField(default= False)

    class Meta:
        db_table = "partners"