from . import views
from django.urls import path

urlpatterns = [
    path("", views.chat_template, name="chat"),
    path("chat/", views.chat, name="chat-response"),
]
