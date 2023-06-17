from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view()),
    path('create_post/', views.PostCreate.as_view()),
    path('update_post/<int:pk>/', views.PostUpdate.as_view()),
    path('delete_post/<int:pk>/', views.delete_post, name="delete_post"),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('category/<str:slug>/', views.categories_page),
    path('tag/<str:slug>/', views.tag_page),
    #path('search/', views.search, name='search'),
    path('<int:pk>/add_comment/', views.add_comment),

    #path('', views.index),

]
