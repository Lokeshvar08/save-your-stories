from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from people.views import create_user, make_friend_request, accept_friend_request, reject_unfriend_request

urlpatterns = [
    path('create-user/', create_user),
    path('login/', obtain_auth_token),
    path('make-friend-request/', make_friend_request),
    path('accept-friend-request/', accept_friend_request),
    path('reject_unfriend_request/', reject_unfriend_request),
]
