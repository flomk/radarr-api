import json
import re
import requests
import urllib.parse
from RadarrComponents.RadarrMovie import RadarrMovie
from RadarrComponents.RadarrCalendar import RadarrCalendar


class RadarrAPI(object):
    def __init__(self, *args, **kwargs):
        self.api_key = kwargs.get('api_key', '')
        self.session = requests.Session()

    def requester(self, url, method="GET", json=False, *args, **kwargs):
        if method == "GET":
            req = self.session.get(url, **kwargs)
        elif method == "POST":
            req = self.session.post(url, **kwargs)

        if json is True:
            return req.json()
        else:
            return req

    def get_movies(self, m_id=None):
        movie_parms = (('apikey', self.api_key),)
        movies = self.requester(
            'http://localhost:7878/api/movie/', params=(('apikey', self.api_key),), json=True)
        movies = [RadarrMovie(**movie) for movie in movies]
        return movies

    def add_movie(self, *args, **kwargs):
        movie_params = (
            ('apikey', self.api_key),
            ('title', kwargs.get('title', '')),
            ('qualityProfileId', kwargs.get('qualityProfileId', '')),
            ('titleSlug', kwargs.get('titleSlug', '')),
            ('images', kwargs.get('images', '')),
            ('tmdbId', kwargs.get('tmdbId', '')),
            ('year', kwargs.get('year', '')),
            ('path', kwargs.get('path', '')),)
        add_movie = self.requester(
            'http://localhost:7878/api/movie/', method="POST", params=movie_params, json=True)

    def _term_mode(self, term_str):
        mode = None
        if re.match(r'^(?:tt|)([0-9]+)$', term_str):
            if term_str[0:2] == "tt":
                mode = "imdb"
            else:
                mode = "tmdb"
        else:
            mode = "term"
        return mode

    def search_movie(self, term):
        mode = self._term_mode(term)
        mode_params = (('apikey', self.api_key),)

        base_search_url = 'http://localhost:7878/api/movie/lookup'
        if mode in ["imdb", "tmdb"]:
            base_search_url += f'/{mode}'
        mode_map = {
            "imdb": (('imdbId', term),),
            "tmdb": (('tmdbId', term),),
            "term": (('term', term),)
        }
        mode_params = mode_params + mode_map[mode]
        tmp_lst = list()
        movie_search = self.requester(
            base_search_url, params=mode_params, json=True)
        if isinstance(movie_search, list):
            searched_movies = movie_search
        else:
            tmp_lst.append(movie_search)
            searched_movies = tmp_lst

        movies = [RadarrMovie(**movie) for movie in searched_movies]
        tmp_lst.append(movie_search)
        del tmp_lst
        return movies


print(RadarrAPI(api_key='b11e4e3a42224478b30a572b01fe46f8').search_movie('Star Wars'))
