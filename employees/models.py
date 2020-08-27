from django.db import models
from django.urls import reverse
import datetime


class EmployeeManager(models.Manager):
    def search(self, query):
        if "Dia:" in query:
            day = query.split(":")[1]
            month = datetime.date.today().month
            return self.get_queryset().filter(models.Q(birth__day=day)).filter(models.Q(birth__month=month))
        elif "Mes:" in query:
            month = query.split(":")[1]
            return self.get_queryset().filter(models.Q(birth__month=month))
        else:    
            return self.get_queryset().filter(models.Q(note__icontains=query) |
                models.Q(name__icontains=query) |
                models.Q(nickname__iexact=query) |
                models.Q(function__icontains=query))

class Employee(models.Model):
    name = models.CharField(max_length=250)
    birth = models.DateField(blank=True, null=True)
    nickname = models.CharField(max_length=80, blank=True, null=True)
    city = models.CharField(max_length=80, blank=True, null=True)
    street = models.CharField(max_length=200, blank=True, null=True)
    number = models.CharField(max_length=10, blank=True, null=True)
    complement = models.CharField(max_length=100, blank=True, null=True)
    cep = models.CharField(max_length=15, blank=True, null=True)
    state = models.CharField(max_length=30, blank=True, null=True)
    neighborhood = models.CharField(max_length=60, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=25, blank=True, null=True)
    cellphone = models.CharField(max_length=25, blank=True, null=True)
    phone_home = models.CharField(max_length=25, blank=True, null=True)
    function = models.CharField(max_length=60, blank=True, null=True)
    note = models.TextField(blank=True, null=True)

    objects = EmployeeManager()

    def get_absolute_url(self):
        return reverse('employees:funcionario', args=[str(self.id)])
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["name"]
