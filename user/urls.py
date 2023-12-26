from django.urls import path
from .views import register_user,user_login,UserRegistrationAPIView, TokenObtainPairAPIView,UserLoginAPIView,UserListView,UserDetailByIDView


urlpatterns = [
    #page urls
    path('register/', register_user, name='register'),
    path('', user_login, name='login'),

    #api end points
    path('api/register/', UserRegistrationAPIView.as_view(), name='user-registration'),
    path('api/token/', TokenObtainPairAPIView.as_view(), name='token-obtain'),
    path('api/login/', UserLoginAPIView.as_view(), name='token-login'),
    path('api/users-list/', UserListView.as_view(), name='user-list'),
    path('api/user-id/<int:id>/', UserDetailByIDView.as_view(), name='user-id'),
]
