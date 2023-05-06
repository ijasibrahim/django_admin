from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'phone' , 'subject','message']


from .models import Picture
class PictureForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ('title', 'image')
