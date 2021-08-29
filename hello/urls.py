from django.urls import path

# Dot(.) means the current directory
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("<str:name>", views.greet, name="greet")
]