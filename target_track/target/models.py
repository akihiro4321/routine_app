from django.db import models

# Create your models here.
from django.utils import timezone


class Goal(models.Model):
    goal = models.CharField(max_length=30)
    regist_date = models.DateTimeField(default=timezone.datetime.today())

    def __str__(self):
        return self.goal