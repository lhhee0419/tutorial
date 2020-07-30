from django.urls import path,include
from secondapp import views

urlpatterns = [
    path('show/', views.show),
]
