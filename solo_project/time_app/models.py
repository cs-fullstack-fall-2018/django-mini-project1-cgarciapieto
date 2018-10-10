from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    Teacher = models.CharField(max_length=200)
    School = models.CharField(max_length=200)
    Subject = models.CharField(max_length=200)
    hours = models.IntegerField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

