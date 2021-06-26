from django.db import models

# Create your models here.

class Essay(models.Model):
    text=models.TextField(null=True)
    score=models.CharField(max_length=64,null=True)

    def __str__(self):
        return self.text