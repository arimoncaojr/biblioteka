from django.urls import path
from .views import LoanCreateView, LoanReturnView

urlpatterns = [
    path("copies/<int:isbn>/loans/", LoanCreateView.as_view()),
    path("copies/<int:isbn>/loans/return/", LoanReturnView.as_view()),
]
