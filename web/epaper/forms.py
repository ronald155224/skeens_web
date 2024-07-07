from django import forms
from epaper.models import EPaperEmail, GuestMessage

class EPaperForm(forms.ModelForm):
    class Meta:
        model = EPaperEmail
        fields = ('email',)

class GuestForm(forms.ModelForm):
    class Meta:
        model = GuestMessage
        fields = ('name', 'email', 'subject', 'message')