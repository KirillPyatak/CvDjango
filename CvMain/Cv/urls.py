from django.urls import path
from .views import Cv
urlpatterns = [
    path('', Cv),
]