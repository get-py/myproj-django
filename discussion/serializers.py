from rest_framework import serializers

from discussion.models import HotPotato


class HotPotatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotPotato
        fields = "__all__"
