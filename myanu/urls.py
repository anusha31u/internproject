from django.urls import path
from myanu.viewsets import UserViewSet

urlpatterns = [
    path('myanu/', UserViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('myanu/<int:pk>/', UserViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('search/', UserViewSet.as_view({'get': 'search', 'post': 'search'})),
]
