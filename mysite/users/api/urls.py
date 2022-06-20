from django.urls import path
from .views import register_view, UserProfileUpdateAPIView, UserProfileDetailAPIView
from rest_framework.authtoken.views import obtain_auth_token


app_name = 'users'

urlpatterns = [
    path('register', register_view, name="register-view"),
    path('login', obtain_auth_token, name="login-view"),
    path('profile/<int:pk>', UserProfileDetailAPIView.as_view(), name="profile-view"),
    path('profile/update/<int:pk>', UserProfileUpdateAPIView.as_view(), name="register-view"),
]