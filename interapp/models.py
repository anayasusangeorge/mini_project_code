from datetime import datetime


from django.db import models



# Create your models here.
# class register(models.Model):
#     gender_choices = (('Male','Male'),('Female','Female'),('Others','Others'))
#     firstname = models.CharField(max_length=50)
#     lname = models.CharField(max_length=50)
#     address = models.CharField(max_length=50)
#     pincode = models.IntegerField()
#     gender = models.CharField(max_length=50,choices=gender_choices,default='None')
#     DOB= models.DateField(default='1997-01-01')
#     phonenumber = models.CharField(max_length=10)
#     state = models.CharField(max_length=50)
#     city = models.CharField(max_length=50)
#     email = models.CharField(max_length=50, unique=True)
#     password = models.CharField(max_length=50)
#     status = models.CharField(max_length=50)
#
#     def __str__(self):
#         return self.firstname
# class login(models.Model):
#     email=models.CharField(max_length=50,unique=True,primary_key=True)
#     password = models.CharField(max_length=50)
from django.shortcuts import render


class user_reg(models.Model):
    gender_choices = (('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others'))
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    pincode = models.IntegerField()
    gender = models.CharField(max_length=20,choices=gender_choices,default='None')
    dob= models.DateField(auto_now=False, auto_now_add=False)
    phonenumber = models.CharField(max_length=10)
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.email

class user_course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=50)
    image=models.ImageField(upload_to='pics')
    desc=models.TextField()
    # price = models.CharField(max_length=10,default=0)
    def __str__(self):
        return self.course_name

class user_logins(models.Model):
    email = models.EmailField(max_length=100,primary_key=True, unique=True)
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.email

class duration(models.Model):
    week=models.CharField(max_length=20)
    def __str__(self):
        return self.week





class course_detail(models.Model):
    course_name = models.ForeignKey(user_course,on_delete=models.CASCADE)
    # title=models.CharField(max_length=10,default=0)
    video=models.FileField(upload_to='video')
    desc=models.TextField()
    course_week=models.ForeignKey(duration,on_delete=models.CASCADE)
    price = models.CharField(max_length=10,default=0)
    mentor=models.CharField(max_length=60)
    outcomes=models.TextField()
    assignment=models.TextField(default=0)
    # def __str__(self):
    #     return self.title



