from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import exceptions, generics, viewsets
from rest_framework.decorators import api_view, parser_classes

from .models import User, Role
from .serializers import UserSerializer, RoleSerializer
from .authentication import generate_access_token, JWTAuthentication
from events.models import Event
from events.serializers import EventSerializer

class RegisterAPIView(APIView):
    def post(self, request):
        data = request.data

        if data['password'] != data['confirm_password']:
            raise exceptions.APIException('Passwords do not match!')

        request.data.update({
        'role': request.data['role_id']
        })
        serializer = UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    user = User.objects.filter(email=email).first()

    if user is None:
        raise exceptions.AuthenticationFailed('User not found!')
    
    if not user.check_password(password):
        raise exceptions.AuthenticationFailed('Incorrect password')
    
    response = Response()

    token = generate_access_token(user)
    response.set_cookie(key='jwt', value=token, httponly=True)
    response.data = {
        'jwt': token
    }

    return response

@api_view(['POST'])
def logout(_):
    response = Response()
    response.delete_cookie(key='jwt')
    response.data = {
        'message': 'Successfully logged out'
    }

    return response

class AuthenticatedUser(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        data = UserSerializer(request.user).data
        data['permissions'] = [p['name'] for p in data['role']['permissions']]

        return Response({
            'data': data
        })

class RoleViewSet(viewsets.ViewSet):

    def list(self, request):
        serializer = RoleSerializer(Role.objects.all(), many=True)

        return Response({
            'data': serializer.data
        })

    def retrieve(self, request, pk=None):
        role = Role.objects.get(id=pk)
        serializer =  RoleSerializer(role)

        return Response({
            'data': serializer.data
        })
    
class UsersListAPIView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProfileAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_current_user(self):
        user_serializer = UserSerializer(self.request.user,context={'request': self.request})
        return user_serializer.data
    
    def get_user_posts(self):
        user_posts = Event.objects.filter(author=self.request.user)
        return EventSerializer(user_posts,many=True,context={'request':self.request}).data

    def get(self,*args,**kwargs):
        return Response({
        'user':self.get_current_user(),
        'posts':self.get_user_posts()
    })

class ProfileInfoAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]
    
    def put(self, request, pk=None):
        user = request.user
        serializer = UserSerializer(user,request.data,partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class ProfilePasswordAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request, pk=None):
        user = request.user

        if request.data['password'] != request.data['confirm_password']:
            raise exceptions.ValidationError('Passwords do not match')

        user.set_password(request.data['password'])
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
@api_view(['GET'])
def follow_user(request,pk):
    user = User.objects.get(pk=pk)
    current_user = request.user
    if current_user in user.followers.all():
        user.followers.remove(current_user)
        return  Response({"data":"Unfollowed"})
    else:
        user.followers.add(current_user)
        return Response({"data":"Followed"})

class UserSearch(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        search_query = self.request.query_params.get('q',None)
        if search_query:
            queryset = User.objects.filter(username__icontains=search_query)
        return queryset