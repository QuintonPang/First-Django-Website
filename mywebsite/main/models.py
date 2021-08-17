from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ToDoList(models.Model):

    #related_name is used to switch User.todolist_set(default) to User.todolist 

    #null = True means it changes empty string to NULL

    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="todolist",null=True)

    name = models.CharField(max_length=200)


    def __str__(self):

        return self.name

#name is changed to lowercase in default, " "_set is default in ToDoList

class Item(models.Model):

    todolist = models.ForeignKey(ToDoList,on_delete=models.CASCADE)
    text = models.CharField(max_length=300)

    completion = models.BooleanField()


    def __str__(self):


        return self.text
