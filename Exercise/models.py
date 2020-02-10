from django.contrib.gis.db import models
from enum import Enum
from django_enum_choices.fields import EnumChoiceField

# Create your models here.


class State(Enum):
    A = 'To validate'
    B = 'Validated'
    C = 'Solved'


class Category(Enum):
    A = 'CONSTRUCTION'
    B = 'SPECIAL_EVENT'
    C = 'INCIDENT'
    D = 'WEATHER_CONDITION'
    E = 'ROAD_CONDITION'


class Occurrence(models.Model):
    description = models.CharField(max_length=500)
    # Couldn't install GDAL
    location = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    date_creation = models.DateField()
    date_update = models.DateField()
    state = EnumChoiceField(State, default=State.A)
    category = EnumChoiceField(Category)

