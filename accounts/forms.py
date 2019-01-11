from django.contrib.auth import get_user_model
from django import forms

class RForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput) #widget비번*로 보이는것같은거
    password2 = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model=get_user_model()
        fields = ('username', 'first_name', 'last_name', 'email')
        def clean_password2(self):
            cd = self.clean_data
            if cd['password'] != cd['password2'] :
                raise forms.ValidationError("password doesn't match. ")

            return cd['password2']