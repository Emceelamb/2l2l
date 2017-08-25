from django import forms
from .models import Sorry

class customTitle(forms.CharField):
    def to_python(self, value):
        return value.lower()

class SorryForm(forms.ModelForm):
    title = customTitle(max_length=20, label='')
    text = forms.CharField(widget=forms.Textarea, label='')
    class Meta:
        model = Sorry
        fields = ('title','text',)
