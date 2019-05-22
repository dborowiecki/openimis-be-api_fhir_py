import json

from api_fhir.models.element import Element


class HumanName(Element):

    resource_type = "HumanName"

    def __init__(self):
        self.family = None  # Type `str`.

        self.given = None  # List of `str` items.

        self.period = None  # Type `Period` (represented as `dict` in JSON).

        self.prefix = None  # List of `str` items.

        self.suffix = None  # List of `str` items.

        self.text = None  # Type `str`.

        self.use = None  # Type `str` (usual | official | temp | nickname | anonymous | old | maiden).

        super(HumanName, self).__init__()

    class Meta:
        app_label = 'api_fhir'
