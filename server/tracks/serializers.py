from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Track, TrackComment

class TrackUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('id','email','profile_image')

class TrackSerializer(serializers.ModelSerializer):

    user_detail = TrackUserSerializer(source='user', read_only=True)
    cover_art = serializers.ImageField(required=False, max_length=None, 
                                       allow_empty_file=True, use_url=True, allow_null=True)
    total_likes = serializers.SerializerMethodField()

    class Meta:
        model = Track
        fields = ('id', 'file', 'title',  'artists', 'genre', 'cover_art', 'total_likes', 'uploaded_at', 
                  'user', 'user_detail')
        extra_kwargs = {
            'user': {'required': False},
        }


    def get_total_likes(self,instance):
        return instance.likes.count()
        
class TrackCommentSerializer(serializers.ModelSerializer):

    author_detail = TrackUserSerializer(source='author', read_only=True)

    class Meta:
        model = TrackComment
        fields = ('id', 'body', 'author', 'author_detail', 'track')

        extra_kwargs = {'author': {'required': False}}

class TrackDetailSerializer(TrackSerializer):
    user_detail = TrackUserSerializer(source='user', read_only=True)
    comments = TrackCommentSerializer(many=True, read_only=True)

    class Meta:
        model = Track
        fields = ('id', 'file', 'title',  'artists', 'genre', 'cover_art', 'user', 'user_detail', 'comments','total_likes','uploaded_at')