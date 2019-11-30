from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=30)
    pin = models.CharField(max_length=10)
    cgpa = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return self.name
