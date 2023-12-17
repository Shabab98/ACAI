# home/urls.py
from django.urls import path
from home.views import LibraryListView, UserListView

urlpatterns = [
    path('library/', LibraryListView.as_view(), name='library_list'),
    path('user/', UserListView.as_view(), name='user_list'),
    # Add more URLs as needed
]