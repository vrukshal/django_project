from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, CreateView

from posts.forms import PostForm
from .models import Post
from django.urls import reverse_lazy


class HomePageView(ListView):
    model = Post
    template_name = "home.html"
# We use the generic class-based ListView here, 
# import our Post model, and then create a HomePageView that uses 
# the model and a template called home.html.






class CreatePostView(CreateView):  # name our new view CreatePostView 
    #which will extend the built-in Django CreateView. 
    model = Post
    form_class = PostForm
    template_name = "post.html"
    success_url = reverse_lazy("home")
    # We'll also import reverse_lazy to handle the redirect back to our homepage after the form has been submitted.

    # Within the view we specify the model, a form_class which we'll create next, the template_name, 
    # and finally a success_url which is what we want to happen after submission.