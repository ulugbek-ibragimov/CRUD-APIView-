from rest_framework import serializers
from .models import *

class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ['id','title', 'file']

class CategorySerializer(serializers.ModelSerializer):
    # count = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Category
        fields = ['id','title', 'order']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id','name']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['firstname', 'lastname', 'avatar',  'facebook', 'instagram', 'twitter' ]

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "email", "profile"]

class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    image = MediaSerializer(many=True, read_only=True)
    author = UserSerializer(read_only=True)
    tags = TagSerializer(read_only=True)
    class Meta:
        model = Post
        fields = ['id','title', 'author', 'body', 'image', 'category', 'tags']

class TagPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagPost
        fields = ['id','tag', 'post']








## def create(self, validated_data):
#     return Category.objects.create(**validated_data)
# def update(self, instance, validated_data):
#     instance.title = validated_data.get("title", instance.title) #title yangi qiymati valid bo'lmasa 2-argument qabul qilinadi
    # va boshqa atributlar
    #instance.save()
    #return instance
