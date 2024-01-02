from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from postfile.forms import Postf
from .models import PostFile1
from django.urls import reverse_lazy


class HomePageView1(ListView):
    model = PostFile1
    template_name = "postfilet.html"
# We use the generic class-based ListView here, 
# import our Post model, and then create a HomePageView that uses 
# the model and a template called home.html.

