from django.shortcuts import render, get_object_or_404
from . models import Post, Comment
from . forms import CommentForm
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User



class PostListView(ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = "posts_list"
    ordering = ['-published']
    paginate_by = 2


class UserPostListView(ListView):
    model = Post
    template_name = "blog/user_posts.html"
    context_object_name = "posts_list"      # object by default
    paginate_by = 2   

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-published')


class PostDetailView(DetailView):
    model = Post
    fields = ['title', 'content']
    


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    

    # currend loggin user is author of the post
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostCommentView(CreateView):
    model = Comment
    form_class = CommentForm  # when you import form you don't need use fields
    template_name = 'blog/add_comment.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    
    success_url = '/'


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    # current loggin user is author of the post
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # only owner can update post
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    # only owner can delete post
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    




def about_page(request):
    return render(request, "blog/about.html")



