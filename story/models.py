from django.contrib.auth.models import User
from django.db import models

# Create your models here.

STORY_TYPES = (
    ('BIRTHDAY', 'BIRTHDAY'),
    ('WEDDING', 'WEDDING'),
    ('RE-UNION', 'RE-UNION'),
    ('HANG OUT', 'HANG OUT'),
    ('TRAVEL', 'TRAVEL'),
    ('OTHER', 'OTHER')
)


class Story(models.Model):
    story_head = models.CharField(max_length=200, null=False, blank=False)
    story_description = models.TextField(max_length=1000, null=False, blank=False)
    story_type = models.CharField(max_length=20, choices=STORY_TYPES, default='OTHER')
    story_date = models.DateField(blank=True, null=True)
    story_creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.story_head + ": " + str(self.story_creator)


class UserStoryRelation(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    participant = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.story.story_head + ": " + str(self.participant)


class Moment(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    participant = models.ForeignKey(User, on_delete=models.CASCADE)
    moment_head = models.CharField(max_length=200, null=False, blank=False)
    moment_description = models.CharField(max_length=1000, null=False, blank=False)

    def __str__(self):
        return self.story.story_head+": "+self.moment_head
