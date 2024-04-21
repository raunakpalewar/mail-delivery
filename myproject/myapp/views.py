from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
from django.http import HttpResponseRedirect
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import *
from .models import *
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import login, logout
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.conf import settings
from django.core.mail import send_mail
from datetime import timedelta
from django.db.models import Q
import re
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .models import PersonalDetails, Education, WorkExperience, Skill, Project, Certificate, Achievement
from .serializers import PersonalDetailsSerializer, EducationSerializer, WorkExperienceSerializer, SkillSerializer, ProjectSerializer, CertificateSerializer, AchievementSerializer
from .models import User
from django.http import HttpResponse
from django.template.loader import get_template
from .models import PersonalDetails, Education, WorkExperience, Skill, Project, Certificate, Achievement
from weasyprint import HTML
from django.utils.safestring import mark_safe
import random
import random,string


def send_updated_resume_email(email):
    subject = "Your Updated Resume"
    message = "Here is your updated resume"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)



def password_validate(password):
    if not re.match(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*(){}[\]:;,<>\'\"~])[A-Za-z\d!@#$%^&*(){}[\]:;,<>\'\"~]{8,16}$', password):
        raise ValueError("Password must be 8 to 16 characters long with one uppercase, one lowercase, a number, and a special character.")


def email_validate(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not email or not re.match(email_regex, email):
        raise ValueError("Invalid email format")




class userregistratin(APIView):
    permission_classes = [AllowAny]
    @swagger_auto_schema(
        operation_description="This is for Customer Registration",
        operation_summary="Customer can Register using this API",
        tags=['Authentication'],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'email': openapi.Schema(type=openapi.TYPE_STRING),
                'password': openapi.Schema(type=openapi.TYPE_STRING),
            },
            required=['email', 'password']
        ),
    )
    def post(self,request):
        try:
            email = request.data.get('email')
            password = request.data.get('password')

            if not email or not password:
                return Response({'status': status.HTTP_400_BAD_REQUEST, 'message': "Email or Password not provided"}, status=status.HTTP_400_BAD_REQUEST)

            email_validate(email)
            password_validate(password)
            user_password = make_password(password)

            date = timezone.now()
            user = User.objects.create(email=email,date_joined=date,password=user_password)
            user.save()

            return Response({'message': "User Registered Successfully"}, status=status.HTTP_201_CREATED)

        except ValueError as e:
            return Response({'status': status.HTTP_400_BAD_REQUEST, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({"status": status.HTTP_500_INTERNAL_SERVER_ERROR, 'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CreateDraft(APIView):
    pass

class ViewDraft(APIView):
    pass

class EditDraft(APIView):
    pass

class DeleteDraft(APIView):
    pass

class ViewAllDraft(APIView):
    pass