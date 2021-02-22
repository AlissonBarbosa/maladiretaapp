from django.db import models
from django.urls import reverse

class CustomerManager(models.Manager):
    def search(self, query):
        if "Referencia:" in query:
            office = query.split(":")[1].replace(" ","")
            return self.get_queryset().filter(models.Q(reference__icontains=office))
        elif "Lideranca:" in query:
            office = query.split(":")[1].replace(" ","")
            return self.get_queryset().filter(models.Q(leadership__icontains=office))
        elif "Dia:" in query:
            day = query.split(":")[1]
            month = datetime.date.today().month
            return self.get_queryset().filter(models.Q(birth__day=day)).filter(models.Q(birth__month=month))
        elif "Mes:" in query:
            month = query.split(":")[1]
            return self.get_queryset().filter(models.Q(birth__month=month))
        return self.get_queryset().filter(models.Q(name__icontains=query) |
            models.Q(nickname__iexact=query) |
            models.Q(profession__icontains=query))

class Customer(models.Model):
    name = models.CharField(max_length=250)
    birth = models.DateField(blank=True, null=True)
    nickname = models.CharField(max_length=80, blank=True, null=True)
    reference = models.CharField(max_length=180, blank=True, null=True)
    city = models.CharField(max_length=80, blank=True, null=True)
    street = models.CharField(max_length=200, blank=True, null=True)
    number = models.CharField(max_length=25, blank=True, null=True)
    complement = models.CharField(max_length=30, blank=True, null=True)
    cep = models.CharField(max_length=15, blank=True, null=True)
    state = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    neighborhood = models.CharField(max_length=60, blank=True, null=True)
    rg = models.CharField(max_length=25, blank=True, null=True)
    cpf = models.CharField(max_length=14, blank=True, null=True)
    phone_number = models.CharField(max_length=25, blank=True, null=True)
    cellphone = models.CharField(max_length=25, blank=True, null=True)
    phone_home = models.CharField(max_length=25, blank=True, null=True)
    leadership = models.CharField(max_length=25, blank=True, null=True)
    subscription = models.CharField(max_length=30, blank=True, null=True)
    zone = models.CharField(max_length=30, blank=True, null=True)
    section = models.CharField(max_length=30, blank=True, null=True)
    profession = models.CharField(max_length=80, blank=True, null=True)
    recurrence = models.CharField(max_length=60, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    updated = models.DateField(auto_now=True)
    location_reference = models.TextField(blank=True, null=True)
    old_id = models.CharField(max_length=15, blank=True, null=True)

    objects = CustomerManager()

    def get_absolute_url(self):
        return reverse('customers:cliente', args=[str(self.id)])
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["name"]