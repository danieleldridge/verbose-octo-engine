from django.forms import ModelForm, Textarea
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from moodjournal.models import JournalEntry


class JournalForm(ModelForm):
    class Meta:
        model = JournalEntry
        fields = ['mood_entry', 'mood_rating']
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save Entry'))
