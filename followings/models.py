from django.db import models

class Following(models.Model):
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="following"
    )
    book = models.ForeignKey(
        "books.Book", on_delete=models.CASCADE, related_name="following"
    )
    last_email_sent = models.DateTimeField(null=True, blank=True)
