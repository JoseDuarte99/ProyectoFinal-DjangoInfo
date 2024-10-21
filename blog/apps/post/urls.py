from django.urls import path
from .views import *

app_name = 'apps.posts'

urlpatterns = [
    path('', PostListView.as_view(), name='posts'),
    path('<int:id>/', PostDetailView.as_view(), name='post_individual'),
    path('CreatePost/', PostCreateView.as_view(), name='posts_create'),
    path('UpdatePost/<int:id>/', PostUpdateView.as_view(), name='post_update'),
    path('DeletePost/<int:id>/', PostDeleteView.as_view(), name='post_delete'),
    path('category/', CategoryListView.as_view(), name='category'),

    path('category/<int:pk>/posts/',
         PostCategoryView.as_view(), name='post_category'),
    
    path('category_create', CategoryCreateView.as_view(), name='category-create'),

    path('category_delete/<int:pk>/',
         CategoryDeleteView.as_view(), name='category_delete'),

    path('comments/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),

]
