from django.db import models

# Create your models here

class InputData(models.Model):
    field1 = models.CharField(max_length=100)
    field2 = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
