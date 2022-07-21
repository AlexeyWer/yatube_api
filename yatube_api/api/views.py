from rest_framework import filters, viewsets
from rest_framework.exceptions import NotFound
from rest_framework.pagination import LimitOffsetPagination

from posts.models import Comment, Group, Post

from .mixins import ListCreateViewSet
from .permissions import IsOwnerOrReadOnly
from .serializers import (
    CommentSerializers,
    FollowSerializers,
    GroupSerializers,
    PostSerializers
)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    permission_classes = [IsOwnerOrReadOnly]
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializers
    permission_classes = [IsOwnerOrReadOnly]


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializers
    permission_classes = [IsOwnerOrReadOnly]
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        new_queryset = Comment.objects.filter(post=post_id)
        return new_queryset

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        post = Post.objects.filter(pk=post_id)
        if not post.exists():
            raise NotFound(detail=f'Поста с номером {post_id} не существует')
        serializer.save(author=self.request.user, post=post[0])


class FollowViewSet(ListCreateViewSet):
    serializer_class = FollowSerializers
    filter_backends = (filters.SearchFilter, )
    search_fields = ('following__username',)

    def get_queryset(self):
        user = self.request.user
        return user.follower

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
