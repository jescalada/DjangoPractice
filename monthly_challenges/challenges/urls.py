from django.urls import path
from . import views  # from the same folder, import the views.py file

urlpatterns = [
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge)
]
