import pkgutil
from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils import timezone
from .models import User, Userdate

class IndexView(TemplateView):
    def get(self, request, *args, **kwargs):
        users = User.objects.order_by('-id')
        return render(request, 'registration/index.html', {
            'users':users
        })

class ShowView(TemplateView):
     def get(self, request, *args, **kwargs):
        datas = Userdate.objects.order_by('-id')
        return render(request, 'registration/show.html', {
            'datas':datas
        })

class CreateView(TemplateView):
    template_name = "create.html"

class EditView(TemplateView):
    template_name = "edit.html"