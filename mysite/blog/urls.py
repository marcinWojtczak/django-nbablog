from django.urls import path
from . import views


urlpatterns = [
    
    path('', views.PostListView.as_view(), name='home-page'),
    path('post/search/', views.post_search_view, name='post-search'),
    path('user/<str:username>/', views.UserPostListView.as_view(), name='user-posts'),
    #path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/<slug:slug>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/comment/', views.PostCommentView.as_view(), name='post-comment'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about_page, name='about-page')
    
]
