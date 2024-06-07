from django.shortcuts import render,redirect
from . import forms
from . import models
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def post_form(request):
    if request.method=='POST':
        post_form = forms.post_form(request.POST)
        if post_form.is_valid():
            post_form.instance.authors = request.user
            post_form.save()
        return redirect('add_post')
    
    else:
     post_form = forms.post_form()  
     return render(request, 'post.html' , {'data' : post_form})
 
 
@login_required
def edit_post(request,id):
    post = models.post.objects.get(pk=id)
    post_form = forms.post_form(instance= post)
    if request.method=='POST':
        post_form = forms.post_form(request.POST , instance=post)
        if post_form.is_valid():
            post_form.instance.authors = request.user
            post_form.save()
        return redirect('add_post')  
    
    return render(request, 'post.html' , {'data' : post_form}) 
@login_required
def delete(request, id):
    post= models.post.objects.get(pk=id)
    post.delete()
    return redirect('homepage')