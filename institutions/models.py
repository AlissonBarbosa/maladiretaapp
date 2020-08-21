from django.db import models

from django.urls import reverse

class InstitutionManager(models.Manager):
    def search(self, query):
        return self.get_queryset().filter(models.Q(name__icontains=query) | models.Q(city__icontains=query) | models.Q(email__icontains=query))

class Institution(models.Model):
    name = models.CharField(max_length=250, unique=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=80, blank=True, null=True)
    street = models.CharField(max_length=200, blank=True, null=True)
    number = models.CharField(max_length=10, blank=True, null=True)
    complement = models.CharField(max_length=30, blank=True, null=True)
    cep = models.CharField(max_length=15, blank=True, null=True)
    state = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    neighborhood = models.CharField(max_length=60, blank=True, null=True)
    note = models.TextField(blank=True, null=True)

    objects = InstitutionManager()

    def get_absolute_url(self):
        return reverse('institutions:instituicao', args=[str(self.id)])
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["name"]
