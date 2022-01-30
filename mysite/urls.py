"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from website.views import IndexView, ShowView, CreateView, EditView

IndexView = TemplateView.as_view(template_name="registration/index.html")
ShowView = TemplateView.as_view(template_name="registration/show.html")
CreateView = TemplateView.as_view(template_name="registration/create.html")
EditView = TemplateView.as_view(template_name="registration/edit.html")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_required(IndexView)),
    path('show/<int:pk>/', login_required(ShowView)),
    path('create/', login_required(CreateView)),
    path('edit/', login_required(EditView)),
    path('', include("django.contrib.auth.urls")),
]
