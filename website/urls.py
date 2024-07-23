from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("Haider", views.haider, name="haider"),
    path("<str:name>", views.greet, name="greet")
]