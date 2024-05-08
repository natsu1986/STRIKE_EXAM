from rest_framework import generics, permissions
from .serializer import taskSerializer, taskCompleteSerializer
from strikeTaskWeb.models import task
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from django.db import IntegrityError
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            user = User.objects.create_user(data['username'], password=data['password'])
            user.save()
            token = Token.objects.create(user=user)
            return JsonResponse({'token':str(token)}, status=201)
        except IntegrityError:
            return JsonResponse({'error':'That username has already been taken. Please choose a new username'}, status=401)
        
        
@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        user = authenticate(request, username=data['username'], password=data['password'])
        if user is None:
            return JsonResponse({'error':'Could not login Please check username and password'}, status=401)
        else:
            try:
                token = Token.objects.get(user=user)
            except:
                token = Token.objects.create(user=user)
            return JsonResponse({'token':str(token)}, status=200)
               
class taskCompletedList(generics.ListAPIView):
    serializer_class = taskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return task.objects.filter(user=user, datecompleted__isnull=False).order_by('-datecompleted')


class taskListCreate(generics.ListCreateAPIView):
    serializer_class = taskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return task.objects.filter(user=user, datecompleted__isnull=True)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class taskRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = taskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return task.objects.filter(user=user)

class taskComplete(generics.UpdateAPIView):
    serializer_class = taskCompleteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return task.objects.filter(user=user)
    
    def perform_update(self, serializer):
        serializer.instance.datecompleted = timezone.now()
        serializer.save()