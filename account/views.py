from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.core.urlresolvers import reverse_lazy
from django.views.generic import FormView, RedirectView

from .forms import LoginForm


class UserLoginView(FormView):
    form_class = LoginForm
    template_name = 'account/login.html'
    success_url = reverse_lazy('shop:home')

    def get_context_data(self, **kwargs):
        context = super(UserLoginView, self).get_context_data(**kwargs)
        context['next'] = self.request.GET.get('next', None)
        return context

    def get_success_url(self):
        next_url = self.request.GET.get('next', None)
        return next_url or reverse('shop:home')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return super(UserLoginView, self).form_valid(form)

    def form_invalid(self, form):
        return super(UserLoginView, self).form_invalid(form)


class UserLogoutView(RedirectView):
    permanent = False
    pattern_name = 'account:user_login'

    def get_redirect_url(self, *args, **kwargs):
        logout(self.request)
        messages.success(self.request, 'You are successfully logged out!')
        return super(UserLogoutView, self).get_redirect_url(*args, **kwargs)
