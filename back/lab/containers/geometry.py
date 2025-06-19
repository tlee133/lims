from rest_framework.exceptions import ValidationError


class PlateGeometry:
    """
    Class for storing plate dimensions.
    """

    def __init__(self, size: int):
        self.size = size

        if size == 6:
            rows = 2
            columns = 3
        elif size == 12:
            rows = 3
            columns = 4
        elif size == 24:
            rows = 4
            columns = 6
        elif size == 48:
            rows = 6
            columns = 8
        elif size == 96:
            rows = 8
            columns = 12
        elif size == 384:
            rows = 16
            columns = 24
        else:
            raise ValidationError(
                f"Invalid plate size: {size}. Valid sizes: 6, 12, 24, 48, 96, 384."
            )

        self.rows = rows
        self.columns = columns


class RackGeometry:
    """
    Class for storing rack dimensions.
    """

    def __init__(self, size: int):
        self.size = size

        if size == 24:
            rows = 4
            columns = 6
        elif size == 48:
            rows = 6
            columns = 8
        elif size == 96:
            rows = 8
            columns = 12
        elif size == 384:
            rows = 16
            columns = 24
        else:
            raise ValidationError(
                f"Invalid rack size: {size}. Valid sizes: 24, 48, 96, 384."
            )

        self.rows = rows
        self.columns = columns
