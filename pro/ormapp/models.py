from django.db import models
from django.contrib import admin

class Movie(models.Model):
    Moviename = models.CharField(max_length=200)
    Director = models.CharField(max_length=100)
    Genre = models.CharField(max_length=100)
    Release_date = models.DateField()
    Duration_minutes = models.PositiveIntegerField()
    Rating = models.DecimalField(max_digits=3, decimal_places=1) 

class MovieAdmin(admin.ModelAdmin):
    list_display=('Moviename','Director','Genre','Release_date','Duration_minutes','Rating')
