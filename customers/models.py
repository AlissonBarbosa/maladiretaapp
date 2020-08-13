from django.db import models
from django.urls import reverse

class CustomerManager(models.Manager):
    def search(self, query):
        return self.get_queryset().filter(models.Q(leadership__name__icontains=query) |
            models.Q(name__icontains=query) |
            models.Q(nickname__iexact=query) |
            models.Q(profession__icontains=query) |
            models.Q(reference__icontains=query))

class Customer(models.Model):
    name = models.CharField(max_length=250)
    birth = models.DateField(blank=True, null=True)
    nickname = models.CharField(max_length=80, blank=True, null=True)
    reference = models.CharField(max_length=180, blank=True, null=True)
    city = models.CharField(max_length=80, blank=True, null=True)
    street = models.CharField(max_length=200, blank=True, null=True)
    number = models.CharField(max_length=10, blank=True, null=True)
    complement = models.CharField(max_length=30, blank=True, null=True)
    cep = models.CharField(max_length=15, blank=True, null=True)
    state = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    neighborhood = models.CharField(max_length=60, blank=True, null=True)
    rg = models.CharField(max_length=10, blank=True, null=True, unique=True)
    cpf = models.CharField(max_length=10, blank=True, null=True, unique=True)
    phone_number = models.CharField(max_length=25, blank=True, null=True)
    cellphone = models.CharField(max_length=25, blank=True, null=True)
    phone_home = models.CharField(max_length=25, blank=True, null=True)
    leadership = models.ForeignKey('leadership.Leadership', on_delete=models.CASCADE, blank=True, null=True)
    subscription = models.CharField(max_length=30, blank=True, null=True)
    zone = models.CharField(max_length=30, blank=True, null=True)
    section = models.CharField(max_length=30, blank=True, null=True)
    profession = models.CharField(max_length=80, blank=True, null=True)

    objects = CustomerManager()

    def get_absolute_url(self):
        return reverse('customers:cliente', args=[str(self.id)])
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["name"]