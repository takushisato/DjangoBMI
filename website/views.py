from distutils.command.clean import clean
import email
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Userdate
from django.contrib.auth.models import User
from .forms import UserdateForm, UserForm
 
class IndexView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        userdates = Userdate.objects.order_by('created_date').reverse()
        return render(request, 'registration/index.html', {
            'userdates':userdates
        })

class ShowView(TemplateView):
    def get(self, request, *args, **kwargs):
        userdates = Userdate.objects.get(id=self.kwargs['pk'])
        return render(request, 'registration/show.html', {
            'userdates':userdates
        })

class CreateView(TemplateView):
    def get(self, request, *args, **kwargs):
        form = UserdateForm(request.POST or None)
        return render(request, 'registration/create.html', {
            'form': form
        })

    def post(self, request, *args, **kwargs):
        form = UserdateForm(request.POST or None)

        if form.is_valid():
            userdate = Userdate()
            userdate.user = request.user
            userdate.height = form.cleaned_data['height']
            userdate.weight = form.cleaned_data['weight']
            userdate.save()
            return redirect('show', userdate.id)

        return render(request, 'registration/create.html', {
            'form': form
        })

class EditView(TemplateView):
    def get(self, request, *args, **kwargs):
        userdates = Userdate.objects.get(id=self.kwargs['pk'])
        form = UserdateForm(
            request.POST or None,
            initial = {
                'height': userdates.height,
                'weight': userdates.weight,
            }
        )

        return render(request, 'registration/edit.html', {
            'form': form
        })
    
    def post(self, request, *args, **kwargs):
        form = UserdateForm(request.POST or None)

        if form.is_valid():
            userdate = Userdate.objects.get(id=self.kwargs['pk'])
            userdate.height = form.cleaned_data['height']
            userdate.weight = form.cleaned_data['weight']
            userdate.save()
            return redirect('show', self.kwargs['pk'])

        return render(request, 'registration/create.html', {
            'form': form
        })

class DeleteView(TemplateView):
    def get(self, request, *args, **kwargs):
        userdates = Userdate.objects.get(id=self.kwargs['pk'])
        return render(request, 'registration/delete.html', {
            'userdates': userdates
        })

    def post(self, request, *args, **kwargs):
        userdates = Userdate.objects.get(id=self.kwargs['pk'])
        userdates.delete()
        return redirect('index')

class UserCreateView(TemplateView):
    def get(self, request, *args, **kwargs):
        form = UserForm(request.POST or None)
        return render(request, 'usercreate.html', {
            'form': form
        })
    
    def post(self, request, *args, **kwargs):
        form = UserForm(request.POST or None)

        if form.is_valid():
            user = User()
            user.username = form.cleaned_data['username']
            user.email = form.cleaned_data['email']
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('usercompleted')

        return redirect('error')

class UserCompletedView(TemplateView):
    template_name = "usercompleted.html"


class UserCreateErrorView(TemplateView):
    template_name = "error.html"

class UserDeleteView(TemplateView):
    def get(self, request, *args, **kwargs):
        user = User.objects.get(username = request.user) 
        return render(request, 'registration/userdelete.html', {
            'user': user
        })

    def post(self, request, *args, **kwargs):
        user = User.objects.get(username = request.user)
        user.delete()
        return redirect('index')