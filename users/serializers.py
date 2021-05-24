from rest_framework.serializers import Serializer, ModelSerializer
from .models import Comment


class CommentSerializer(Serializer):


    def create(self, validated_data=None):
        validated_data = validated_data if validated_data else self.validated_data
        return Comment.objects.create(**validated_data)

    def update(self, instance=None, validated_data=None):
        validated_data = validated_data if validated_data else self.validated_data
        instance = instance if instance else self.instance
        instance.user = validated_data.get('user', instance.user)
        instance.content = validated_data.get('content', instance.content)
        self.instance = instance
        self.instance.save()
        return self.instance

