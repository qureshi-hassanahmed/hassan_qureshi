from django.forms import ModelForm, TextInput, EmailInput, Textarea
from .models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'}),
            'notes': Textarea(attrs={'class': 'form-control', 'rows': 4, 'id': 'comment'}),
        }
