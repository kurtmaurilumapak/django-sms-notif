from django.db import models
from decouple import config
from twilio.rest import Client

# Create your models here.
class Score(models.Model):
    result = models.PositiveSmallIntegerField()

    def __str__(self):
        return str(self.result)

    def save(self, *args, **kwargs):

        twilio_acc_sid = config('TWILIO_ACCOUNT_SID')
        twilio_auth_token = config('TWILIO_AUTH_TOKEN')
        twilio_phone_number = config('TWILIO_PHONE_NUMBER')

        client = Client(twilio_acc_sid, twilio_auth_token)
        if self.result < 70:
            message = client.messages.create(
                body=f'Hi there, I am sorry to say but your score is bad - {self.result}.',
                from_=twilio_phone_number,
                to='+639760009509'
            )

            print(f"Message for low score sent with SID: {message.sid}")
        return super().save(*args, **kwargs)
