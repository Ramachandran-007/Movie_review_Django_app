from django import forms
from .models import MovieModel, CommentModel

class MovieForm(forms.ModelForm):
    class Meta:
        model = MovieModel
        fields = '__all__'

        widgets = {'release_date':forms.DateInput(attrs={'type':'date'}),'reviewed_on':forms.DateInput(attrs={'type':'date'})}

class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = '__all__'
        widgets = {'movie':forms.HiddenInput,'comment_date':forms.DateInput(attrs={'type':'date'}),'user':forms.HiddenInput}