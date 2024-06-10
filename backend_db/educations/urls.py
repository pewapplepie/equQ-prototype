from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import SchoolViewSet, DegreeViewSet, DegreeViewViewSet, UserProfileViewSet, UserViewSet

urlpatterns = [
    path('schools', SchoolViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('schools/<str:pk>', SchoolViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('degrees', DegreeViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('degrees/<str:pk>', DegreeViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('degree-views', DegreeViewViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('degree-views/<str:pk>', DegreeViewViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('user-profiles', UserProfileViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('user-profiles/<str:pk>', UserProfileViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('users', UserViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('users/<str:pk>', UserViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
]
