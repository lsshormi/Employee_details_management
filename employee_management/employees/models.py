from django.db import models
from django.core.validators import RegexValidator

class Employee(models.Model):
    photo = models.ImageField(upload_to='employee_photos/')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15, validators=[
        RegexValidator(regex=r'^\d{11}$',
                message='Mobile number must be 11 digits.')
    ])
    date_of_birth = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

