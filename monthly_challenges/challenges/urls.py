from django.urls import path
from . import views  # from the same folder, import the views.py file

urlpatterns = [
    path("", views.index),
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge, name='month-challenge'),
    path("unicorns/", views.display_unicorns)
]
