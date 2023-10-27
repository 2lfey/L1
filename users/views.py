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


class ProfileView(mixins.LoginRequiredMixin, generic.DetailView):
    model = models.User
    template_name = 'registration/profile.html'
    context_object_name = 'user'

    def get_object(self, queryset=None):
        return self.request.user
