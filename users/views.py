from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import generic

from . import models
from . import forms

class RegisterView(generic.CreateView):
    model = User
    form_class = forms.RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

from django.urls import reverse_lazy
from django.contrib.auth import views, mixins
from django.views import generic

from .models import User

# from .forms import ChangePasswordForm, RegisterForm, LoginForm, UpdateProfileForm


class ProfileView(mixins.LoginRequiredMixin, generic.DetailView):
    model = User
    template_name = 'registration/profile.html'
    context_object_name = 'user'

    def get_object(self, queryset=None):
        return self.request.user


# class UpdateProfileView(mixins.LoginRequiredMixin, generic.UpdateView):
#     model = User
#     form_class = UpdateProfileForm
#     template_name = 'users/update_profile.html'

#     def get_success_url(self) -> str:
#         return reverse_lazy('users:profile', kwargs={
#             "pk": self.request.user.pk
#         })


# class ChangePasswordView(mixins.LoginRequiredMixin, views.PasswordChangeView):
#     template_name = 'users/change_password.html'
#     form_class = ChangePasswordForm
#     success_url = reverse_lazy('users:password_change_done')


# class ChangePasswordDoneView(views.PasswordChangeDoneView):
#     template_name = 'users/change_password_done.html'


# class LogoutUserView(mixins.LoginRequiredMixin, views.LogoutView):
#     template_name = 'users/logout.html'
#     success_url = reverse_lazy('users:login')


# class RegisterUserView(generic.CreateView):
#     model = User
#     form_class = RegisterForm
#     template_name = "users/register.html"
#     success_url = reverse_lazy('users:login')