from rest_framework import serializers
from app.models import Blog, Comment, Tag, Category


class blogSerializer(serializers.ModelSerializer):
    comment = serializers.SerializerMethodField()
    class Meta:
        model = Blog
        fields = '__all__'

    def get_comment(Self, obj):
        return commentSerializer(obj.blog_comment.all(), many=True).data


class commentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class tagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category 
        fields = "__all__"