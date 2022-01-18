from django.http import HttpResponse
from rest_framework import viewsets
import json

from rest_framework.permissions import AllowAny, IsAuthenticated

from blog.models import Post
from blog.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


def post_list(request):
    qs = Post.objects.all()
    data = [
        {"id": post.id, "title": post.title, "content": post.content} for post in qs
    ]
    json_string = json.dumps(data)
    return HttpResponse(json_string)
