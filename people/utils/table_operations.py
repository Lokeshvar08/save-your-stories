from django.contrib.auth.models import User
from django.db.models import Q

from people.models import Friend


class UserOperation:

    def __init__(self, username, email, first_name, last_name):
        self.username = username
        self.email = email
        self.first_name = first_name
        self.last_name = last_name

    @staticmethod
    def create_user(user_details):
        try:
            user = User.objects.create(
                username=user_details.get('username'),
                email=user_details.get('email'),
                first_name=user_details.get('first_name'),
                last_name=user_details.get('last_name')
            )
            user.set_password(user_details.get('password'))
            user.save()
            return True
        except:
            return False


class FriendOperation:

    @staticmethod
    def make_friend_request(request):
        from_user = request.user
        to_user = request.data.get('to_user')
        try:
            make = Friend.objects.create(username_from=from_user, username_to=User.objects.get(username=to_user))
            make.save()
            return True
        except:
            return False

    @staticmethod
    def accept_friend_request(request):
        user = request.user
        from_user = request.data.get('from_user')
        try:
            accept = Friend.objects.get(username_from=User.objects.get(username=from_user), username_to=user)
            accept.friend_status = True
            accept.save()
            return True
        except:
            return False

    @staticmethod
    def reject_unfriend_request(request):
        from_user = request.user
        to_user = User.objects.get(username=request.data.get('user'))
        try:
            remove = Friend.objects.get(
                Q(username_from=from_user, username_to=to_user) | Q(username_from=to_user, username_to=from_user)
            )
            remove.delete()
            return True
        except:
            return False
