from django.urls import path
from . import views
from .views import PostListElement, PostDetailElement, PostCreateElement, PostUpdateElement, PostDeleteElement, UserPostListElement

urlpatterns = [
    path('', PostListElement.as_view(), name='diary-home'),
    path('post/<int:pk>/', PostDetailElement.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateElement.as_view(), name='post-update'),
    path('post/new/', PostDetailElement.as_view(), name='post-create'),
    path('post/<int:pk>/delete/', PostDeleteElement.as_view(), name='post-delete'),
    path('about/', views.about, name='diary-about'),
    path('user/<str:username>', UserPostListElement.as_view(), name='user-posts'),
]



