from django.urls import path
from .views import FollowingCreate

urlpatterns = [
    path("books/<int:book_id>/following/", FollowingCreate.as_view()),
]
