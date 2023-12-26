import requests

#django import
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib import messages
#my project files
from .registration_form import UserRegistrationForm
from .serializers import UserRegistrationSerializer, TokenObtainPairSerializer,UserListSerializer,UserSerializer
from .models import User
#rest framework
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics



#Page registration form
def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            email_to_verify = form.cleaned_data['email']#email will be sent to hunter.io for validation
            hunter_api_key = '5daa2ca116eebcb451f0736dc888126983c3f97d'#my hunter.io api key
            hunter_url = f'https://api.hunter.io/v2/email-verifier?email={email_to_verify}&api_key={hunter_api_key}'  # endpoint API for verification

            response = requests.get(hunter_url)
            if response.status_code == 200:
                verification_data = response.json()

                # Check if email verification status is valid (deliverable)
                if verification_data['data']['result'] == 'deliverable':
                    user = form.save(commit=False)
                    user.set_password(form.cleaned_data['password'])
                    user.save()
                    messages.success(request, 'Account created successfully. Please log in.')
                    return redirect('login')
                else:
                    # If the email is not deliverable, show an error message
                    form.add_error('email', 'The provided email is not valid.')
            else:
                # Handle API request failure
                messages.error(request, 'Failed to verify the email. Please try again later.')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})


#login view
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username') #use email for login
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a specific page after login recipe_list.html
                return redirect('recipe_list')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})



#FRAMEWORK register form
class UserRegistrationAPIView(APIView):
    authentication_classes = []  # Override authentication classes for this view
    permission_classes = [AllowAny]  # Allow unauthenticated access

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Obtain Token for register users
class TokenObtainPairAPIView(APIView):
    authentication_classes = []  # Override authentication classes for this view
    permission_classes = [AllowAny]  # Allow unauthenticated access

    def post(self, request):
        serializer = TokenObtainPairSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)

#Login with Obtain Token
class UserLoginAPIView(APIView):
    authentication_classes = [JWTAuthentication]  # Use JWT authentication for this view
    permission_classes = [IsAuthenticated]  # Require authenticated access

    def post(self, request):
        return Response({"message": "User successfully authenticated."}, status=status.HTTP_200_OK)

#When user is login use Obtain Token to se users-list
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    permission_classes = [IsAuthenticated]

#When user is login use Obtain Token to se user by id, use <int:id>
class UserDetailByIDView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'