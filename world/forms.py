from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import DogProfile


# Create your forms here.

class NewUser(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUser, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class NewDog(forms.ModelForm):
    name = forms.CharField(required=True)
    dogimg = forms.ImageField

    class Meta:
        model = DogProfile
        labels = {
            "dogimg": "Your dog's profile picture:"
        }
        fields = ("name", "dogimg")

