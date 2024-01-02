from django.urls import path

from .views import CreatePostView, HomePageView, index
from posts import views

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    # put all posts on the homepage so 
    # again use the empty string "" as our route path.

    path("post/", CreatePostView.as_view(), name="add_post"),
    # We'll make a dedicated page for this form at the path of post/.
    path("fw/", views.index,name="fw"),   
]