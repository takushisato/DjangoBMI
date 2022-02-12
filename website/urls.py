# from unicodedata import name
from django.urls import path
from .views import IndexView, ShowView, CreateView, EditView

urlpatterns = [
    path('', IndexView.as_view(), name="registration/index"),
    path('show/<int:pk>/', ShowView.as_view(), name="show"),
    path('new/', CreateView.as_view(), name="new"),
    path('edit/', EditView.as_view(), name="edit"),
]
