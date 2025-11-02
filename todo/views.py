from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from todo.models import ToDo


def signup(request):
    """Signup view with validation and duplicate-username handling."""
    if request.user.is_authenticated:
        return redirect('todo_home')
    
    if request.method == 'POST':
        username = (request.POST.get('username') or '').strip()
        email = (request.POST.get('email') or '').strip()
        password = request.POST.get('password') or ''

        # Basic required-field validation
        if not username or not password:
            return render(request, 'signup.html', {
                'error': 'Username and password are required.',
                'username': username,
                'email': email,
            })

        # Prevent IntegrityError by checking existence first
        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {
                'error': 'Username already taken. Please choose another.',
                'username': username,
                'email': email,
            })

        # Create the user
        user = User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, 'Account created successfully! Please login.')
        return redirect('login')
    
    return render(request, 'signup.html')


def login(request):
    """Login view - authenticate user by username or email."""
    if request.user.is_authenticated:
        return redirect('todo_home')
    
    if request.method == 'POST':
        username_or_email = (request.POST.get('email') or '').strip()
        password = request.POST.get('password') or ''
        
        if not username_or_email or not password:
            return render(request, 'login.html', {
                'error': 'Please provide both username/email and password.'
            })
        
        # Try to authenticate with username first, then email
        user = authenticate(request, username=username_or_email, password=password)
        
        # If authentication failed, try to find user by email
        if user is None and '@' in username_or_email:
            try:
                user_obj = User.objects.get(email=username_or_email)
                user = authenticate(request, username=user_obj.username, password=password)
            except User.DoesNotExist:
                pass
        
        if user is not None:
            auth_login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect('todo_home')
        else:
            return render(request, 'login.html', {
                'error': 'Invalid username/email or password.'
            })
    
    return render(request, 'login.html')


@login_required(login_url='login')
def logout(request):
    """Logout view."""
    auth_logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login')


@login_required(login_url='login')
def todo_home(request):
    """Display all todos for the logged-in user."""
    todos = ToDo.objects.filter(user=request.user)
    return render(request, 'todo.html', {'todos': todos})


@login_required(login_url='login')
def add_todo(request):
    """Add a new todo item."""
    if request.method == 'POST':
        title = (request.POST.get('title') or '').strip()
        description = (request.POST.get('description') or '').strip()
        
        if title:
            ToDo.objects.create(
                title=title,
                description=description,
                user=request.user
            )
            messages.success(request, 'Todo added successfully!')
        else:
            messages.error(request, 'Title is required!')
    
    return redirect('todo_home')


@login_required(login_url='login')
def update_todo(request, todo_id):
    """Update an existing todo item."""
    todo = get_object_or_404(ToDo, sno=todo_id, user=request.user)
    
    if request.method == 'POST':
        title = (request.POST.get('title') or '').strip()
        description = (request.POST.get('description') or '').strip()
        
        if title:
            todo.title = title
            todo.description = description
            todo.save()
            messages.success(request, 'Todo updated successfully!')
        else:
            messages.error(request, 'Title is required!')
    
    return redirect('todo_home')


@login_required(login_url='login')
def delete_todo(request, todo_id):
    """Delete a todo item."""
    todo = get_object_or_404(ToDo, sno=todo_id, user=request.user)
    todo.delete()
    messages.success(request, 'Todo deleted successfully!')
    return redirect('todo_home')


@login_required(login_url='login')
def toggle_todo(request, todo_id):
    """Toggle the completed status of a todo item."""
    todo = get_object_or_404(ToDo, sno=todo_id, user=request.user)
    todo.completed = not todo.completed
    todo.save()
    return redirect('todo_home')