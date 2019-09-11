from django.urls import path
from todos import views
from decouple import config

app_name = 'todos'

urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create, name="create"),
    path('update/<int:pk>/', views.update, name="update"),
    path('delete/<int:pk>/', views.delete, name="delete"),
]