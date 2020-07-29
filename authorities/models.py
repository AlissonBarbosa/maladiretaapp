from django.db import models

from django.urls import reverse

class Authoritie(models.Model):
    name = models.CharField(max_length=250)
    genre = models.CharField(max_length=25)
    created = models.DateField(auto_now_add=True)
    birth = models.DateField()
    position = models.ForeignKey('positions.Position', on_delete=models.CASCADE, blank=True, null=True)
    institution = models.ForeignKey('institutions.Institution', on_delete=models.CASCADE, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('authorities:autoridade', args=[str(self.id)])
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["name"]
