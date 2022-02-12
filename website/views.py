from distutils.command.clean import clean
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Userdate
from django.contrib.auth.models import User
from .forms import UserdateForm

class IndexView(TemplateView):
    def get(self, request, *args, **kwargs):
        userdates = Userdate.objects.all()
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
    template_name = "edit.html"