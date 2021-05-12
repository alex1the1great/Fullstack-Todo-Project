from django.urls import path

from . import views

urlpatterns = [
    path('<int:pk>/', views.DetailTodo.as_view()),
    path('todo/add/', views.AddTodo.as_view()),
    path('todo/update/<int:pk>/', views.UpdateTodo.as_view()),
    path('todo/delete/<int:pk>/', views.DeleteTodo.as_view()),
    path('', views.ListTodo.as_view())
]
