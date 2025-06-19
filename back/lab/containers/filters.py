import django_filters

from lab.containers.models import Container, ContainerCollection

class ContainerFilter(django_filters.FilterSet):
    class Meta:
        model = Container
        fields = ['barcode', 'location_name', 'container_type', 'container_collection']


class ContainerCollectionFilter(django_filters.FilterSet):
    class Meta:
        model = ContainerCollection 
        fields = ['barcode','name','description','container_collection_type']