from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, GroupViewSet, CommentViewSet
from rest_framework.authtoken import views

router = DefaultRouter()
router.register(r"posts", PostViewSet, basename="posts")
router.register(r"groups", GroupViewSet, basename="groups")
router.register(r"posts/(?P<post_id>\d+)/comments", CommentViewSet,
                basename="comments")

urlpatterns = [
    path("", include(router.urls)),
    path("v1/", include(router.urls)),
    path("v1/api-token-auth/", views.obtain_auth_token),
]
