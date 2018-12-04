from django.db import models
from django.utils import timezone
import datetime


class JournalEntry(models.Model):
    MOOD_RATINGS = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
    )
    mood_entry = models.CharField(max_length=400)
    mood_rating = models.CharField(max_length=1, choices=MOOD_RATINGS)
    mood_date = models.DateField()

    class Meta:
        ordering = ["-mood_date"]

    #def __str__(self):
    #    "Identifies an entry by its date"
    #    return 'Mood for %s = %s' % (self.mood_date, self.mood_rating)



