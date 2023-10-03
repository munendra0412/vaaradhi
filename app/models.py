from django.db import models

# Create your models here.

class Categories(models.Model):
    category_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/profile_pic')
    seq = models.IntegerField

    def __str__(self):
        return self.name
