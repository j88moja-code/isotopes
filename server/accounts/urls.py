from django.urls import path

from .views import (
    RegisterAPIView, login, logout, AuthenticatedUser,
    RoleViewSet, UsersListAPIView, ProfileAPIView,
    ProfileInfoAPIView, ProfilePasswordAPIView, follow_user,
    UserSearch
)

urlpatterns = [
    path('register', RegisterAPIView.as_view()),
    path('login', login),
    path('user', AuthenticatedUser.as_view()),
    path('logout', logout),
    path('roles', RoleViewSet.as_view({
        'get': 'list'
    })),
    path('users/info', ProfileInfoAPIView.as_view()),
    path('users/password', ProfilePasswordAPIView.as_view()),
    path('profile',ProfileAPIView.as_view()),
    path('all',UsersListAPIView.as_view(),name='user-list'),
    path('follow/<str:pk>',follow_user),
    path('search',UserSearch.as_view()),

]