from django.db import models
from datetime import datetime

# Create your models here.
class User (models.Model):
    username= models.CharField(max_length=100)
    password= models.TextField()
    email=models.TextField()
    position= models.CharField(max_length=100)

class ToDoList (models.Model):
    userID= models.ForeignKey(User, on_delete=models.CASCADE)
    toDoListName=  models.CharField(max_length=100)

class Task(models.Model):
    toDoListId= models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    taskName= models.CharField(max_length=100)
    status= models.CharField(max_length=100)
    startDate= models.DateTimeField()
    dueDate= models.DateTimeField()