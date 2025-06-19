from django.db import models


class ContainerCollectionType(models.Model):
    CHOICES = [
        ("box", "box"),
        ("rack", "rack"),
        ("plate", "plate"),
        ("tray", "tray"),
    ]

    name = models.CharField(
        max_length=10, choices=CHOICES, default="plate", unique=True
    )
    description = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class ContainerCollection(models.Model):
    barcode = models.CharField(max_length=50, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)    
    description = models.CharField(null=True, max_length=100)
    name = models.CharField(null=True, max_length=30)
    size = models.IntegerField()

    container_collection_type = models.ForeignKey(
        ContainerCollectionType, on_delete=models.CASCADE
    )
    
    def __str__(self):
        return f"{self.name} ({self.barcode})"


class ContainerType(models.Model):
    CHOICES = [
        ("bottle", "bottle"),
        ("flask", "flask"),
        ("jar", "jar"),  
        ("specimen_container", "specimen_container"),      
        ("tube", "tube"),
        ("well", "well"),
    ]
    name = models.CharField(max_length=20, choices=CHOICES, default="well", unique=True)
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.name


class Container(models.Model):
    barcode = models.CharField(null=True, blank=True, max_length=50, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    location_x = models.IntegerField()
    location_y = models.IntegerField()
    location_name = models.CharField(max_length=5)
    container_type = models.ForeignKey(ContainerType, on_delete=models.CASCADE)
    container_collection = models.ForeignKey(
        ContainerCollection, on_delete=models.CASCADE, null=True, blank=True
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["location_x", "location_y", "container_collection"],
                name="unique_container_location",
                condition=models.Q(container_collection__isnull=False),
            )
        ]

    def __str__(self):
        return self.barcode
