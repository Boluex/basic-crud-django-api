import imp
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from.serializer import profileserializer,registerserializer
from django.http import HttpResponse
from.forms import profile_form,user_form
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from.models import profile
# from rest_framework.authentication import w      

# Create your views here.
def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('password')

        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            messages.success(request, f'welcome back {username}')
            return redirect('home')
        else:
            messages.error(request,'you are not registered yet,kindly register')
            return redirect('register')

    return render(request, 'users/login.html')
def sign_out(request):
    logout(request)
    return redirect('sign_in')

@login_required
# def profile(request):
#     return render(request,'users/profile.html')
def profiles(request):
    try:
        get_profile=profile.objects.get(user=request.user)
    except profile.DoesNotExist:
        return HttpResponse('Does Not Exist')
    serializer=profileserializer(get_profile)
    print(serializer)
    context={
        'profile':serializer.data
    }
    
    return render(request,'users/profile.html',context)

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 == pass2:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email taken')
                return redirect('register')

            else:
                store = User.objects.create_user(username=username, email=email, password=pass1)
                # send_mail(
                #     'Greetings from blogify',
                #     f'Welcome {username}, to the the best blog site,with latest and trending topics,we are 100% sure you will like it',
                #     settings.EMAIL_HOST_USER, [email], fail_silently=False
                # )
                store.save()
                user = authenticate(request, username=username, password=pass1)
                if user is not None:
                    login(request, user)
                    messages.success(request, f'welcome {username}')
                    return redirect('home')
        else:
            messages.error(request, "Both password field don't match,input match passwords ")
            return redirect('register')
    return render(request, 'users/register.html')


@login_required
def update_profile(request):
    user=request.user
    if request.method == 'POST':
        u_form = user_form(request.POST, instance=request.user)
        p_form = profile_form(request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Updated successful')
    else:
        u_form = user_form()
        p_form = profile_form()
    return render(request, 'users/update_profile.html', {'u_form': u_form, 'p_form': p_form})
# def register(request):
#     if request.method =='POST':
#         user=User()
#         serializer=registerserializer(user,data=request.POST)
#         if serializer.is_valid():
#             serializer.save(raise_exception=True)
#             # login_user=authenticate(request,username=serializer.username,password=serializer.password2)
#             # if login_user is not None :
#             #     login(request,login_user)
#             #     return redirect('/')
#             # messages.error(request,'oops no user found,try registering again')
#             return redirect('sign_in')
#         messages.error(request,'we cannot save this right now')
#         return redirect('register')
#     return render(request,'users/register.html')
