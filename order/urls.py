from django.urls import path
from order import views

urlpatterns = [
    path('create/', views.OrderCreate.as_view()),
]