from django.db import models

from django.urls import reverse

class PartyManager(models.Manager):
    def search(self, query):
        return self.get_queryset().filter(models.Q(leadership__name__icontains=query) |
            models.Q(name__icontains=query) |
            models.Q(initials__icontains=query) |
            models.Q(number__iexact=query) |
            models.Q(union__icontains=query))
        

class Party(models.Model):
    name = models.CharField(max_length=350)
    initials = models.CharField(max_length=25)
    number = models.IntegerField()
    union = models.CharField(max_length=350, blank=True, null=True)
    leadership = models.ForeignKey('leadership.Leadership', on_delete=models.SET_NULL, null=True, blank=True)

    objects = PartyManager()

    def get_absolute_url(self):
        return reverse('party:partido', args=[str(self.id)])
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["name"]