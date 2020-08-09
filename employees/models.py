from django.db import models
from django.urls import reverse

class EmployeeManager(models.Manager):
    def search(self, query):
        return self.get_queryset().filter(models.Q(note_icontains=query) |
            models.Q(name_icontains=query) |
            models.Q(nickname_iexact=query) |
            models.Q(function_icontains=query))

class Employee(models.Model):
    name = models.CharField(max_length=250)
    birth = models.DateField(blank=True, null=True)
    nickname = models.CharField(max_length=80, blank=True, null=True)
    city = models.CharField(max_length=80, blank=True, null=True)
    street = models.CharField(max_length=200, blank=True, null=True)
    number = models.CharField(max_length=10, blank=True, null=True)
    complement = models.CharField(max_length=30, blank=True, null=True)
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
