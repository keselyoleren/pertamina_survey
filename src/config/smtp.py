
import requests

from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from decouple import config

class Smtp:
    def __init__(self, template=None, subject=None, reciept=None, context=None) -> None:
        self.key = config('MAILGUN_API_KEY')
        self.domain = config('MAILGUN_DOMAIN')
        self.sender = config('MAILGUN_FROM_EMAIL')
        self.template_name = template
        self.subject = subject
        self.recipient_email = reciept
        self.context = context

    def send_mail(self):
        email_content = render_to_string(self.template_name, self.context)
        email = EmailMessage(
            self.subject,
            email_content,
            self.sender,
            [self.recipient_email],
        )
        email.content_subtype = 'html'  # Set the email content type to HTML
        # Use Mailgun API to send the email
        response = requests.post(
            f"https://api.mailgun.net/v3/{self.domain}/messages",
            auth=("api", self.key),
            data={
                "from": f"no replay <mailgun@{self.domain}>",
                "to": self.recipient_email,
                "subject": self.subject,
                "html": email_content,
            }
        )
        return response

    def create_authorized_recipient(self):
        mailgun_url = f"https://api.mailgun.net/v3/{self.domain}/authorized_recipients"
        return requests.post(mailgun_url, auth=("api", self.key), data={"email": self.recipient_email})