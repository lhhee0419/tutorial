from django.urls import path,include
from . import views

urlpatterns = [
    path('show/', views.hospital),
]
