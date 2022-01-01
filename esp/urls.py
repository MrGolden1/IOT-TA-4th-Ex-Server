from django.urls import path
from .views import register,get_expression,submit_solution,sentence_get,sentence_submit

urlpatterns = [
    path('register',register,name='register'),
    path('get_expression',get_expression,name='get_expression'),
    path('submit_solution',submit_solution,name='submit_solution'),
    path('sentence_get',sentence_get,name='sentence_get'),
    path('sentence_submit',sentence_submit,name='sentence_submit'),
]