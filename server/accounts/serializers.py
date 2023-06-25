from rest_framework import serializers
from .models import Permission, Role, User

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'


class PermissionRelatedField(serializers.StringRelatedField):
    def to_representation(self, value):
        return PermissionSerializer(value).data

    def to_internal_value(self, data):
        return data


class RoleSerializer(serializers.ModelSerializer):
    permissions = PermissionRelatedField(many=True)

    class Meta:
        model = Role
        fields = '__all__'

class RoleRelatedField(serializers.RelatedField):
    def to_representation(self, instance):
        return RoleSerializer(instance).data

    def to_internal_value(self, data):
        return self.queryset.get(pk=data)
    

class UserSerializer(serializers.ModelSerializer):
    role = RoleRelatedField(many=False, queryset=Role.objects.all())
    total_followers = serializers.SerializerMethodField()
    is_following = serializers.SerializerMethodField()
    
    def get_total_followers(self,instance):
        return instance.followers.count()
    
    def get_is_following(self,instance):
        request = self.context.get('request',None)
        if request:
            user = request.user
            return user in instance.followers.all()
        
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'bio', 'profile_image' ,'total_followers','is_following', 'password', 'role']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
