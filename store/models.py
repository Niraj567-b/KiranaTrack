from django.db import models

class Customer(models.Model):

    name = models.CharField(max_length = 100, blank = False, null = False)
    phone = models.CharField(max_length = 10, blank = False, null = False)
    AadharNo = models.CharField(max_length = 10, blank = False, null = False, unique = True)
    address = models.TextField(blank = False, null = False)

    def __str__(self):
        return self.name
    
class Staff(models.Model):

    staffName = models.CharField(max_length = 100, blank = False, null = False)
    phone = models.CharField(max_length = 10, blank = False, null = False)
    address = models.TextField(blank = False, null = False)

    def __str__(self):
        return self.staffName


