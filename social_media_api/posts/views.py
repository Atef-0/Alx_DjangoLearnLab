from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework import permissions
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination

class DefaultPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class isOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user

# Create your views here.

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all().select_related('author')
    serializer_class = PostSerializer
    permission_classes = [isOwnerOrReadOnly, permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    pagination_class = DefaultPagination
    ordering_fields = ['created_at', 'updated_at', 'title']
    search_fields = ['title', 'content', 'author__username']


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all().select_related('author', 'post')
    serializer_class = CommentSerializer
    permission_classes = [isOwnerOrReadOnly, permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    pagination_class = DefaultPagination
    ordering_fields = ['created_at', 'updated_at']
    search_fields = ['content', 'author__username', 'post__title']

from django.shortcuts import render

["viewsets", "viewsets.ModelViewSet", "Comment.objects.all()", "Post.objects.all()"]
# Create your views here.

["Post.objects.filter(author__in=following_users).order_by"
 "following.all()"
 "permissions.IsAuthenticated"]
["generics.get_object_or_404(Post, pk=pk)", "Like.objects.get_or_create(user=request.user, post=post)", "Notification.objects.create"]