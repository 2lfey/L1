from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from . import models

class RegisterForm(UserCreationForm):
    class Meta():
        model = models.User
        fields = (
            'username',
            'avatar',
            'password1',
            'password2',
        )

    def clean(self):
        super().clean()

        avatar = self.files.get('avatar')

        if avatar is not None:
            self.cleaned_data['avatar'] = avatar
        else:
            raise ValidationError('Avatar required', code='noavatar')

        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password and password2 and password != password2:
            raise ValidationError({
                'password2': ValidationError('Passwords mismatch', code='password_mismatch')
            })

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.avatar = self.cleaned_data['avatar']

        if commit:
            user.save()

        return user
    

# QWEasd12345