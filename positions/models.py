from django.db import models
from django.urls import reverse

class PositionManager(models.Manager):
    def search(self, query):
        return self.get_queryset().filter(models.Q(position__iexact=query) | models.Q(handling__icontains=query) | models.Q(abbreviation__icontains=query))

class Position(models.Model):
    position = models.CharField(max_length=150, unique=True)
    handling = models.CharField(max_length=100, blank=True, null=True)
    abbreviation = models.CharField(max_length=50, blank=True, null=True)

    objects = PositionManager()

    def get_absolute_url(self):
        #return "cargos/{}".format(self.id)
        return reverse('positions:cargo', args=[str(self.id)])
    
    def __str__(self):
        return self.position
    
    class Meta:
        ordering = ["position"]
