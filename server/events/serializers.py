from rest_framework import serializers
from .models import Event, Comment
from django.contrib.auth import get_user_model


class EventUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id','email','profile_image')


class EventSerializer(serializers.ModelSerializer):
    author_detail = EventUserSerializer(source='author',read_only=True)
    image = serializers.ImageField(required=False, max_length=None, 
                                     allow_empty_file=True, use_url=True,allow_null=True)
    total_likes = serializers.SerializerMethodField()
    class Meta:
        model = Event
        fields = ('id','body','image', 'line_up', 'entrance_fee', 'total_likes','created_at','author','author_detail')
        extra_kwargs = {
            'author': {'required': False},
        }
    
    def get_total_likes(self,instance):
        return instance.likes.count()

class CommentSerializer(serializers.ModelSerializer):
    author_detail = EventUserSerializer(source='author',read_only=True)
    class Meta:
        model = Comment
        fields = ('id','body','author','author_detail','event')
        extra_kwargs = {'author': {'required': False}}


class EventDetailSerializer(EventSerializer):
    author_detail = EventUserSerializer(source='author',read_only=True)
    comments = CommentSerializer(many=True,read_only=True)

    class Meta:
        model = Event
        fields = ('id','body','image', 'line_up', 'entrance_fee', 'created_at','author','author_detail','comments','total_likes')
