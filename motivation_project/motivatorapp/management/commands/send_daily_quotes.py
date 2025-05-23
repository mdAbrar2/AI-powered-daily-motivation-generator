from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import get_user_model
from motivatorapp.views import fetch_quote

class Command(BaseCommand):
    help = 'Send daily motivational quotes to all users'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        users = User.objects.all()
        quote = fetch_quote()
        subject = "Your Daily Dose of Motivation 💪"
        message = f"Hello!\n\nHere's your motivational quote for today:\n\n{quote}\n\nHave a great day!"
        for user in users:
            if user.email:
                send_mail(
                    subject,
                    message,
                    settings.DEFAULT_FROM_EMAIL,
                    [user.email],
                    fail_silently=False,
                )
        self.stdout.write(self.style.SUCCESS('Sent daily quotes to all users.'))