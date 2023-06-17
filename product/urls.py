from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.ProductRegister.as_view()),
    path('delete_product/<int:pk>/', views.delete_product, name="delete_product"),
    path('<int:pk>/', views.ProductDetail.as_view()),
    path('', views.ProductList.as_view()),
    path('search/', views.search, name='search'),
    #path('category/<str:slug>/', views.categories_page),
]