from django.db import models

# Create your models here.
class Product(models.Model):
    p_name=models.CharField(max_length=100)
    p_image=models.URLField()
    p_desc=models.TextField()
    p_category=models.CharField()
    p_price=models.FloatField()