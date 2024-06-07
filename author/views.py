from django.shortcuts import render,redirect
from . import forms
from django.contrib.auth.forms import  AuthenticationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth import authenticate , login ,logout,update_session_auth_hash
from django.contrib import messages
from post.models import post
from django.contrib.auth.decorators import login_required
    
# Create your views here.
def register(request):
    if not request.user.is_authenticated :
        if request.method=='POST':
            register_form = forms.RegistrationForm(request.POST)
            if register_form.is_valid():
                register_form.save()
                messages.success(request, 'Account Created Successfully Completed')

            return redirect('register')
        
        else:
         register_form = forms.RegistrationForm()  
        return render(request, 'register.html' , {'data' : register_form , 'type' : 'register'} )
    
    else:
        return redirect('register')
 
def log_in(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            form = AuthenticationForm(request, request.POST)
            if form.is_valid():
                user_name = form.cleaned_data['username']
                pass_word = form.cleaned_data['password']
                user = authenticate(username = user_name , password = pass_word)
                if user is not None :
                    messages.success(request, "Logged in Complete successfully")
                    login(request, user)
                    return redirect('profile')               
                else:
                    messages.success(request, 'Your information is incorrect ')
                    return redirect('register')               
        else :
            form = AuthenticationForm()   
    else:
        
        form = AuthenticationForm()
    return render(request, 'register.html' , {'data' : form , 'type' : 'log_in'} )  
    
    
def log_out(request):
    logout(request)
    return redirect ('log_in')

@login_required
def profile(request):
    
    form = post.objects.filter(authors = request.user)     
    return render(request, 'profile.html' ,{'data': form} )
    



def edit_profile(request):
    
        if request.method=='POST':
            profile_form = forms.user_change_data(request.POST , instance = request.user )
            if profile_form.is_valid():
                profile_form.save()
                messages.success(request, 'Profile update Successfully Completed')

            return redirect('profile')
        
        else:
         profile_form = forms.user_change_data( instance = request.user)  
        return render(request, 'edit_profile.html' , {'data' : profile_form } )










def pass_change(request):
    
        if request.method=='POST':
            pass_form = PasswordChangeForm(request.user, data=request.POST )
            if pass_form.is_valid():
                pass_form.save()
                messages.success(request, 'Password update Successfully Completed')
                update_session_auth_hash(request, pass_form.user)
                return redirect('profile')
        
        else:
         pass_form = PasswordChangeForm(request.user)  
        return render(request, 'pass_change.html' , {'data' : pass_form } )