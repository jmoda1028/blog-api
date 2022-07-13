from django.urls import path, include, re_path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('posts', views.PostView)

urlpatterns = [
    path('', include(router.urls)),
    path('posts_list/', views.PostView.post_list),
    # re_path(r'^posts_list/(?P<id>[0-9]+)$', views.PostView.post_detail),
    path('posts_list/<int:pk>', views.PostView.post_detail),
    path('add_post/', views.PostView.add_post),

]