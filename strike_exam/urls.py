from django.contrib import admin
from django.urls import path, include
from strikeTaskWeb import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.homepage, name='home'),
    path('usersignup/', views.usersignup, name='usersignup'),
    path('requiredtask/', views.requiredtasks, name='requiredtasks'),
    path('completedtasks', views.completedtask, name='completedtasks'),
    path('taskcreation/', views.taskcreation, name='taskcreation'),
    path('userlogin/', views.userlogin, name='userlogin'),
    path('userlogout/', views.userlogout, name='userlogout'),
    path('<int:pk>/', views.taskview, name='taskview'),
    path('<int:pk>/delete', views.deletetask, name='deletetask'),
    path('todo/<int:pk>/taskcomplete', views.taskcomplete, name='taskcomplete'),
    
    path('api/', include('api.urls')),
]
