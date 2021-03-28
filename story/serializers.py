from rest_framework import serializers

from story.models import Story, Moment


class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = '__all__'


class MomentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moment
        fields = '__all__'
