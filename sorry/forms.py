from django import forms
from .models import Sorry

# Dropdown RELATIONSHIP
# RELATIONSHIP = (
#     ('EXL', 'Ex-Lover'),
#     ('FAM', 'Family'),
#     ('SOT', 'Significant Other'),
#     ('FRI', 'Friend'),
#     ('COW', 'Co-Worker'),
#     ('STG', 'Stranger'),
#
# )
RELATIONSHIP = (
    ('Lover', 'Lover'),
    ('Ex-Lover', 'Ex-Lover'),
    ('Family', 'Family'),
    ('Friend', 'Friend'),
    ('Enemy', 'Enemy'),
    ('Co-Worker', 'Co-Worker'),
    ('Stranger', 'Stranger'),

)



class customTitle(forms.CharField):
    def to_python(self, value):
        return value.lower()

class SorryForm(forms.ModelForm):
    title = customTitle(max_length=20, label='')
    relationship=forms.ChoiceField(choices=RELATIONSHIP, required=True)
    text = forms.CharField(widget=forms.Textarea, label='')
    class Meta:
        model = Sorry
        fields = ('title','relationship','text',)
