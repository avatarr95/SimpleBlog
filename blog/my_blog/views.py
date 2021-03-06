from django.shortcuts import render
from django.views import generic
from .models import Post


class IndexView(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status='published')
    context_object_name = "posts"
    template_name = "my_blog/index.html"
    paginate_by = 2


def post_detail_view(request, pk, post):
    post = Post.objects.get(pk=pk, slug=post)
    return render(request, "my_blog/post_detail.html", {'post': post})
