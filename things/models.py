from django.db import models
from django.core.exceptions import ValidationError

def validate_quantity(value):
    if value < 0 or value > 100:
        raise(ValidationError("Quantity needs to be a value from 0 to 100!"))

class Thing(models.Model):
    name = models.CharField(
        max_length=30, 
        unique=True,
        blank=False
    )
    description = models.CharField(
        max_length=120, 
        unique=False,
        blank=True
    )
    quantity = models.IntegerField(
        unique=False,
        validators=[validate_quantity]
    )


