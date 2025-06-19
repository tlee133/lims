from django.urls import include, path
from rest_framework import routers

from lab.containers import views

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"groups", views.GroupViewSet)
router.register(r"containers", views.ContainerViewSet)
router.register(r"container_type", views.ContainerTypeviewSet)
router.register(r"container_collection", views.ContainerCollectionViewSet)
router.register(r"container_collection_type", views.ContainerCollectionTypeViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
