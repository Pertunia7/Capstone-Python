
from django.urls import path
from .views import showarticle, show_topics,send_input_data

app_name = 'article'

urlpatterns = [
    path('',showarticle),
    path('topics',show_topics),
    path('input',send_input_data),
 
]
