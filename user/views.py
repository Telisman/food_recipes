from django.shortcuts import render, redirect
from .registration_form import UserRegistrationForm

def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('')  # Redirect to login page or any other page
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

