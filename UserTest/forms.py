from django import forms

STATES = (
    ('', 'Choose...'),
    ('MG', 'Minas Gerais'),
    ('SP', 'Sao Paulo'),
    ('RJ', 'Rio de Janeiro')
)
class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput())

class RegisterForm(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Name'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    agree = forms.BooleanField(required=False)
    def clean(self):
        name=self.cleaned_data.get('name')
        email=self.cleaned_data.get('email')
        password=self.cleaned_data.get('password')
        confirm_password=self.cleaned_data.get('confirm_password')
        agree=self.cleaned_data.get('agree')
        if password and confirm_password and password!=confirm_password:
            raise forms.ValidationError("Passwords don't match")

        values={
            'name':name,
            'email':email,
            'password':password,
            'agree':agree,
        }
        return  values