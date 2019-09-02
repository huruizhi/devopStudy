from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    """
    User 序列化类
    """
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(required=True, max_length=32)
    email = serializers.EmailField(required=True, max_length=50)

