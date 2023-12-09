
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', views.todo,name='todo'),
    path('todo/', include('tasks.urls') ),
]
