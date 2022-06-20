from django.urls import path
from .views import (
    PostListCreateAPIView,
    PostDetailAPIView, 
    PostUpdateAPIView,
    PostDeleteAPIView
)


app_name = 'blog'

urlpatterns = [
    path('post', PostListCreateAPIView.as_view(), name="posts-list"),
    path('post/<str:pk>', PostDetailAPIView.as_view(), name="post-detail"),
    path('post/update/<str:pk>', PostUpdateAPIView.as_view(), name="post-update"),
    path('post/delete/<str:pk>', PostDeleteAPIView.as_view(), name="post-delete"),
]