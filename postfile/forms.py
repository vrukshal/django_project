from django import forms
from .models import PostFile1

class Postf(forms.ModelForm):

    class Meta:
        model = PostFile1
        fields = ["title", "cover"]

# we extend Django's built-in ModelForm. 
# All we need for our basic form is to specify the 
# correct model Post and the fields we want displayed which are title and cover.