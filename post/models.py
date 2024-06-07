from django.db import models
from categories.models import category_model
from django.contrib.auth.models import User

# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    categorys = models.ManyToManyField(category_model)
    authors = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    