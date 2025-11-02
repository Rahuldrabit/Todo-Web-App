"""
URL configuration for todo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Authentication URLs
    path('', views.login, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    
    # Todo URLs
    path('todo/', views.todo_home, name='todo_home'),
    path('todo/add/', views.add_todo, name='add_todo'),
    path('todo/update/<int:todo_id>/', views.update_todo, name='update_todo'),
    path('todo/delete/<int:todo_id>/', views.delete_todo, name='delete_todo'),
    path('todo/toggle/<int:todo_id>/', views.toggle_todo, name='toggle_todo'),
]
