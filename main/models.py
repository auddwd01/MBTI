from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField, IntegerField

# Create your models here.
class Developer(models.Model):
    name = models.CharField(max_length=50)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Question(models.Model):
    number = IntegerField(unique=True)
    content = CharField(max_length=100)
    def __str__(self):
        return f'{self.number}. {self.content}'

class Choice(models.Model):
    content = CharField(max_length=100)
    question = models.ForeignKey(to='main.Question',on_delete=models.CASCADE)
    developer= models.ForeignKey(to='main.Developer',on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.content