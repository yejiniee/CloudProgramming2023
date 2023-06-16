from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.RegisterView.as_view()),
    #path('signup/', views.register),
    path('login/', views.LoginView.as_view()),
    ]