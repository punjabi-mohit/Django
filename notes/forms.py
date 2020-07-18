from django import forms
from notes.models import Notes

class NotesForm(forms.ModelForm):
    body=forms.CharField()
    label=forms.CharField()
    class Meta:
        model=Notes
        fields=['label','body']
    