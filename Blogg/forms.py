from django import  forms
from .models import Post
from django.contrib.auth.forms import UserCreationForm

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        exclude = ['profile']
        fields ='__all__'
       

class CustomUserCreationForm(UserCreationForm):

   # class Meta:
       # fields = ['username','email','password1','password2']

   
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)



