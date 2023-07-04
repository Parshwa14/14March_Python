from django.db import models
from django.utils.timezone import timezone

# Create your models here.
class User(models.Model):
    email = models.EmailField(unique=True,max_length=30)
    password = models.CharField(max_length=30)
    role = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) :
        return self.email    
    

class Teacher(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30) 
    date_of_birth =  models.DateTimeField(null=True)   
    date_of_joining =  models.DateTimeField(null=True)
    pic = models.FileField(upload_to="media/images",default="media/images/user.png")
    
class Student(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    date_of_birth =  models.DateTimeField(null=True)   
    date_of_joining =  models.DateTimeField(null=True)
    address = models.TextField(default="my address")
    pic = models.FileField(upload_to="media/images",default="media/images/user.png")
    
class Events(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    event_name = models.CharField(max_length=50, default="This is event")
    pic = models.FileField(upload_to="media/images",default="media/images/ds.png")
    
class Clubs(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    club_name = models.CharField(max_length=30)
    club_activity = models.TextField()
    club_pic = models.FileField(upload_to="media/images",default="media/images/ds.png")
    
class Library(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    book_name=models.CharField(max_length=50)
    author = models.CharField(max_length=50)