from django.urls import path
from .views import *

urlpatterns = [
    path('tracks', TrackListAPI.as_view()),
    path('tracks/<str:pk>', TrackDetailAPI.as_view()),
    path('tracks/edit/<str:pk>', TrackUpdateDeleteView.as_view()),
    path('tracks/like/<str:pk>', TrackLikeAPI),
    path('tracks/comment', TrackCommentCreateAPI.as_view()),
    path('tracks/comment/<str:pk>', TrackCommentDelete.as_view()),
    path('search',search_track),
]