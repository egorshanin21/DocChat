from django.urls import path
from . import views


urlpatterns = [
    path("signup/", views.register, name="register"),
    path('login/', views.custom_login, name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path("password_change/", views.password_change, name="password_change"),
    path("password_reset/", views.password_reset_request, name="password_reset"),
    path('password_reset/<uidb64>/<token>/', views.passwordResetConfirm, name='password_reset_confirm'),
    path('delete_user/<int:pk>', views.DeleteUser.as_view(), name='delete_user')
]