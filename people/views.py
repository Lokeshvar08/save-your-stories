
# Create your views here.
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from people.utils.table_operations import UserOperation, FriendOperation


@api_view(['POST'])
@permission_classes([])
def create_user(request):
    data = {}
    status = UserOperation.create_user(request.data)
    data['creation'] = status
    return Response(data)


@api_view(['POST', ])
@permission_classes([IsAuthenticated, ])
def make_friend_request(request):
    data = {}
    status = FriendOperation.make_friend_request(request=request)
    data['request'] = status
    return Response(data)


@api_view(['POST', ])
@permission_classes([IsAuthenticated, ])
def accept_friend_request(request):
    data = {}
    status = FriendOperation.accept_friend_request(request=request)
    data['request'] = status
    return Response(data)


@api_view(['POST', ])
@permission_classes([IsAuthenticated, ])
def reject_unfriend_request(request):
    data = {}
    status = FriendOperation.reject_unfriend_request(request=request)
    data['request'] = status
    return Response(data)
