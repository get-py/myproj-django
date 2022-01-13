import json

from django.db.migrations import serializer
from django.http import HttpResponse
from rest_framework import viewsets
from news.models import Article
from news.serializers import ArticleSerializer
from rest_framework.generics import ListAPIView


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


article_list = ListAPIView.as_view(
    queryset=Article.objects.all(),
    serializer_class=ArticleSerializer,
)


# def article_list(request):
#     qs=Article.objects.all()
#     serializer = ArticleSerializer(qs, many=True)
#     data = serializer.data
#
#     json_string = json.dumps(data)
#     return HttpResponse(json_string)
