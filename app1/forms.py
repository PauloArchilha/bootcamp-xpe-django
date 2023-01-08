from django import forms
from .models import User

# modelForm


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['nome', 'telefone', 'email']

# form.form
