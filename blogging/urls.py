from django.urls import include, path
from rest_framework import routers
from blogging.views import (list_view, detail_view, UserViewSet, GroupViewSet,
                            PostViewSet, CategoryViewSet)


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'postapi', PostViewSet)
router.register(r'categoryapi', CategoryViewSet)


urlpatterns = [
    path('', list_view, name="blog_index"),
    path('posts/<int:post_id>/', detail_view, name="blog_detail"),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]