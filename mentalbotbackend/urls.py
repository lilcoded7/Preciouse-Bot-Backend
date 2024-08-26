from django.urls import path
from .views import chat_view, index

urlpatterns = [
    path('chat/', chat_view, name='chat'),
    path('', index)
    # other paths
]
