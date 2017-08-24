from django import forms
from .models import Sorry
class SorryForm(forms.ModelForm):
    title = forms.CharField(max_length=30, label='')
    text = forms.CharField(widget=forms.Textarea, label='')
    class Meta:
        model = Sorry
        fields = ('title','text',)
