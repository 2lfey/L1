from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import mixins

from . import models
from . import forms


class RegisterView(generic.CreateView):
    model = models.User
    form_class = forms.RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class ProfileView(mixins.LoginRequiredMixin, generic.edit.UpdateView):
    model = models.User
    template_name = 'registration/profile.html'
    success_url = reverse_lazy('profile')
    fields = (
        'avatar',
        'email',
        'username',
    )

    def get_object(self, queryset=None):
        return self.request.user