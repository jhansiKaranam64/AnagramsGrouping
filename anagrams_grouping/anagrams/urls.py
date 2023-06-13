from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('group-anagrams/', views.group_anagrams, name='group_anagrams'),
]
