from django.db import models

# Create your models here.
class siteusers(models.Model):
    username = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    password = models.CharField(max_length=122)
    date = models.DateField() 

    def __str__(self):
        return self.username

class uploadData(models.Model):
    bp=models.CharField(max_length=5)
    sugar=models.CharField(max_length=5)
    chole=models.CharField(max_length=5)
    bmi=models.CharField(max_length=5)
    smoke=models.CharField(max_length=3)
    drink=models.CharField(max_length=3)