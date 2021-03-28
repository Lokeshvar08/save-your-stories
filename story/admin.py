from django.contrib import admin

# Register your models here.
from story.models import Story, UserStoryRelation, Moment

admin.site.register(Story)
admin.site.register(UserStoryRelation)
admin.site.register(Moment)
