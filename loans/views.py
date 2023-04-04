from .models import Loan
from copies.models import Copy
from .serializers import LoansBooksSerializer
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from rest_framework.response import Response
from rest_framework import status
from datetime import timedelta, date
from django.utils import timezone

class LoanCreateView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = LoansBooksSerializer

    def create(self, serializer, isbn):
        day_week = date.today().weekday()

        if day_week > 4:
            return Response(
                {"message": "Biblioteka not working on weekends"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if self.request.user.is_blocked == True:
            if self.request.user.blocked_until < timezone.now():
                self.request.user.is_blocked = False
                self.request.user.blocked_until = None
            else:
                return Response(
                    {"message": "The user is currently blocked."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        try:
            copy = Copy.objects.get(isbn=isbn)
        except:
            return Response(
                {"message": "Copy does not exist."}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = LoansBooksSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)

        if copy.is_loaned == True:
            return Response(
                {"isbn": "This copy is not available."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        copy.is_loaned = True
        copy.save()

        serializer.save(user=self.request.user, copy=copy)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoanReturnView(UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Loan.objects.all()
    serializer_class = LoansBooksSerializer
    lookup_url_kwarg = "isbn"

    def patch(self, request, isbn):
        try:
            copy = Copy.objects.get(isbn=isbn)
        except:
            return Response(
                {"message": "Copy does not exist."}, status=status.HTTP_404_NOT_FOUND
            )

        try:
            loan = Loan.objects.get(
                user=self.request.user, copy=copy, date_returned=None
            )
        except:
            return Response(
                {"message": "You don't have any use with this copy."},
                status=status.HTTP_404_NOT_FOUND,
            )

        loan.date_returned = timezone.now()
        copy.is_loaned = False

        if loan.date_returned > loan.date_limit_return:
            user = self.request.user
            user.is_blocked = True
            if (loan.date_returned - loan.date_limit_return) > timedelta(day=1):
                violated_days = loan.date_returned - loan.date_limit_return
                punishment = (violated_days * 2) + 7
                user.blocked_until = timedelta(days=punishment)
            else:
                user.blocked_until = timezone.now() + timedelta(days=7)
            user.save()

        loan.save()
        copy.save()

        return Response({"message": "Book returned."}, status=status.HTTP_200_OK)
