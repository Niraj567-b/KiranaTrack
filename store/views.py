from django.shortcuts import render

def home (request):
    return render(request,'home.html')


def customer (request):
    return render(request,'customer.html')


def staff (request):
    return render(request,'staff.html')
