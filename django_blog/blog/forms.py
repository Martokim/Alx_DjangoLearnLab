from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Comment , Post
from taggit.forms import TagWidget 

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author_name', 'content']  # <- use "content", not "text"

    # Example validation for content
    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) < 5:
            raise forms.ValidationError("Comment must be at least 5 characters long.")
        return content

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title","content","tags"]
        widgets = {
            "tags": TagWiget(),
        }