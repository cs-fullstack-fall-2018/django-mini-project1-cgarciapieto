from django.db import models



class Timeapp(models.Model):
    name = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    hours = models.IntegerField()
    date_worked = models.DateField()
    pub_date = models.DateTimeField('date published')

def __str__(self):
    return self.name