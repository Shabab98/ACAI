from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from home.models import Library, UserProfile

class LibraryListView(LoginRequiredMixin, ListView):
    model = Library
    template_name = 'home/library_list.html'

    def get_queryset(self):
        return Library.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Library List'
        return context

class UserListView(LoginRequiredMixin, ListView):
    model = UserProfile
    template_name = 'home/user_list.html'

    def get_queryset(self):
        return UserProfile.objects.filter(role='user')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'User List'
        return context
