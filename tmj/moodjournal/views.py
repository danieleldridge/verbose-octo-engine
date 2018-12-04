from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from moodjournal.models import JournalEntry
from django.views import View
from django.views.generic import ListView
from django.contrib.auth.forms import UserCreationForm

from moodjournal.forms import JournalForm
import datetime


def index(request):
    if request.method == 'POST':
        form = JournalForm(request.POST)
        if form.is_valid():
            mood_entry = form.cleaned_data['mood_entry']
            mood_rating = form.cleaned_data['mood_rating']
            mood_date = datetime.datetime.now()
            j = JournalEntry(mood_entry=mood_entry, mood_rating=mood_rating, mood_date=mood_date)
            j.save()
            return HttpResponseRedirect('/moodjournal/view/')
    else:
        form = JournalForm()
    return render(request, 'moodjournal/index.html', {'form': form})


def about(request):
    return render(request, 'moodjournal/about.html')


class JournalList(ListView):
    model = JournalEntry


def register(request):
    pass
