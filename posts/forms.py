from django import forms
from .models import Post
from django.forms.widgets import NumberInput
import datetime

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ["title", "cover"]

# we extend Django's built-in ModelForm. 
# All we need for our basic form is to specify the 
# correct model Post and the fields we want displayed which are title and cover.

BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]


class FormWid(forms.Form):
    firstname = forms.CharField(label="Enter first name",max_length=50)  
    comment = forms.CharField(widget=forms.Textarea)
    comment1 = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    email = forms.EmailField()
    agree = forms.BooleanField()
    agree1 = forms.BooleanField(initial=True)
    date = forms.DateField()
    birth_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    numbervalue = forms.DecimalField()
    email_address1 = forms.EmailField(required = False,)
    first_name1 = forms.CharField(initial='Your name')
    day = forms.DateField(initial=datetime.date.today)
    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
    favorite_color1=forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES)
    favorite_colors2 = forms.MultipleChoiceField(choices=FAVORITE_COLORS_CHOICES)
    favorite_colors3=forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=FAVORITE_COLORS_CHOICES,)
    




