from django.db import models
from django.urls import reverse

class CandidateManager(models.Manager):
    def search(self, query):
        return self.get_queryset().filter(models.Q(party__name__icontains=query) |
            models.Q(position__position__icontains=query) |
            models.Q(name__icontains=query) |
            models.Q(number__iexact=query) |
            models.Q(union__icontains=query))

class Candidate(models.Model):
    name = models.CharField(max_length=250)
    number = models.IntegerField()
    union = models.CharField(max_length=350, blank=True, null=True)
    party = models.ForeignKey('parties.Party', on_delete=models.CASCADE)
    position = models.ForeignKey('positions.Position', on_delete=models.CASCADE)
    votes = models.IntegerField(blank=True, null=True)

    objects = CandidateManager()

    def get_absolute_url(self):
        return reverse('candidate:Candidate', args=[str(self.id)])
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["name"]