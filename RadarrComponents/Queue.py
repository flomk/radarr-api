from .RadarrGeneric import RadarrGeneric


class Quality(object):
    def __init__(self, *args, **kwargs):
        self._id = kwargs.get("id", "")
        self._name = kwargs.get("name", "")
        self._source = kwargs.get("source", "")
        self._resolution = kwargs.get("resolution", "")
        self._modifier = kwargs.get("modifier", "")

    def __repr__(self):
        return "%s (%s)" % (self.__class__.__name__, self.__dict__)

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def source(self):
        return self._source

    @property
    def resolution(self):
        return self._resolution

    @property
    def modifier(self):
        return self._modifier


class AlternativeTitles(object):
    def __init__(self, *args, **kwargs):
        self._source_type = kwargs.get("sourceType", "")
        self._movie_id = kwargs.get("movieId", "")
        self._title = kwargs.get("title", "")
        self._source_id = kwargs.get("sourceId", "")
        self._votes = kwargs.get("votes", "")
        self._vote_count = kwargs.get("voteCount", "")
        self._language = kwargs.get("language", "")
        self._id = kwargs.get("id", "")

    def __repr__(self):
        return "%s (%s)" % (self.__class__.__name__, self.__dict__)

    @property
    def source_type(self):
        return self._source_type

    @property
    def movie_id(self):
        return self._movie_id

    @property
    def title(self):
        return self._title

    @property
    def source_id(self):
        return self._source_id

    @property
    def votes(self):
        return self._votes

    @property
    def vote_count(self):
        return self._vote_count

    @property
    def language(self):
        return self._language

    @property
    def id(self):
        return self._id


class Revision(object):
    def __init__(self, *args, **kwargs):
        self._version = kwargs.get('version', '')
        self._real = kwargs.get('real', '')

    def __repr__(self):
        return "%s (%s)" % (self.__class__.__name__, self.__dict__)

    @property
    def version(self):
        return self._version

    @property
    def real(self):
        return self._real


class MovieQuality(object):
    def __init__(self, *args, **kwargs):
        self._quality = Quality(**kwargs.get('quality', ''))
        self._custom_formats = kwargs.get('customFormats', '')
        self._revision = Revision(**kwargs.get('revision', ''))

    def __repr__(self):
        return "%s (%s)" % (self.__class__.__name__, self.__dict__)

    @property
    def quality(self):
        return self._quality

    @property
    def custom_formats(self):
        return self._custom_formats

    @property
    def revision(self):
        return self._revision


class MovieFile(object):
    def __init__(self, *args, **kwargs):
        self._movie_id = kwargs.get("movieId", "")
        self._relative_path = kwargs.get("relativePath", "")
        self._size = kwargs.get("size", "")
        self._date_added = kwargs.get("dateAdded", "")
        self._release_group = kwargs.get("releaseGroup", "")
        self._quality = MovieQuality(**kwargs.get("quality", ""))
        self._edition = kwargs.get("edition", "")
        self._id = kwargs.get("id", "")

    def __repr__(self):
        return "%s (%s)" % (self.__class__.__name__, self.__dict__)

    @property
    def movie_id(self):
        return self._movie_id

    @property
    def relative_path(self):
        return self._relative_path

    @property
    def size(self):
        return self._size

    @property
    def date_added(self):
        return self._date_added

    @property
    def release_group(self):
        return self._release_group

    @property
    def quality(self):
        return self._quality

    @property
    def edition(self):
        return self._edition

    @property
    def id(self):
        return self._id


class RadarrQueueMovie(RadarrGeneric):
    def __init__(self, *args, **kwargs):
        self._secondary_year_source_id = kwargs.get("secondaryYearSourceId", "")
        self._alternative_titles = [AlternativeTitles(**kw) for kw in kwargs.get("alternativeTitles", "")]
        self._physical_release_note = kwargs.get("physicalReleaseNote", "")
        self._physical_release = kwargs.get("physicalRelease", "")
        self._path_state = kwargs.get("pathState", "")
        self._minimum_availability = kwargs.get("minimumAvailability", "")
        self._is_available = kwargs.get("isAvailable", "")
        self._folder_name = kwargs.get("folderName", "")
        self._movie_file = MovieFile(**kwargs.get("movieFile", ""))
        super().__init__(**kwargs)

    @property
    def secondary_year_source_id(self):
        return self._secondary_year_source_id

    @property
    def physical_release_note(self):
        return self._physical_release_note

    @property
    def physical_release(self):
        return self._physical_release

    @property
    def path_state(self):
        return self._path_state

    @property
    def minimum_availability(self):
        return self._minimum_availability

    @property
    def is_available(self):
        return self._is_available

    @property
    def folder_name(self):
        return self._folder_name

    @property
    def movie_file(self):
        return self._movie_file


class RadarrQueue:
    def __init__(self, *args, **kwargs):
        self._size = kwargs.get("size", "")
        self._title = kwargs.get("title", "")
        self._sizeleft = kwargs.get("sizeleft", "")
        self._timeleft = kwargs.get("timeleft", "")
        self._estimated_completion_time = kwargs.get(
            "estimatedCompletionTime", "")
        self._status = kwargs.get("status", "")
        self._tracked_download_status = kwargs.get("trackedDownloadStatus", "")
        self._status_messages = kwargs.get("statusMessages", "")
        self._download_id = kwargs.get("downloadId", "")
        self._protocol = kwargs.get("protocol", "")
        self._id = kwargs.get("id", "")
        self._quality = MovieQuality(**kwargs.get("quality", ""))
        self._movie = RadarrQueueMovie(**kwargs.get("movie", ""))

    def __repr__(self):
        return "%s (%s)" % (self.__class__.__name__, self.__dict__)

    @property
    def size(self):
        return self._size

    @property
    def title(self):
        return self._title

    @property
    def sizeleft(self):
        return self._sizeleft

    @property
    def timeleft(self):
        return self._timeleft

    @property
    def estimated_completion_time(self):
        return self._estimated_completion_time

    @property
    def status(self):
        return self._status

    @property
    def tracked_download_status(self):
        return self._tracked_download_status

    @property
    def status_messages(self):
        return self._status_messages

    @property
    def download_id(self):
        return self._download_id

    @property
    def protocol(self):
        return self._protocol

    @property
    def id(self):
        return self._id

    @property
    def movie(self):
        return self._movie

    @property
    def quality(self):
        return self._quality
