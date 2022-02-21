from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from .models import Information
from .forms import SignupForm
from django.views.generic import RedirectView
from django.contrib.auth import logout
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.


@method_decorator(login_required, name='dispatch')
class StudentCreateView(CreateView):
    model = Information
    template_name = 'app/home.html'
    fields = ['name', 'age', 'course']
    success_url = '/home/'


@method_decorator(staff_member_required, name='dispatch')
class StudentListView(ListView):
    model = Information
    template_name = 'app/show.html'
    context_object_name = 'students'


class StudentUpdateView(UpdateView):
    model = Information
    template_name = 'app/update.html'
    fields = ['name', 'age', 'course']
    success_url = '/show/'


class StudentDeleteView(DeleteView):
    model = Information
    success_url = '/show/'


class SignupCreateView(FormView):
    form_class = SignupForm
    template_name = 'app/signup.html'
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super(SignupCreateView, self).form_valid(form=form)


class Logout(RedirectView):
    url = '/login/'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(Logout, self).get(request, *args, **kwargs)
