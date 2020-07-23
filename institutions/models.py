from django.db import models

from django.urls import reverse

class Institution(models.Model):
    name = models.CharField(max_length=250, unique=True)
    phone_number = models.CharField(max_length=25)
    city = models.CharField(max_length=80)
    street = models.CharField(max_length=200)
    number = models.CharField(max_length=10)
    complement = models.CharField(max_length=30)
    cep = models.CharField(max_length=15)
    state = models.CharField(max_length=30)

    def get_absolute_url(self):
        return reverse('institutions:instituicao', args=[str(self.id)])
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["name"]
