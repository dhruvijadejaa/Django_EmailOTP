from django.shortcuts import render
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import *
from .email import *

class RegisterAPI(APIView):

    def post (self, request):
        try:
            data = request.data  
            serializer = UserSerializer(data = data)
            if serializer.is_valid():
                """ serializer.save() """
                """ send_otp_via_email(serializer.data['email']) """     
                email = serializer.data['email']
                otp = serializer.otp['otp']

                user = 
                return Response({
                    'status': 200,
                    'message':
                    'registration successfully check email',
                    'data': serializer.data
                })
            return Response({
                'status': 400,
                'message': 'something went wrong',
                'data' : serializer.errors
            })
        except Exception as e:
            return Response({
                "status": 500,
                "message": str(e)
            })
        
class VerifyOTP(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = VarifyAccountSeriazlier(data = data)
        except Exception as e:
            return Response(e)