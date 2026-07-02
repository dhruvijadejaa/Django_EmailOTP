from django.core.mail import send_mail
import random 
from django.conf import settings
from rest_framework.response import Response
from .models import User

def send_otp_via_email(email):
    subject = "your account verification email"
    otp = random.randint(1000, 9999)
    message = f"your otp is {otp}"
    email_from = settings.EMAIL_HOST_USER
    """ searches user by email """
    user_obj = User.objects.filter(email=email).first()
    if not user_obj:
        return Response({"error": "User not found"})
    user_obj.otp = otp
    user_obj.save()
    send_mail(subject, message, email_from, [email])

    """  
    user_obj = User.objects.get(email= email)
    Fetch users from database
    Finds user in database using email
    Returns a single user object
    """

    """ sending an OTP in email and storing the OTP in the database. """

