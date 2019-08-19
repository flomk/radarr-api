import json


class Image(object):
    def __init__(self, **kwargs):
        self._cover_type = kwargs.get('coverType', '')
        self._url = kwargs.get('url', '')

    @property
    def cover_type(self):
        """Get the Calendar title"""
        return self._cover_type

    @property
    def url(self):
        """Get the Calendar title"""
        return self._url

    @property
    def json(self):
        return {"coverType": self._cover_type, "url": self._url}


class Ratings(object):
    def __init__(self, **kwargs):
        self._votes = int(kwargs.get('votes', ''))
        self._value = float(kwargs.get('value', ''))

    @property
    def votes(self):
        """Get the Calendar title"""
        return self._votes

    @property
    def value(self):
        """Get the Calendar title"""
        return self._value

    @property
    def json(self):
        return {"votes": self._votes, "value": self._value}


class RadarrGeneric:
    def __init__(self, **kwargs):
        self._added = kwargs.get('added', '')
        self._alternative_titles = kwargs.get('alternativeTitles', '')
        self._clean_title = kwargs.get('cleanTitle', '')
        self._downloaded = kwargs.get('downloaded', '')
        self._genres = kwargs.get('genres', '')
        self._has_file = kwargs.get('hasFile', '')
        self._id = kwargs.get('id', '')
        self._images = [Image(**i) for i in kwargs.get('images', '')]
        self._imdb_id = kwargs.get('imdbId', '')
        self._monitored = kwargs.get('monitored', '')
        self._path = kwargs.get('path', '')
        self._profile_id = kwargs.get('profileId', '')
        self._quality_profile_id = kwargs.get('qualityProfileId', '')
        self._runtime = kwargs.get('runtime', '')
        self._size_on_disk = kwargs.get('sizeOnDisk', '')
        self._sort_title = kwargs.get('sortTitle', '')
        self._status = kwargs.get('status', '')
        self._tags = kwargs.get('tags', '')
        self._title = kwargs.get('title', '')
        self._title_slug = kwargs.get('titleSlug', '')
        self._tmdb_id = kwargs.get('tmdbId', '')
        self._ratings = Ratings(**kwargs.get('ratings', {'votes': None, 'value': None}))
        self._year = kwargs.get('year', '')
        self._studio = kwargs.get('studio', '')
        self._website = kwargs.get('website', '')
        self._you_tube_trailer_id = kwargs.get('youTubeTrailerId', '')
        self._overview = kwargs.get('overview', '')
        self._last_info_sync = kwargs.get('lastInfoSync', '')
        self._in_cinemas = kwargs.get('inCinemas', '')

    def __repr__(self):
        for k, v in self.__dict__.items():
            if isinstance(v, list):
                if all(map(lambda x: isinstance(x, Ratings), v)):
                    self.__dict__.update({k: [u.json for u in v]})
                if all(map(lambda x: isinstance(x, Image), v)):
                    self.__dict__.update({k: [u.json for u in v]})
            if isinstance(v, Ratings):
                self.__dict__.update({k: v.json})
        return "%s (%s)" % (self.__class__.__name__, json.dumps(self.__dict__, indent=4))

    @property
    def last_info_sync(self):
        return self._last_info_sync

    @property
    def ratings(self):
        """Get the Calendar title"""
        return self._ratings

    @property
    def in_cinemas(self):
        """Get the Calendar title"""
        return self._in_cinemas

    @property
    def overview(self):
        """Get the Calendar title"""
        return self._overview

    @property
    def youtube_trailer_id(self):
        """Get the Calendar title"""
        return self._youtube_trailer_id

    @property
    def website(self):
        """Get the Calendar title"""
        return self._website

    @property
    def studio(self):
        """Get the Calendar title"""
        return self._studio

    @property
    def year(self):
        """Get the Calendar title"""
        return self._year
    
    @property
    def added(self):
        return self._added

    @property
    def alternative_titles(self):
        return self._alternative_titles

    @property
    def clean_title(self):
        return self._clean_title

    @property
    def downloaded(self):
        return self._downloaded

    @property
    def genres(self):
        return self._genres

    @property
    def has_file(self):
        return self._has_file

    @property
    def id(self):
        return self._id

    @property
    def images(self):
        return self._images

    @property
    def imdb_id(self):
        return self._imdb_id

    @property
    def monitored(self):
        return self._monitored

    @property
    def path(self):
        return self._path

    @property
    def profile_id(self):
        return self._profile_id

    @property
    def quality_profile_id(self):
        return self._quality_profile_id

    @property
    def runtime(self):
        return self._runtime

    @property
    def size_on_disk(self):
        return self._size_on_disk

    @property
    def sort_title(self):
        return self._sort_title

    @property
    def status(self):
        return self._status

    @property
    def tags(self):
        return self._tags

    @property
    def title(self):
        return self._title

    @property
    def title_slug(self):
        return self._title_slug

    @property
    def tmdb_id(self):
        return self._tmdb_id

    @property
    def ratings(self):
        return self._ratings
