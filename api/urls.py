from django.urls import path
from . import views

urlpatterns = [
    #Todo
    path('tasks', views.taskListCreate.as_view()),
    path('tasks/<int:pk>', views.taskRetrieveUpdateDestroy.as_view()),
    path('tasks/<int:pk>/complete', views.taskComplete.as_view()),
    path('tasks/completed', views.taskCompletedList.as_view()),
    
    #Auth
    path('signup', views.signup),
    path('login', views.login),
]
