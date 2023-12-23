from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

from .forms import SignUpForm
from .models import Room

# Create your views here.

def home(request):
    return render(request, "core/home.html")

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            login(request, user)
            
            return redirect('home')
    else:
        form = SignUpForm()
    
    return render(request, 'core/signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def rooms(request):
    rooms = Room.objects.all()
    
    return render(request, 'core/rooms.html', {'rooms': rooms})

@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    
    return render(request, 'core/room.html', {'room': room})