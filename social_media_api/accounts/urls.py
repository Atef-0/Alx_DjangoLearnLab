from django.urls import path, include
from .views import UserRegisterationView, CustomAuthToken, UserProfileView

urlpatterns = [
    path('register/', UserRegisterationView.as_view(), name='register'),
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
]