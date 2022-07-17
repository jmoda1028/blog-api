from rest_framework import serializers
from rest_framework.serializers import StringRelatedField
from .models import *

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):

        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            middle_name=validated_data['middle_name'],
            last_name=validated_data['last_name'],
            mobile_no=validated_data['mobile_no'],
            role=validated_data['role'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class PostSerializer(serializers.ModelSerializer):

    # username = serializers.SerializerMethodField('get_username')
    # author   = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # author = serializers.ReadOnlyField(source='author.username')
    author = StringRelatedField()
    class Meta:
            model = Post
            fields = ('id', 'title', 'author', 'body', 'publish', 'created_at', 'updated_at', 'status')


    # def get_username(self):
    #     author =  self.context['request'].user