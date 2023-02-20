from django.db import models


class Employee(models.Model):

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    patronymic = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    date_of_employment = models.DateField()
    salary = models.FloatField()
    supervisor_id = models.PositiveBigIntegerField()

