from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Administrator(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    def __str__(self):
        return self.username

class Doctor(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class Patient(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    def __str__(self):
        return self.username

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    confirmed =models.BooleanField(default=False)
    date_time = models.DateTimeField()
class Schedule(models.Model):
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    date = models.DateTimeField()
    booked = models.BooleanField(default=False)
    
class SystemUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    is_doctor = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
