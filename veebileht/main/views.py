from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def register_request(request):
    form = NewUserForm()
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/")
    return render(request=request, template_name="register.html", context={"register_form": form})

def login_request(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
    return render(request=request, template_name="login.html", context={"login_form": form})

def logout_request(request):
    logout(request)
    return redirect("/")

@login_required(login_url="/preview")
def home(response):
    return render(response, "home.html", {})

def preview(response):
    return render(response, "preview.html", {})

