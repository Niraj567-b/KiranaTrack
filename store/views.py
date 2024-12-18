from django.shortcuts import render
from .models import Customer

def home (request):
    return render(request,'home.html')


def customer (request):

    customers = Customer.objects.all()

    return render(request,'customer.html',{'customers': customers})


def staff (request):
    return render(request,'staff.html')
