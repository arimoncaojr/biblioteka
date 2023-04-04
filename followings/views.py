from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404
from .models import Following
from copies.models import Copy
from books.models import Book
from .serializers import FollowingSerializer
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.generics import CreateAPIView
from rest_framework.views import status

class FollowingCreate(CreateAPIView):
    serializer_class = FollowingSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)

        if request.user.following.filter(book=book).exists():
            return Response(
                {"message": "Você já está seguindo este livro."}, status=status.HTTP_403_FORBIDDEN
            )

        following = Following(user=request.user, book=book)
        following.save()

        copies = Copy.objects.filter(book=book)

        all_loaned = all(copy.is_loaned for copy in copies)
        if all_loaned:
            subject = (
                f"O livro {book.title} está temporariamente indisponível na BiblioteKA"
            )
            message = (
                f"O livro {book.title} está temporariamente indisponível na BiblioteKA."
            )
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [request.user.email]
            send_mail(subject, message, from_email, recipient_list)
        else:
            subject = f"O livro {book.title} está disponível na BiblioteKA"
            message = f"O livro {book.title} está disponível na BiblioteKA."
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [request.user.email]
            send_mail(subject, message, from_email, recipient_list)

        following.save()

        return Response({"message": "Você agora está seguindo este livro."})
