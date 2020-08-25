from django.db import models
import datetime

from django.urls import reverse

class AuthoritieManager(models.Manager):
    def search(self, query):
        if "Dia:" in query:
            day = query.split(":")[1]
            month = datetime.date.today().month
            return self.get_queryset().filter(models.Q(birth__day=day)).filter(models.Q(birth__month=month))
        elif "Mes:" in query:
            month = query.split(":")[1]
            return self.get_queryset().filter(models.Q(birth__month=month))
        else:
            return self.get_queryset().filter(models.Q(institution__name__icontains=query) |
                    models.Q(position__position__icontains=query) |
                    (models.Q(name__icontains=query) |
                    (models.Q(email__icontains=query))))

class Authoritie(models.Model):
    name = models.CharField(max_length=250)
    updated = models.DateField(auto_now_add=True)
    birth = models.DateField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    position = models.ForeignKey('positions.Position', on_delete=models.CASCADE, blank=True, null=True)
    institution = models.ForeignKey('institutions.Institution', on_delete=models.CASCADE, blank=True, null=True)

    objects = AuthoritieManager()

    def get_absolute_url(self):
        return reverse('authorities:autoridade', args=[str(self.id)])
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["name"]
