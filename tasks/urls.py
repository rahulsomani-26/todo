from django.urls import path,re_path
from .views import list_task,add_task,delete_task


urlpatterns = [
    path('listtask/',list_task,name='list_task'),
    path('addtask/',add_task,name='add_task'),
    path('deletetask/<int:task_id>',delete_task,name='delete_task'),
]