from django.urls import path
from .views import *

urlpatterns = [
    path('events', EventListAPI.as_view()),
    path('events/<str:pk>',EventDetailAPI.as_view()),
    path('events/edit/<str:pk>',EventUpdateDeleteView.as_view()),
    path('events/like/<str:pk>',EventLikeAPI),
    path('events/comment',CommentCreateAPI.as_view()),
    path('events/comment/<str:pk>',CommentDelete.as_view()),
    path('search',search),
]