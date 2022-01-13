from rest_framework import serializers
import re
from news.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"

    # def validate_title(self, title):
    #     if len(title) < 3:
    #         raise serializers.ValidationError("3글자 이상!!")
    #     if not re.search(r"[ㄱ-힣]", title):
    #         raise serializers.ValidationError("한글을 써주세요")
    #     return title