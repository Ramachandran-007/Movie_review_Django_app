from django import forms
from .models import RegisterModel

class RegisterForm(forms.ModelForm):
    re_enter_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = RegisterModel
        fields = ['first_name','last_name','username','email','phone_no','password','re_enter_password']

        widgets = {'first_name':forms.TextInput,
                   'last_name':forms.TextInput,
                   'username':forms.TextInput,
                   'email':forms.EmailInput,
                   'phone_no':forms.NumberInput,
                   'password':forms.PasswordInput
                   }

    def clean(self):
        password = self.cleaned_data['password']
        re_enter = self.cleaned_data['re_enter_password']

        if password != re_enter:
            raise forms.ValidationError('Password and re-enter password are not matching')