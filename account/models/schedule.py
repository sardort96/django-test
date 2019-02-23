from django.db import models
from django.db.models import PROTECT


class Schedule(models.Model):
    BREAKFAST = 'breakfast'
    LUNCH = 'lunch'
    DINNER = 'dinner'

    TYPES = (
        (BREAKFAST, 'Breakfast'),
        (LUNCH, 'Lunch'),
        (DINNER, 'Dinner'),
    )

    HUFFMAN = 'huffman'
    STAYLER = 'stayler'
    CURTIES = 'curties'

    DINING_HALLS = (
        (HUFFMAN, 'Huffman'),
        (STAYLER, 'Stayler'),
        (CURTIES, 'Curties'),
    )

    type = models.CharField(max_length=20, choices=TYPES)
    dining_halls = models.CharField(max_length=20, choices=DINING_HALLS)
    from_time = models.TimeField(null=True)
    to_time = models.TimeField(null=True)
    user = models.ForeignKey('auth.User', PROTECT, related_name='schedules')

    class Meta:
        ordering = ['from_time']
