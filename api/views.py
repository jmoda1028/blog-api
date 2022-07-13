from django.shortcuts import render
from .serializers import PostSerializer
from .models import Post
from .paginations import *
from django.http import JsonResponse
import json

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    pagination_class = PostStandardResultsSetPagination

    @api_view(['GET'])
    def post_list(request):
        posts = Post.objects.all().order_by('-created_at')
        
        serializer = PostSerializer(posts, many=True)
        # paginator = PostStandardResultsSetPagination()
        # result_page = paginator.paginate_queryset(list(result), request)

        result = serializer.data

        paginator = PostStandardResultsSetPagination()
        result_page = paginator.paginate_queryset(list(result), request)
        res = paginator.get_paginated_response(result_page)

        return res
        # result = Post.objects.values('id', 'title', 'body', 'publish', 'status', 
        #                                   'author', 'created_at', 'updated_at')
        # paginator = PostStandardResultsSetPagination()
        
    
        # result_page = paginator.paginate_queryset(list(result), request)                                  
        # res = paginator.get_paginated_response(result_page)
        # serializer = PostSerializer(res, many=True)
        # response = serializer.data
        # return Response(response)


    @api_view(['POST'])
    def add_post(request):
        if request.method == 'POST':
            serializer = PostSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
    def post_detail(request, pk):
        try:
            post = Post.objects.get(id=pk)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = PostSerializer(post,context={'request': request})
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = PostSerializer(post, data=request.data,context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'PATCH':
            serializer = PostSerializer(post, data=request.data,partial=True, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

        elif request.method == 'DELETE':
            post.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)