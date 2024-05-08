from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import taskcreationForm
from .models import task
from django.utils import timezone
from django.contrib.auth.decorators import login_required

def homepage(request):
    return render(request, 'home.html')

def usersignup(request):
    if request.method == 'GET':
        return render(request, 'usersignup.html', {'form':UserCreationForm()})
    else:
        if request.POST['password_A'] == request.POST['password_B']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password_A'])
                user.save()
                login(request, user)
                return redirect('requiredtasks')
            except IntegrityError:
                return render(request, 'usersignup.html', {'form':UserCreationForm(), 'error':'The username you chose have been taken. Please enter a new username'})
        else:
            return render(request, 'usersignup.html', {'form':UserCreationForm(), 'error':'Passwords do not match. Please, enter the password agian'})
        
def userlogin(request):
    if request.method == 'GET':
        return render(request, 'userlogin.html')
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])   
        if user is not None:
            login(request, user)
        else:
         user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'userlogin.html', {'form':AuthenticationForm(), 'error':'Username and password do not match. Please, try again ^^'})
        else:
            login(request, user)
            return redirect('requiredtasks')
        
@login_required
def requiredtasks(request):
    tasks = task.objects.filter(user=request.user, datecompleted__isnull = True)
    return render(request, 'requiredtasks.html', {'tasks':tasks})
        
@login_required
def userlogout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    
@login_required
def taskcreation(request):
    if request.method == 'GET':
        return render(request, 'taskcreation.html', {'form':taskcreationForm()})
    else:
        try:
            form = taskcreationForm(request.POST)
            newtask = form.save(commit=False)
            newtask.user = request.user
            newtask.save()
            return redirect('requiredtasks')
        except ValueError:
            return render(request, 'taskcreation.html', {'form':taskcreationForm(), 'error':'Error in passing in information. Please, enter again with correct information'})

@login_required
def completedtask(request):
    tasks = task.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
    return render(request, 'completedtasks.html', {'tasks':tasks})

@login_required
def taskview(request, pk):
    task_ = get_object_or_404(task, pk=pk, user=request.user)
    if request.method == 'GET':
        form = taskcreationForm(instance=task_)
        return render(request, 'taskview.html', {'task':task_, 'form':form})
    else:
        try:
            form = taskcreationForm(request.POST, instance=task_)
            form.save()
            return redirect('requiredtasks')
        except ValueError:
            return render(request, 'taskview.html', {'task':task_, 'form':form, 'error':'Error in passing in information. Please, enter again with correct information'})   
        
@login_required
def taskcomplete(request, pk):
    task_ = get_object_or_404(task, pk=pk, user=request.user)
    if request.method == 'POST':
        task_.datecompleted = timezone.now()
        task_.pending_status = False
        task_.save()
        return redirect('requiredtasks')

@login_required
def deletetask(request, pk):
    task_ = get_object_or_404(task, pk=pk, user=request.user)
    if request.method == 'POST':
        task_.delete()
        return redirect('requiredtasks')