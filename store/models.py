from django.db import models

GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

class Customer(models.Model):

    name = models.CharField(max_length = 100, blank = False, null = False)
    phone = models.CharField(max_length = 10, blank = False, null = False)
    AadharNo = models.CharField(max_length = 12, blank = False, null = False, unique = True)
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES,default='M')
    address = models.TextField(blank = False, null = False)

    def __str__(self):
        return self.name
    
class Staff(models.Model):

    staffName = models.CharField(max_length = 100, blank = False, null = False)
    phone = models.CharField(max_length = 10, blank = False, null = False)
    address = models.TextField(blank = False, null = False)
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES,default='M')

    def __str__(self):
        return self.staffName


