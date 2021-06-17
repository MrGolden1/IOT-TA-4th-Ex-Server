from django.urls import path
from .views import register,get_expression,submit_solution

urlpatterns = [
    path('register',register,name='register'),
    path('get_expression',get_expression,name='get_expression'),
    path('submit_solution',submit_solution,name='submit_solution'),
]