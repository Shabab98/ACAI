from django.shortcuts import render

# Create your views here.
# home/views.py
# home/views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from home.models import Library, UserProfile

class LibraryListView(LoginRequiredMixin, ListView):
    model = Library
    template_name = 'home/library_list.html'

    def get_queryset(self):
        return Library.objects.all()

class UserListView(LoginRequiredMixin, ListView):
    model = UserProfile
    template_name = 'home/user_list.html'

    def get_queryset(self):
        return UserProfile.objects.filter(role='user')