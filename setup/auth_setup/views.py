from django.shortcuts import render,redirect
from django.http import Http404, HttpResponse
from django.contrib.auth import authenticate, login
from . import models
from . import forms

def home(request):
    if request.user.is_authenticated:
        cards = models.PostModel.objects.all().order_by('date')
        return render(request, 'pages/home/home.html', {'cards':cards})
    else:
        return redirect('auth:login')
#  POST
def post(request):
    if request.method == 'GET':
        form = forms.PostForm()
    if request.method == 'POST':
        form = forms.PostForm(request.POST)
        
        if form.is_valid():
            form.save()
            form = forms.PostForm()
            
    return render(request, 'pages/post/post.html', {'PostForm':form})
# AUTH
def auth(request):
    if request.method == 'GET':
        form = forms.RegisterForm(request.session.get('register_form_data')) or forms.RegisterForm()
            
        return render(request, 'pages/auth/auth.html', {'RegisterForm':form})

def auth_register(request):
    if request.method == 'GET':
        form = forms.RegisterForm()
        return render(request, 'pages/auth/auth.html', {'RegisterForm':form})

    if request.method == 'POST':
        POST = request.POST
        request.session['register_form_data'] = POST
        RegisterForm = forms.RegisterForm(POST)
        
        
        if RegisterForm.is_valid():
            RegisterForm.save()
            request.session['register_form_data'] = None
            
            return redirect('auth:login')
    return redirect('auth:auth')

def auth_login(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request, 'pages/auth/auth.html', {})
        else:
            form = forms.LoginForm(request.session.get('login_form_data')) or forms.LoginForm()
            return render(request, 'pages/auth/auth.html', {'LoginForm':form})
    if request.method == 'POST':
        POST = request.POST
        request.session['login_form_data'] = POST
        form = forms.LoginForm(POST)
        
        if form.is_valid():
            authenticated_user = authenticate(
                username=form.cleaned_data.get('username',''),
                password=form.cleaned_data.get('password','')
                )
            print(authenticated_user)
            if authenticated_user is not None:
                login(request, authenticated_user)
                return redirect('home')
                
            else: 
                print('ta errado burrao')
                request.session['login_form_data'] = request.POST
                return redirect('auth:login')
                
        else:
            return redirect('auth:login')

# def auth(request):
#     if request.method == 'POST':
#         form = forms.RegisterForm(request.POST)
    
#     if request.method == 'GET':
        
#         register_form = request.session['register_form_data'] or None 
        
#         form = forms.RegisterForm(register_form)
        
#     return render(request, 'pages/auth/auth.html', {'form': form})

# def auth_register(request):
    
#     if not request.POST:
#         raise Http404()
    
#     POST = request.POST
#     request.session['register_form_data'] = POST
    
#     return redirect('auth:auth')