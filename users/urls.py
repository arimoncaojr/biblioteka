from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import UserCreate, UserLoans, IsUserBlocked

urlpatterns = [
    path("users/", UserCreate.as_view()),
    path("users/login/", TokenObtainPairView.as_view()),
    path("users/<int:user_id>/loans/", UserLoans.as_view()),
    path("users/<int:user_id>/status/", IsUserBlocked.as_view()),
]
