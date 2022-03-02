from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="list"),
    # 'name' is called by html a tag 
    path('update_task/<str:pk>/', views.updateTask, name="update_task"),
]