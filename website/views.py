from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Userdate
from django.contrib.auth.models import User

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
    template_name = "create.html"

class EditView(TemplateView):
    template_name = "edit.html"