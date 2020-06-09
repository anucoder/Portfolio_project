from django import forms
from projects.models import Message


# class ContactForm(forms.Form):
#     name = forms.CharField()
#     email = forms.EmailField()
#     message = forms.CharField(widget=forms.Textarea(attrs={"rows":2, "cols":20}))

class ContactForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
