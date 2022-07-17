from django.urls import path, include, re_path
from . import views
from rest_framework import routers

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

router = routers.DefaultRouter()
router.register('posts', views.PostView)
router.register('users', views.UserView)
router.register('roles', views.RoleView)

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # path('posts_list/', views.PostView.post_list),
    # path('posts_list/', views.PostView.post_list),
    # re_path(r'^posts_list/(?P<id>[0-9]+)$', views.PostView.post_detail),
    # path('posts_list/<int:pk>', views.PostView.post_detail),
    # path('add_post/', views.PostView.perform_create),
    # path('create/', views.PostCreateView.as_view(), name='Create'),


]