from django.urls import path

# Dot(.) means the current directory
from . import views

app_name = "tasks"
urlpatterns = [
    path("", views.index, name="index"),
    path("new", views.new, name="new")
]