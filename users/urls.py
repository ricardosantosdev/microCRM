from django.urls import path
from .views import register_user, login_user, logout_user

urlpatterns = [
    path('login/', login_user, name="login_user"),
    path('logout_user/', logout_user, name="logout_user"),
    path('register/', register_user, name="register_user"),
]
