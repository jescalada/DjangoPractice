from django.urls import path
from . import views  # from the same folder, import the views.py file

urlpatterns = [
    path("<month>", views.monthly_challenge)
]