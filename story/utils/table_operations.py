from django.contrib.auth.models import User

from story.models import Story, UserStoryRelation, Moment
from story.serializers import StorySerializer, MomentSerializer

"""
{
    "story_head":"Goa Trip",
    "story_description":"College Vacation Trip to Goa via mangalore",
    "story_type":"TRAVEL",
    "story_date":"2021-03-27"
}
"""


class StoryOperation:
    def __init__(self, story_head, story_description, story_type, story_date, story_creator):
        self.story_head = story_head
        self.story_description = story_description
        self.story_type = story_type
        self.story_date = story_date
        self.story_creator = story_creator

    @staticmethod
    def create_story(story_details, user):
        try:
            story = Story.objects.create(
                story_head=story_details.get('story_head'),
                story_description=story_details.get('story_description'),
                story_type=story_details.get('story_type'),
                story_date=story_details.get('story_date'),
                story_creator=user
            )
            story.save()
            serialize = StorySerializer(story).data
            return serialize
        except:
            return False

    @staticmethod
    def delete_story(request, id):
        try:
            story = Story.objects.get(id=id)
            if request.user == story.story_creator:
                story.delete()
                return True
            else:
                return False
        except:
            return False


class UserStoryRelationOperation:
    @staticmethod
    def add_peoples(story_id, peoples):
        try:
            for i in peoples:
                user_relation = UserStoryRelation.objects.create(
                    story=Story.objects.get(id=story_id),
                    participant=User.objects.get(username=i)
                )
                user_relation.save()
            return True
        except:
            return False

    @staticmethod
    def remove_peoples(story_id, peoples):
        try:
            for i in peoples:
                user_relation = UserStoryRelation.objects.get(
                    story=Story.objects.get(id=story_id),
                    participant=User.objects.get(username=i)
                )
                user_relation.delete()
            return True
        except:
            return False

    @staticmethod
    def exit_story(request, story_id):
        try:
            user_relation = UserStoryRelation.objects.get(
                story=Story.objects.get(id=story_id),
                participant=User.objects.get(username=request.user)
            )
            user_relation.delete()
            return True
        except:
            return False
        

class MomentOperation:
    def __init__(self, story, participant, moment_head, moment_description):
        self.story = story
        self.participant = participant
        self.moment_head = moment_head
        self.moment_description = moment_description
        
    @staticmethod
    def create_moment(moment_details, user):
        try:
            moment = Moment.objects.create(
                story=Story.objects.get(id=moment_details.get('story_id')),
                participant=user,
                moment_head=moment_details.get('moment_head'),
                moment_description=moment_details.get('moment_description')
            )
            moment.save()
            serialize = MomentSerializer(moment).data
            return serialize
        except:
            return False

    @staticmethod
    def delete_moment(request):
        try:
            moment = Moment.objects.get(id=request.data['moment_id'])
            if request.user == moment.participant:
                moment.delete()
                return True
            else:
                return False
        except:
            return False

