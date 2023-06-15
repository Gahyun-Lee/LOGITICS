from django.urls import path
from . import views

urlpatterns = [
    path('', views.hubs, name='hubs'),
    path('<int:id>/', views.more, name='more'),
    path('<int:id>/delete/', views.delete, name='delete'),
]