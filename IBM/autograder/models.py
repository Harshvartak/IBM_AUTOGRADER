from django.db import models

# Create your models here.

class Essay(models.Model):
    text=models.TextField(null=True)
    score=models.FloatField(null=True)

    def __str__(self):
        return self.text