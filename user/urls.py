from django.urls import path
from .views import register_user,user_login,RegisterView

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', user_login, name='login'),
    path('api/register/', RegisterView.as_view(), name='register'),
]
