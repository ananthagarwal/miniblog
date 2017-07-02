from django.shortcuts import render
from .models import Blog, BlogAuthor, Comment
from django.views import generic
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

from .forms import AddCommentForm

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
    paginate_by = 5

class BlogDetailView(generic.DetailView):
    model = Blog
    context_object_name = 'blog_detail'

class BlogAuthorListView(generic.ListView):
    model = BlogAuthor
    context_object_name = 'blog_author_list'


class BlogAuthorDetailView(generic.DetailView):
    model = BlogAuthor
    context_object_name = 'blog_author_detail'

@login_required
def add_comment(request, pk):
    blog_inst=get_object_or_404(Blog, pk = pk)
    print(pk)
    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = AddCommentForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            blog_inst.comment_set.add(Comment.objects.create(blog = blog_inst, comment_date = form.cleaned_data['time'], description = form.cleaned_data['description'], comment_author =
            BlogAuthor.objects.get(user = request.user) ))
            blog_inst.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('blog-detail', args=[str(blog_inst.id)]) )

    # If this is a GET (or any other method) create the default form.
    else:
        description = 'Empty comment'
        form = AddCommentForm(initial={'description': description,})

    return render(request, 'catalog/addcomment.html', {'form': form, 'bloginst': blog_inst})