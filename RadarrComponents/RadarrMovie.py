from .RadarrGeneric import RadarrGeneric, Ratings, Image
import json


class RadarrMovie(RadarrGeneric):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._minimum_availability = kwargs.get('minimumAvailability', '')
        self._remote_poster = kwargs.get('remotePoster', '')

    @property
    def minimum_availability(self):
        """Get the Calendar title"""
        return self._minimum_availability

    @property
    def remote_poster(self):
        """Get the Calendar title"""
        return self._remote_poster
