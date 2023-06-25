from django.db.models import Q
from django.contrib.auth import get_user_model
from rest_framework.parsers import FileUploadParser,MultiPartParser,FormParser
from rest_framework import generics, mixins, response, status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated

from .models import Event, Comment
from .serializers import EventSerializer, CommentSerializer, EventDetailSerializer
from accounts.permissions import ViewPermissions, IsAuthorOrReadOnly
from core.pagination import CustomPagination
from accounts.serializers import UserSerializer
from accounts.authentication import JWTAuthentication

# events views

class EventListAPI(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = EventSerializer
    pagination_class = CustomPagination
    parser_classes = (MultiPartParser,FormParser)

    def get_queryset(self):
        user = self.request.user
        #get the followings
        following_users = [following.id for following in user.followers.all()]
        # check if following is 1 or more than 1 show the followers post else show all
        if following_users != []: # if len(following_users) >= 1:
            return Event.objects.filter(Q(author_id__in=following_users)|
            Q(author=self.request.user)).distinct()
        return Event.objects.all()
    
    def perform_create(self,serializer):
        return serializer.save(author=self.request.user)
    
class EventDetailAPI(generics.RetrieveDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Event.objects.all()
    serializer_class = EventDetailSerializer

class EventUpdateDeleteView(generics.RetrieveAPIView,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = EventSerializer

    def get_queryset(self):
        return Event.objects.filter(author=self.request.user)
    
    def patch(self,request,*args,**kwargs):
        return self.partial_update(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return response.Response(status=status.HTTP_204_NO_CONTENT)

# comments views

class CommentCreateAPI(generics.CreateAPIView):
    model = Comment
    serializer_class = CommentSerializer

    def perform_create(self,serializer):
        return serializer.save(author=self.request.user)

class CommentDelete(generics.RetrieveDestroyAPIView):
    model = CommentSerializer
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(author=self.request.user)

    def delete(self,request,*args,**kwargs):
        instance = self.get_object()
        print(instance)
        self.perform_destroy(instance)
        return response.Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def EventLikeAPI(request,pk):
    try:
        event = Event.objects.get(pk=pk) 
        if request.user in event.likes.all():
            event.likes.remove(request.user)
            return response.Response({"data":"Unliked"})
        else:
            event.likes.add(request.user)
            return response.Response({"data":"Liked"})
    except Event.DoesNotExist:
        return response.Response(status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def search(request):
    event_query = request.GET.get('event',None)
    user_query = request.GET.get('user',None)
    User = get_user_model()
    if event_query and not user_query:
        queryset = Event.objects.filter(body__icontains=post_query)
        return response.Response({
            "events":EventSerializer(
                queryset,many=True,
            context={'request':request}).data
        })

    if user_query and not event_query:
        queryset = User.objects.filter(username__icontains=user_query)
        return response.Response({"users":UserSerializer(queryset,many=True).data})

    if event_query and user_query:
        events = Event.objects.filter(body__icontains=event_query)
        users = User.objects.filter(username__icontains=user_query)
        return response.Response({
            "events":EventSerializer(events,many=True,context={'request':request}).data,
            "users":UserSerializer(users,many=True).data
        })
    return []