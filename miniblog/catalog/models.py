from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.


class Blog(models.Model):
    """
    Model representing a Blog.
    """
    title = models.CharField(max_length=200)
    author = models.ForeignKey('BlogAuthor', on_delete=models.SET_NULL, null=True)
    post = models.TextField(max_length=1000, help_text="Write your post here")
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        """
        String for representing Model object.
        """
        return self.title

    def get_absolute_url(self):
        """
        Returns the url to access a particular Blog instance.
        """
        return reverse('blog-detail', args=[str(self.id)])


class Comment(models.Model):
    """
    Model representing a Blog Comment
    """
    blog = models.ForeignKey(Blog, on_delete=models.SET_NULL, null=True)
    comment_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=1000, help_text="Write your comment here")
    comment_author = models.ForeignKey('BlogAuthor', on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ["comment_date"]


    def __str__(self):
        """
        String for representing Model object.
        """
        return self.description[:25] + " ..."


class BlogAuthor(models.Model):
    """
    Model representing a Blog Author
    """
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    bio = models.TextField(max_length=1000, help_text="Enter your bio here")

    def __str__(self):
        """
        String for representing Model object.
        """
        return self.user.__str__()

    def get_absolute_url(self):
        """
        Returns the url to access a particular BlogAuthor instance.
        """
        return reverse('blog-author-detail', args=[str(self.id)])