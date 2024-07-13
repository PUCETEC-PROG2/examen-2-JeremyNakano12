from django.db import models

# Create your models here.

class Movies (models.Model):
    title = models.CharField(max_length=30, null=False)
    genre = models.CharField(max_length=15, null=False)
    director = models.CharField(max_length=30, null=False)
    release_year = models.CharField(max_length=12, null=False)
    sinopsis = models.TextField(max_length=300, null=False)
    
    def __str__(self) -> str:
        return self.title