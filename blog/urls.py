from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)
from . import views

urlpatterns = [
    # Blog post views
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('search/', views.search, name='search'),
    path('about/', views.about, name='blog-about'),

    # Room feature URLs
    path('room/create/', views.create_room, name='create-room'),
    path('room/join/', views.join_room, name='join-room'),
    path('room/<str:room_id>/', views.room_detail, name='room-detail'),
    path('room/<str:room_id>/upload/', views.upload_file, name='upload-file'),
    path('your-rooms/', views.user_rooms, name='your-rooms'),
]
