from django.db import models
from django.core.validators import RegexValidator
# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email= models.EmailField()
    ph_no= models.CharField(max_length=10, validators=[RegexValidator(r'^\d{10}$', 'Phone number must have 10 numbers only')])

    def __str__(self):
        return self.name