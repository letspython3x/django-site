from django.db import models

# Create your models here.
class UserDetails(models.Model):
    Name = models.CharField(max_length=30)
    Age = models.DecimalField(max_digits=2, decimal_places=2)

