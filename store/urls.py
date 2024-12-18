from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name = "home"),
    path("customer/", views.customer , name = "customer"),
    path("staff/", views.staff , name = "staff")
]