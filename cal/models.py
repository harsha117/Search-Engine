from django.db import models

# Create your models here.


class Search(models.Model):
    search_str = models.CharField(max_length=100)
    des = models.TextField()
    img = models.ImageField(upload_to='pics')