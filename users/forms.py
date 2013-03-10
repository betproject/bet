from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from users.models import Userbet

class RegistrationForm(ModelForm):
        username        = forms.CharField(label=(u'User Name'))
        email           = forms.EmailField(label=(u'Email Address'))
        password        = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))
        password1       = forms.CharField(label=(u'Verify Password'), widget=forms.PasswordInput(render_value=False))
        birthday        = forms.DateField(label=(u'Date of Birth'), input_formats=['%d/%m/%Y'], required=True, widget = forms.DateInput(format = '%d/%m/%Y'))
        first_name      = forms.CharField(label=(u'First Name'))

        def __init__(self, *args, **kwargs):
                super(RegistrationForm, self).__init__(*args, **kwargs)
                self.fields['birthday'].localize = False
                self.fields['birthday'].widget.is_localized = False

        class Meta:
                model = Userbet
                exclude = ('user',)

        def clean_username(self):
                username = self.cleaned_data['username']
                try:
                        User.objects.get(username=username)
                except User.DoesNotExist:
                        return username
                raise forms.ValidationError("That username is already taken, please select another.")

        def clean(self):
                password = self.cleaned_data['password']
                password1 = self.cleaned_data['password1']
                if password and password1 and password != password1:
                        raise forms.ValidationError("The passwords did not match.  Please try again.")

                return self.cleaned_data
		

class LoginForm(forms.Form):
        username        = forms.CharField(label=(u'User Name'))
        password        = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))
                