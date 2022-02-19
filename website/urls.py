# from unicodedata import name
from django.urls import path
from .views import IndexView, ShowView, CreateView, EditView, DeleteView, UserCreateView

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('show/<int:pk>/', ShowView.as_view(), name="show"),
    path('new/', CreateView.as_view(), name="new"),
    path('<int:pk>/edit', EditView.as_view(), name="edit"),
    path('<int:pk>/delete', DeleteView.as_view(), name="delete"),
    path('usernew/', UserCreateView.as_view(), name="usernew"),
]
