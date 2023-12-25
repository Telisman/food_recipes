from django.shortcuts import render, redirect
from .registration_form import UserRegistrationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
import requests
from django.contrib import messages

def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            email_to_verify = form.cleaned_data['email']
            hunter_api_key = '5daa2ca116eebcb451f0736dc888126983c3f97d'
            hunter_url = f'https://api.hunter.io/v2/email-verifier?email={email_to_verify}&api_key={hunter_api_key}'

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


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a specific page after login
                return redirect('create_recipe')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})