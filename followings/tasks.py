from apscheduler.schedulers.background import BackgroundScheduler
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from .models import Following
from django_apscheduler.jobstores import DjangoJobStore
from pytz import utc
from django.utils import timezone


def check_availability_and_send_emails():
    followings = Following.objects.all()

    for following in followings:
        book = following.book
        copies = book.copies.all()
        all_loaned = all(copy.is_loaned for copy in copies)

        if all_loaned and following.last_email_sent is None:
            subject = f"Disponibilidade do livro {book.title}"
            message_template = "email/unavailable.txt"
            message = render_to_string(message_template, {"book": book})
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [following.user.email]
            send_mail(subject, message, from_email, recipient_list)
            following.last_email_sent = timezone.now()
            following.save()

        elif not all_loaned and following.last_email_sent is not None:
            subject = f"Disponibilidade do livro {book.title}"
            message_template = "email/available.txt"
            message = render_to_string(message_template, {"book": book})
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [following.user.email]
            send_mail(subject, message, from_email, recipient_list)
            following.last_email_sent = None
            following.save()


scheduler = BackgroundScheduler(timezone=utc)
scheduler.add_jobstore(DjangoJobStore(), "default")

scheduler.add_job(
    check_availability_and_send_emails,
    trigger="interval",
    minutes=1,
    id="check_availability_and_send_emails",
    replace_existing=True,
)

scheduler.start()
