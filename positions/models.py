from django.db import models
from django.urls import reverse

class Position(models.Model):
    position = models.CharField(max_length=150)
    handling = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=50)

    def get_absolute_url(self):
        #return "cargos/{}".format(self.id)
        return reverse('positions:cargo', args=[str(self.id)])
    
    def __str__(self):
        return self.position
    
