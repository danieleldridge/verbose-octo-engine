from django.test import TestCase
from .models import JournalEntry
from django.urls import reverse
import datetime

# Create your tests here.

class EntryTests(TestCase):

    def setUp(self):
        JournalEntry.objects.create(
        mood_entry="Today I'm feeling testy!",
        mood_rating="4",
        mood_date=datetime.date.today(),
        )

    def test_entry_content(self):
        entry=JournalEntry.objects.get(id=1)
        expected_object_name=f'{entry.mood_entry}'
        self.assertEquals(expected_object_name, "Today I'm feeling testy!")

    # def test_entry_view(self):
    #     response=self.client.get(reverse('view'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, "Today I'm feeling testy!")
    #     self.assertTemplateUsed(response, 'journalentry_list.html')
