from django.shortcuts import render, get_object_or_404
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListElement, DeatilElement, CreateElement, UpdateElement, DeleteElement
from django.contrib.auth.models import User

def home(request):
    content = {
        'posts': Post.objects.all()
    }
    return render(request, 'diary/home.html', content)

class PostListElement(ListElement):
    model = Post
    template_name = 'diary/home.html'
    content_object = 'posts'
    order = ['-date_posted']
    paginate_by = 10

class UserPostListElement(ListElement):
    model = Post
    template_name = 'diary/user_post.html'
    content_object = 'posts'
    paginate_by = 10

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailElement(DeatilElement):
    model = Post

class PostCreateElement(LoginRequiredMixin, UserPassesTestMixin, CreateElement):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostUpdateElement(LoginRequiredMixin, UserPassesTestMixin, UpdateElement):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostDeleteElement(LoginRequiredMixin, UserPassesTestMixin, DeleteElement):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'diary/about.html', {'title': 'About'})   

