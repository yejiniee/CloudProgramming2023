from django.urls import path
from order import views

urlpatterns = [
    path('', views.OrderList.as_view()),
    path('create/', views.OrderCreate.as_view()),
]