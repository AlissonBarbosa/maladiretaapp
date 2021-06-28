from django.db import models
from django.urls import reverse
import datetime

class LeadershipManager(models.Manager):
    def search(self, query):
        if "Dia:" in query:
            day = query.split(":")[1]
            month = datetime.date.today().month
            return self.get_queryset().filter(models.Q(birth__day=day)).filter(models.Q(birth__month=month))
        elif "Mes:" in query:
            month = query.split(":")[1]
            return self.get_queryset().filter(models.Q(birth__month=month)).order_by('birth__month', 'birth__day')
        elif "Cargo: " in query:
            position = query.split("Cargo: ")[1]
            return self.get_queryset().filter(models.Q(position__position__iexact=position))
        elif "Referencia: " in query:
            office = query.split("Referencia: ")[1]
            return self.get_queryset().filter(models.Q(office__icontains=office))
        elif "Entre: " in query:
            first_day = query.split(":")[1].split(" e ")[0]
            last_day = query.split(":")[1].split(" e ")[1].split(" ")[0]
            month = query.split(" de ")[1]
            return self.get_queryset().filter(models.Q(birth__day__gte=first_day)).filter(models.Q(birth__day__lte=last_day)).filter(models.Q(birth__month=month)).order_by('birth__month', 'birth__day')
        else:
            return self.get_queryset().filter(models.Q(name__icontains=query) | 
                models.Q(nickname__icontains=query) | 
                models.Q(note__icontains=query) | 
                models.Q(rg__iexact=query) | 
                models.Q(cpf__iexact=query))

class Leadership(models.Model):
    name = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=25, blank=True, null=True)
    cellphone = models.CharField(max_length=25, blank=True, null=True)
    phone_home = models.CharField(max_length=25, blank=True, null=True)
    city = models.CharField(max_length=80, blank=True, null=True)
    street = models.CharField(max_length=200, blank=True, null=True)
    number = models.CharField(max_length=10, blank=True, null=True)
    complement = models.CharField(max_length=150, blank=True, null=True)
    cep = models.CharField(max_length=15, blank=True, null=True)
    state = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    neighborhood = models.CharField(max_length=60, blank=True, null=True)
    rg = models.CharField(max_length=20, blank=True, null=True)
    cpf = models.CharField(max_length=20, blank=True, null=True)
    birth = models.DateField(blank=True, null=True)
    updated = models.DateField(auto_now_add=True)
    nickname = models.CharField(max_length=60, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    position = models.ForeignKey('positions.Position', on_delete=models.SET_NULL, blank=True, null=True)
    office = models.CharField(max_length=150, blank=True, null=True)
    pendency = models.CharField(max_length=350, blank=True, null=True)

    objects = LeadershipManager()

    def get_absolute_url(self):
        return reverse('leadership:lideranca', args=[str(self.id)])
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["name"]