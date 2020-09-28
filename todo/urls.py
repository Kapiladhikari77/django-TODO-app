from django.urls import path
from .views import homepage,edit,deleteTask
urlpatterns = [
    path('',homepage,name='home'),
    path('edit/<str:pk>',edit,name='edit'),
    path('delete/<str:pk>',deleteTask,name='delete'),

]
