from django import forms

from runkansas.profiles.models import Profile



class ProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        exclude = [
            "user",
            "races",
        ]
