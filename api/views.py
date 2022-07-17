from django.shortcuts import render
from .serializers import *
from .models import *
from .paginations import *


from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView

# Create your views here.
class RoleView(viewsets.ModelViewSet):
    queryset = Role.objects.all().order_by('-created_at')
    serializer_class = RoleSerializer


class UserView(viewsets.ModelViewSet):  
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class RoleView(viewsets.ModelViewSet):
    queryset = Role.objects.all().order_by('-created_at')
    serializer_class = RoleSerializer


class UserView(viewsets.ModelViewSet):  
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    pagination_class = PostStandardResultsSetPagination
    permission_classes = [IsAuthenticated]

    def perform_create(self,serializer):
		    serializer.save(author=self.request.user)

    


# class PostCreateView(CreateAPIView):
# 	serializer_class = PostSerializer

    
# 	def perform_create(self,serializer):
# 		serializer.save(author=self.request.user)