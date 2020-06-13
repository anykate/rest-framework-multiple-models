from django.db import models


# Create your models here.
class Employee(models.Model):
    empname = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    salary = models.IntegerField()

    def __str__(self):
        return self.empname

    class Meta:
        verbose_name = 'employee'
        verbose_name_plural = 'employees'


class Sport(models.Model):
    sportname = models.CharField(max_length=10)

    def __str__(self):
        return self.sportname

    class Meta:
        verbose_name = 'sport'
        verbose_name_plural = 'sports'
