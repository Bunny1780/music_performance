from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm, EditForm
from .models import Location, Unit, MusicEvent

def index(request):
    return render(request, "index.html")

def user_login(req):
    if req.method == "POST":
        form = LoginForm(req.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(req, username=username, password=password)
            if user:
                login(req, user)
                messages.success(req, "登入成功")
                return redirect('apps:index')
            else :
                messages.error(req, "登入失敗")
    else:
        form = LoginForm()
    return render(req, "login.html", {'form':form})

def register(req):
    if req.method == "POST":
        form = RegisterForm(req.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('apps:login')
    else:
        form = RegisterForm()
    return render(req, "register.html", {'form':form})

def user_logout(req):
    logout(req)
    return redirect('apps:login')

def operation(req):
    search_query = req.GET.get('search', '')
    if search_query:
        music_events = MusicEvent.objects.filter(title__icontains=search_query)
    else:
        music_events = MusicEvent.objects.all()
    return render(req, "operation.html", {"musicEvents": music_events})

@login_required
def edit(req, id):
    musicEvent = get_object_or_404(MusicEvent, pk = id)
    if req.method == "POST":
        form = EditForm(req.POST, instance=musicEvent)
        if form.is_valid():
            form.save()
            return redirect('apps:operation')
    else:
        form = EditForm(instance=musicEvent)
    return render(req, "edit.html", {"musicEvent": musicEvent, "form": form})

@login_required
def delete(req, id):
    musicEvent = get_object_or_404(MusicEvent, pk = id)
    musicEvent.delete()
    return redirect('apps:operation')