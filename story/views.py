from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# Create your views here.
from story.utils.table_operations import StoryOperation, UserStoryRelationOperation, MomentOperation


@api_view(['POST', ])
@permission_classes([IsAuthenticated, ])
def create_story(request):
    data = {}
    story = StoryOperation.create_story(request.data, request.user)
    if story:
        data['story'] = story
        data['creation'] = True
        return Response(data)
    data['creation'] = False
    return Response(data)


@api_view(['DELETE', ])
@permission_classes([IsAuthenticated, ])
def delete_story(request, id):
    data = {}
    status = StoryOperation.delete_story(request=request, id=id)
    data['deletion'] = status
    return Response(data)


@api_view(['POST', ])
@permission_classes([IsAuthenticated, ])
def add_people_to_story(request):
    data = {}
    status = UserStoryRelationOperation.add_peoples(request.data['story'], request.data['peoples'])
    data['people'] = status
    return Response(data)


@api_view(['DELETE', ])
@permission_classes([IsAuthenticated, ])
def remove_people_from_story(request):
    data = {}
    status = UserStoryRelationOperation.remove_peoples(request.data['story'], request.data['peoples'])
    data['people'] = status
    return Response(data)


@api_view(['DELETE', ])
@permission_classes([IsAuthenticated, ])
def exit_from_story(request):
    data = {}
    status = UserStoryRelationOperation.exit_story(request=request, story_id=request.data['story'])
    data['exit'] = status
    return Response(data)


@api_view(['POST', ])
@permission_classes([IsAuthenticated, ])
def create_moment(request):
    data = {}
    moment = MomentOperation.create_moment(request.data, request.user)
    if moment:
        data['moment'] = moment
        data['creation'] = True
        return Response(data)
    data['creation'] = False
    return Response(data)


@api_view(['DELETE', ])
@permission_classes([IsAuthenticated, ])
def delete_moment(request):
    data = {}
    status = MomentOperation.delete_moment(request=request)
    data['deletion'] = status
    return Response(data)
