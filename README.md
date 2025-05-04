# Ex02 Django ORM Web Application
## Date: 04/05/2025

## AIM
To develop a Django application to store and retrieve data from a Movies Database using Object Relational Mapping(ORM).

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM

```
Name : A Praneya
Register No: 212224110045
```

models.py

```
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
```
admin.py

```
from django.contrib import admin
from .models import Movie,MovieAdmin
admin.site.register(Movie,MovieAdmin)
```

## OUTPUT

![alt text](<Screenshot (1).png>)


## RESULT
Thus the program for creating movies database using ORM hass been executed successfully
