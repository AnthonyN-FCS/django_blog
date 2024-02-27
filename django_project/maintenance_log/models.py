from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Trip(models.Model):
    FUEL_CHOICES = {
        ('full','Full'),
        ('three-quarters', '3/4 Full'),
        ('half', '1/2 Full'),
        ('quarter', '1/4 Full'),
        ('empty', 'Empty'),
    }
    TYPE_CHOICES = (
        ('out-bound', 'Out-bound'),
        ('in-bound', 'In-bound'),
    )

    driver = models.ForeignKey(User, on_delete=models.CASCADE)
    mileage = models.IntegerField()
    date_driven = models.DateTimeField()
    fuel = models.CharField(max_length=15, choices=FUEL_CHOICES)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    engine_light_on = models.BooleanField(default=False)
    noisy_brakes = models.BooleanField(default=False)
    other_issues = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
       return f"{self.type} trip on {self.date_driven.strftime('%Y-%m-%d')} by {self.driver.username}"