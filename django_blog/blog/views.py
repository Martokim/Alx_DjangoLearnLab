from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = '/'
