# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
import random
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

# verification email
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import  urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage

from .models import Account
from .forms import RegistrationForm



# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            email_prefix = email.split("@")[0]         # ================Extract email prefix

            last_three_digits = ''.join(random.sample(phone_number, 3))   # =========Randomly select three digits from the phone number

            username = f"{email_prefix}{last_three_digits}"  # ==========Combine email prefix and last three digits of phone number
            
            user = Account.objects.create_user(
                first_name=first_name, last_name=last_name,
                email=email, username=username, password=password
                )
            user.phone_number = phone_number
            user.save()
            
            
            # =========================USER ACTIVATION=================================================
            current_site = get_current_site(request)
            mail_subject = ' Please activate your account!'
            message = render_to_string('accounts/account_verification_email.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send() 
            
            #messages.success(request, ' Thank you for registering, Please open your email and click on the link sent to verify that you are not a Robot and to activate your account.')
            return redirect('/accounts/login/?command=verification&email='+email)  
    else:
        form = RegistrationForm()
    
    context = {
        'form': form,
    }
    return render(request, 'accounts/register.html', context)

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        user = auth.authenticate(email=email, password=password)
        
        if user is not None:
            auth.login(request, user)
            messages.success(request, ' You are logged in.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid login details. Please Try Again.')
            return redirect('login')
    return render(request, 'accounts/login.html')


@login_required(login_url = 'login')
def logout(request):
    auth.logout(request)
    messages.success(request, ' You have logged out successfully!')
    return redirect('login')


User = get_user_model()

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Congratulations! Your account has been activated.')
        # Additional actions, like logging the user in or redirecting
        return redirect('login')           #========================= Replace with your desired success page
    else:
        messages.error(request, ' Invalid activation link')#============= Invalid link or already activated
        return render(request, 'register')


@login_required(login_url='login')
def dashboard(request):
    return render(request, 'accounts/dashboard.html')