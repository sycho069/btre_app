from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
from contacts.models import Contact

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.warning(request, 'Username is taken. Try different!')
                return redirect('register_page')
            else:
                if User.objects.filter(email=email).exists():
                    messages.warning(request, 'Email is already taken.')
                    return redirect('register_page')
                else:
                    user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, password=password, email=email)
                    user.save()
                    messages.success(request, f'Account created successfully! Login to continue')
                    return redirect('login_page')
        else:
            messages.warning(request, f'Password is not matching.')
            return redirect('register_page')

    else:    
        return render(request, 'accounts/register.html', {})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, f'Welcome to the dashboard {username}!')
            return redirect('dashboard_page')
    else:    
        return render(request, 'accounts/login.html', {})

def logout_view(request):
    auth.logout(request)
    return redirect('login_page')

def dashboard(request):
    contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)

    context = {
        'contacts':contacts,
    }
    return render(request, 'accounts/dashboard.html', context)
