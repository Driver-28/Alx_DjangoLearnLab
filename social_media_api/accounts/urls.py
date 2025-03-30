from django.urls import path
from .views import RegisterView
from rest_framework.authtoken.views import obtain_auth_token
from .views import FollowUserView, UnfollowUserView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", obtain_auth_token, name="login"),
]
urlpatterns = [
    path("follow/<int:user_id>/", FollowUserView.as_view(), name="follow-user"),
    path("unfollow/<int:user_id>/", UnfollowUserView.as_view(), name="unfollow-user"),
]
