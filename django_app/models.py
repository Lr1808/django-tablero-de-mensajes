from django.db import models

# Create your models here.
class Posr(models.Model):
    text = models.TextField()
    def __str__(self):
        return self.text[:50]



class product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

