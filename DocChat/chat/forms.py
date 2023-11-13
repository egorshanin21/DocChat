from django import forms
from django.forms import FileInput

from .models import UserFile


class UserFileForm(forms.ModelForm):
    # pdf_document = forms.FileField(label='Upload a PDF', required=True,
    #                                widget=FileInput({'class': "form-control"}))
    class Meta:
        model = UserFile
        fields = ['file']

class SendMessageForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea)