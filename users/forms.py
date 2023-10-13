from django.contrib.auth.forms import UserCreationForm


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

    def clean_avatar(self):
        avatar = self.cleaned_data['avatar']
        if avatar:
            return avatar


    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.avatar = self.cleaned_data['avatar']

        if commit:
            user.save()

        return user
    

# QWEasd12345