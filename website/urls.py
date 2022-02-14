# from unicodedata import name
from django.urls import path
from .views import IndexView, ShowView, CreateView, EditView, DeleteView

urlpatterns = [
    path('', IndexView.as_view(), name="registration/index"),
    path('show/<int:pk>/', ShowView.as_view(), name="show"),
    path('new/', CreateView.as_view(), name="new"),
    path('<int:pk>/edit', EditView.as_view(), name="edit"),
    path('<int:pk>/delete', DeleteView.as_view(), name="delete"),
    
]
