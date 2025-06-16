from django.shortcuts import render
from django.contrib.auth import authenticate,login
from users.forms import UserLoginForm, UserRegistrationForm
from users.models import User
from django.shortcuts import redirect

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        valid = form.is_valid()
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('') 
    else:
        form = UserRegistrationForm()
    return render(request, 'signup.html', {'form': form})


def signin(request):
    if request.method == 'POST':
        data = {'email': request.POST['email'], 'password': request.POST['password']}
        form = UserLoginForm(data=data)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('upload_file')  
            else:
                try:
                    existing_user = User.objects.get(email=email)
                except User.DoesNotExist:
                    existing_user = None

                if existing_user is None:
                    error_message = "Email is incorrect."
                else:
                    error_message = "Password is incorrect."
        else:
            error_message = "Invalid form data. Please check your input."
    else:
        form = UserLoginForm()
        error_message = None

    return render(request, 'login.html', {'form': form, 'error_message': error_message})