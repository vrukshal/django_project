from django.urls import path

from .views import HomePageView1

urlpatterns = [
    path("postf/", HomePageView1.as_view(), name="home1"),
    # put all posts on the homepage so 
    # again use the empty string "" as our route path.

    #path("post/", CreatePostView.as_view(), name="add_post")
    # We'll make a dedicated page for this form at the path of post/.
    
]