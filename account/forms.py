from django import forms
from django.contrib.auth import authenticate


from .models import Myuser


class UserCreationForm(forms.ModelForm):

    class Meta:
        Model = Myuser
        fields = ['username', 'first_name', 'last_name', 'email', 'mobile', 'is_active']

        def save(self, commit=True):
            instance = super(UserCreationForm, self).save(commit=False)
            instance.role = 'user'
            if self.cleaned_data.get('password'):
                instance.set_password(self.cleaned_data['password'])
            if commit:
                instance.save()
            return instance


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean(self, *args, **kwargs):
        cleaned_data = super(LoginForm, self).clean()
        username = cleaned_data.get('username', None)
        password = cleaned_data.get('password', None)
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                msg = 'Username or password is invalid'
                self._errors['username'] = self.error_class([msg])
                del cleaned_data['username']
                del cleaned_data['password']
            elif not user.is_active:
                msg = 'Your account is not activated. Please contact administratior.'
                self._errors['username'] = self.error_class([msg])
                del cleaned_data['username']
                del cleaned_data['password']
        return cleaned_data
