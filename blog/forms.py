from django import forms
from blog.models import Post, Comment
from ckeditor.fields import RichTextFormField

class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('author','title','text','image')

        widget = {
            'title':forms.TextInput(attrs={'class': 'form-control','placeholder':'Post Title'}),
            'text': RichTextFormField(),
            'image':forms.FileInput(attrs={'class':'custom-file-input'}),
        }



class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('author','text')


        widget = {
        'author':forms.TextInput(attrs={'class': 'form-control','placeholder':'Your Name'}),
        'text': RichTextFormField()
        }
