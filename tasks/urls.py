from django.urls import path
from .views import homeless 


urlpatterns = [
    path('task/',homeless,name='task'),
]