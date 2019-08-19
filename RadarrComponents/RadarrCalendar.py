from .RadarrGeneric import RadarrGeneric, Ratings, Image
import json


class RadarrCalendar(RadarrGeneric):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._physical_release = kwargs.get('physicalRelease', '')

    @property
    def physical_release(self):
        """Get the Calendar title"""
        return self._physical_release
