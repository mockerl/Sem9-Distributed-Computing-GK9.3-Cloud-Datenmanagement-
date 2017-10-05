from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')


#class SnippetSerializer(serializers.Serializer):
#    id = serializers.IntegerField(read_only=True)
#    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#    username = serializers.CharField(max_length=100, allow_blank=False)
#    name = serializers.CharField(max_length=100, allow_blank=False)
#    surname = serializers.CharField(max_length=100, allow_blank=False)
#    surname = serializers.CharField(max_length=100, allow_blank=False)
#    linenos = serializers.BooleanField(required=False)
#
#    def create(self, validated_data):
#        """
#        Create and return a new `User` instance, given the validated data.
#        """
#        return User.objects.create(**validated_data)
#
#    def update(self, instance, validated_data):
#        """
#        Update and return an existing `User` instance, given the validated data.
#        """
#        instance.title = validated_data.get('title', instance.title)
#        instance.username = validated_data.get('username', instance.username)
#        instance.name = validated_data.get('name', instance.name)
#        instance.surname = validated_data.get('surname', instance.surname)
#        instance.password = validated_data.get('password', instance.password)
#        instance.save()
#        return instance
#