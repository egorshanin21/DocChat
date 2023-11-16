from django.urls import path
from .views import (homepage, upload_file, get_chats,
                    get_messages, send_message, create_chat, delete_document, delete_chat)

urlpatterns = [
    path('', homepage, name='homepage'),
    path('upload/', upload_file, name='upload_file'),
    path('chat/', create_chat, name='create_chat'),
    path('get_chats/', get_chats, name='get_chats'),
    path('send_message/<int:chat_id>/', send_message, name='send_message_id'),
    path('send_message/', send_message, name='send_message'),
    path('delete_document/<int:doc_id>/', delete_document, name='delete_document'),
    path('delete_chat/<int:chat_id>/', delete_chat, name='delete_chat'),
]
