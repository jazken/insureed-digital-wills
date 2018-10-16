from django.db import models

class Will(models.Model):
    #Will Number
    willno = models.CharField(max_length=255)
    #Date and time created
    datesigned = models.DateTimeField()#(input_formats='%Y-%m-%d')
    #Signed
    timesubmit = models.DateTimeField()#(input_formats='%H:%M:%S')
    #Lawyer - User 2
    lawyer = models.IntegerField
    #Executor - User 
    executor = models.IntegerField