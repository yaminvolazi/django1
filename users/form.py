from  django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','telephone','email']

    def clean_email(self):
        email=self.cleaned_data.get('email')
        #if not "volazi" in email:
            #raise forms.ValidationError("Please enter .volazi domain")
        return email