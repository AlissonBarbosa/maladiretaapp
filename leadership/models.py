from django.db import models

class LeadershipManager(models.Manager):
    def search(self, query):
        return self.get_queryset(models.Q(name__icontais=query) | 
            models.Q(nickname__icontains=query) | 
            models.Q(note__icontains=query) | 
            models.Q(rg__iexact=query) | 
            models.Q(cpf__iexact=query) |
            models.Q(position__position__icontains=query))

class Leadership(models.Model):
    name = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=25, blank=True, null=True)
    cellphone = models.CharField(max_length=25, blank=True, null=True)
    phone_home = models.CharField(max_length=25, blank=True, null=True)
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
    birth = models.DateField(blank=True, null=True)
    updated = models.DateField(auto_now_add=True)
    nickname = models.CharField(max_length=30, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    position = models.ForeignKey('positions.Position', on_delete=models.CASCADE, blank=True, null=True)
    #party

    objects = LeadershipManager()

    def get_absolute_url(self):
        return reverse('leadership:lideranca', args=[str(self.id)])
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["name"]