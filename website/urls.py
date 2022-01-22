from unicodedata import name
from django.urls import path
from .views import IndexView, ShowView, CreateView, EditView

urlpatterns = [
    path('', IndexView.as_view()),
    path('show/<int:pk>/', ShowView.as_view(), name="show"),
    path('create/', CreateView.as_view(), name="create"),
    path('edit/', EditView.as_view(), name="edit"),
]
