from django import forms
from django.forms import FileInput

from .models import UserFile


class UserFileForm(forms.ModelForm):
    """
    Form for handling UserFile model data.
    """
    # pdf_document = forms.FileField(label='Upload a PDF', required=True,
    #                                widget=FileInput({'class': "form-control"}))
    class Meta:
        """
        Meta class specifying the model and its fields for the form.
        """
        model = UserFile
        fields = ['file']


class SendMessageForm(forms.Form):
    """
    Form for sending messages.
    """
    message = forms.CharField(widget=forms.Textarea)
