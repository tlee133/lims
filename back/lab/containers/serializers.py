from django.contrib.auth.models import Group, User
from rest_framework import serializers
from lab.containers import helpers
from .models import (
    Container,
    ContainerType,
    ContainerCollection,
    ContainerCollectionType,
)
from .geometry import PlateGeometry


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]


class ContainerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Container
        fields = [
            "id",
            "barcode",
            "location_x",
            "location_y",
            "location_name",
            "container_type",
            "container_collection",
        ]



class ContainerTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ContainerType
        fields = ["id", "name", "description"]


class ContainerCollectionTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ContainerCollectionType
        fields = ["id", "name", "description"]


class ContainerCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContainerCollection
        fields = [
            "id",
            "barcode",
            "created",
            "modified",
            "size",
            "name",
            "description",
            "container_collection_type",
        ]
        extra_kwargs = {
                'barcode': {'validators': []}  # Disables all validators for 'name'
        }

    def create(self, validated_data):
        container_collection_type = validated_data["container_collection_type"]
        size = validated_data["size"]
        plate = PlateGeometry(size)
        # Generate new barcode
        last_container = ContainerCollection.objects.all().order_by("-id").first()
        if last_container == None:
            last_barcode = 0
        else:
            last_barcode = last_container.barcode
            
        serial = helpers.Barcode(int(last_barcode))
        validated_data["barcode"] = serial.get_one()
        
        container_collection = ContainerCollection.objects.create(**validated_data)
        
        
        if container_collection_type == ContainerCollectionType.objects.get(
            name="plate"
        ):

            well = {"container_type": ContainerType.objects.get(name="well")}
            for col in range(plate.columns):
                for row in range(plate.rows):
                    location_name = f"{chr(65+row)}{col + 1}"
                    well["location_x"] = col
                    well["location_y"] = row
                    well["location_name"] = location_name
                    well["barcode"] = container_collection.barcode + ":" + location_name
                    Container.objects.create(
                        container_collection=container_collection, **well
                    )

        return container_collection


        """
        TODO: Implement the creation of containers for other collection types
        Wells can only be created for plates.
        Tubes can be created for racks and boxes.
        """