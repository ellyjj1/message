from django.db import models

# Create your models here.

from django.contrib.auth.models import User 
from django.db import models

'''
from django.db.models import Q
from django.utils import timezone
from django.contrib.auth.models import User
'''
class ChatRoom(models.Model):  #creat a class called chatroom
    name = models.CharField(max_length=100)     # name of chatroom
    created = models.DateTimeField(auto_now_add=True)   # date of the chatroom created
    updated_at = models.DateTimeField(auto_now=True)    # date of the chatroom updated

def __str__(self): #object lable
    return self.name

class Message(models.Model):    #creat a class called   Message
    test = models.TextField()   
    chat_room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


def __str__(self):  #object lable
    return self.text + "-" + self.user.username

