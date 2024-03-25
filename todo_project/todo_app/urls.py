from django.urls import path
from . import views

urlpatterns = [
    path('addTask/', views.add_task, name='add_task'),
    path('mark_done/<int:pk>/', views.mark_done, name='mark_done'),
    path('mark_undone/<int:pk>/', views.mark_undone, name='mark_undone'),
    path('edit_task/<int:pk>/', views.edit_task, name='edit_task'),
    path('delete_task/<int:pk>/', views.delete_task, name='delete_task'),
]
