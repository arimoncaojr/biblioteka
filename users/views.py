from users.serializers import UserSerializer
from rest_framework.generics import ListAPIView, CreateAPIView
from .serializers import UserLoansSerializer, IsUserBlockedSerializer
from loans.models import Loan
from .models import User
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsAccountOwner
from django.shortcuts import get_object_or_404

class UserCreate(CreateAPIView):
    serializer_class = UserSerializer


class UserLoans(ListAPIView):
    serializer_class = UserLoansSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAccountOwner]

    def get_queryset(self):
        user_id = self.kwargs["user_id"]
        self.check_object_permissions(self.request, user_id)

        user = get_object_or_404(User, id=user_id)
        return Loan.objects.filter(user=user)


class IsUserBlocked(ListAPIView):
    serializer_class = IsUserBlockedSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    pagination_class = None

    def get_queryset(self):
        user_id = self.kwargs["user_id"]
        user = get_object_or_404(User, id=user_id)
        return User.objects.filter(id=user_id)
