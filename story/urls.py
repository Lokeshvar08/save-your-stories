from django.urls import path
from .views import create_story, delete_story, add_people_to_story, remove_people_from_story, exit_from_story, \
    create_moment, delete_moment

urlpatterns = [
    path('create-story/', create_story),
    path('delete-story/<int:id>/', delete_story),
    path('add-people-to-story/', add_people_to_story),
    path('remove-people-from-story/', remove_people_from_story),
    path('exit-from-story/', exit_from_story),
    path('create-moment/', create_moment),
    path('delete-moment/', delete_moment),
]
