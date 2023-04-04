from django.db import models
from datetime import timedelta
from django.utils import timezone

class Loan(models.Model):
    date_collected = models.DateTimeField(auto_now_add=True)
    date_limit_return = models.DateTimeField(null=True, blank=True)
    date_returned = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="loans_books"
    )
    copy = models.ForeignKey(
        "copies.Copy", on_delete=models.CASCADE, related_name="loans_books"
    )

    def save(self, *args, **kwargs):
        if not self.pk:
            self.date_limit_return = timezone.now() + timedelta(days=7)
        super().save(*args, **kwargs)
