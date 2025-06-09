from django import forms
from .models import Help

class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Help
        fields = ['name', 'phone', 'email', 'help_text']
        labels = {
            'name': 'Імʼя',
            'phone': 'Телефон',
            'email': 'Email',
            'help_text': 'Допомога',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'help_text': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

    def clean(self):
        cleaned_data = super().clean()
        phone = cleaned_data.get('phone')
        email = cleaned_data.get('email')
        if not phone and not email:
            self.add_error(None, 'Вкажіть хоча б телефон або email для звʼязку.')
        return cleaned_data
