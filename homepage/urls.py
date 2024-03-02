from django.urls import path
from . import views

urlpatterns = [
    path('homepage/', views.Product_view, name='homepage'),
    path('homepage/details/<int:id>', views.details, name='details'),
]
