from django import forms

from main import models

class ReviewForm(forms.Form):
  title = forms.CharField(max_length = 256)
  body = forms.CharField(widget = forms.Textarea())
  stars = forms.IntegerField(max_value = 5, min_value = 0)

class ReviewModelForm(forms.ModelForm):
  class Meta:
    model = models.Review
    fields = ['title', 'body', 'stars']
    # fields = '__all__'
    # exclude = ['user', 'restaurant']
  
