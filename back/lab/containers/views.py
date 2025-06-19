from django.contrib.auth.models import Group, User
from .models import (
    Container,
    ContainerType,
    ContainerCollection,
    ContainerCollectionType,
)
from rest_framework import permissions, viewsets

from lab.containers.serializers import (
    GroupSerializer,
    UserSerializer,
    ContainerSerializer,
    ContainerTypeSerializer,
    ContainerCollectionSerializer,
    ContainerCollectionTypeSerializer,
)

from django_filters.rest_framework import DjangoFilterBackend


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all().order_by("name")
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class ContainerViewSet(viewsets.ModelViewSet):
    queryset = Container.objects.all().order_by("id")
    serializer_class = ContainerSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    search_fields = ['barcode', 'location_x', 'location_y', 'location_name', 'container_type', 'container_collection']
    filterset_fields = ['barcode', 'location_x', 'location_y', 'location_name', 'container_type', 'container_collection']


class ContainerTypeviewSet(viewsets.ModelViewSet):
    queryset = ContainerType.objects.all().order_by("id")
    serializer_class = ContainerTypeSerializer
    permission_classes = [permissions.IsAuthenticated]


class ContainerCollectionViewSet(viewsets.ModelViewSet):    
    queryset = ContainerCollection.objects.all().order_by("id")
    serializer_class = ContainerCollectionSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['barcode', 'size', 'name', 'description', 'container_collection_type']



class ContainerCollectionTypeViewSet(viewsets.ModelViewSet):
    queryset = ContainerCollectionType.objects.all().order_by("id")
    serializer_class = ContainerCollectionTypeSerializer
    permission_classes = [permissions.IsAuthenticated]
