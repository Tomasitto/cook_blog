
from django.views.generic import ListView, DetailView
from django.shortcuts import render

from blog.models import Post


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(categoty__slug=self.kwargs.get('slug')).select_related('categoty')
    

class PostDetailView(DetailView):
    model = Post
    context_object_name: str = 'post'
    slug_url_kwarg = 'post_slug'

    

def home(request):
    return render(request, 'index.html')