from django.urls import path
from .views import (homepage, upload_file, get_chats,
                    get_messages, send_message, create_chat)

urlpatterns = [
    path('', homepage, name='homepage'),
    path('upload/', upload_file, name='upload_file'),
    path('chat/', create_chat, name='create_chat'),
    path('get_chats/', get_chats, name='get_chats'),
    path('send_message/<int:chat_id>/', send_message, name='send_message_id'),
    path('send_message/', send_message, name='send_message'),
]
