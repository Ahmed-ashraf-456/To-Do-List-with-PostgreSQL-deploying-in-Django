
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index , name= 'index'),
    path('insert_todo/',views.insert_todo_item,name='insert_todo_item'),
    path('delete_todo/<int:todo_id>/',views.delete_todo_item,name='delete_todo_item'),
]