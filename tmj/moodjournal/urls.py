from django.urls import path, include
from . import views
from django.contrib import admin
from django.views.generic.base import TemplateView

from moodjournal.views import JournalList

urlpatterns = [
    
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('submit/', views.index, name='submit'),
    path('view/', JournalList.as_view()),
    path('about/', views.about, name="about"),
    


]
