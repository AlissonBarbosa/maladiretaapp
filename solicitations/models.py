from django.db import models
from django.urls import reverse

class SolicitationManager(models.Manager):
    def search(self, query):
        return self.get_queryset(models.Q(description__icontais=query) | 
            models.Q(created__icontains=query) | 
            models.Q(note__icontains=query) | 
            models.Q(description__iexact=query) | 
            models.Q(situation__iexact=query) |
            models.Q(indication__iexact=query) |
            models.Q(customer__name__icontains=query))

class Solicitation(models.Model):
    created = models.DateField(auto_now_add=True)
    description = models.TextField()
    indication = models.CharField(max_length=250, blank=True, null=True)
    value = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    situation = models.CharField(max_length=9, default="ABERTO")
    note = models.TextField(blank=True, null=True)
    customer = models.ForeignKey('customers.Customer', on_delete=models.CASCADE)

    objects = SolicitationManager()

    def get_absolute_url(self):
        return reverse('solicitations:pleito', args=[str(self.id)])
    
    def __str__(self):
        return self.description
    
    class Meta:
        ordering = ["created"]