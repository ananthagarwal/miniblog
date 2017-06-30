from django.shortcuts import render
from .models import Blog, BlogAuthor, Comment
from django.views import generic


# Create your views here.

def index(request):
    """
    View function for home page of site.
    """
    num_blogs = Blog.objects.all().count()
    num_authors = BlogAuthor.objects.all().count()
    num_unique_authors = Blog.objects.distinct().count()
    num_comments = Comment.objects.all().count()
    return render(request, 'index.html', context={'num_blogs' : num_blogs, 'num_authors' : num_authors,
                                                  'num_unique_authors' : num_unique_authors, 'num_comments' : num_comments})


class BlogListView(generic.ListView):
    model = Blog
    context_object_name = 'blog_list'
    template_name = 'blog_list.html'

class BlogDetailView(generic.DetailView):
    model = Blog
    context_object_name = "blog_detail"
    template_name = "blog_detail.html"
