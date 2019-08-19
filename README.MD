# Radarr Api
A wrapper around the radarr JSON api

# Installation
    python3 -m pip install radarr-api

# Usage
```python
radarr_api = RadarrAPI(api_key='API_KEY_HERE')
radarr_api.search_movie('Star Wars')
```
returns
```python
[
    RadarrMovie ({
        "_added": "0001-01-01T00:00:00Z",
        "_alternative_titles": [],
        "_clean_title": "",
        "_downloaded": false,
        "_genres": [],
        "_has_file": false,
        "_id": "",
        "_images": [
            {
                "coverType": "poster",
                "url": "http://image.tmdb.org/t/p/original/btTdmkgIvOi0FFip1sPuZI2oQG6.jpg"
            }
        ],
        "_imdb_id": "",
        "_monitored": false,
        "_path": "",
        "_profile_id": 0,
        "_quality_profile_id": 0,
        "_runtime": 0,
        "_size_on_disk": 0,
        "_sort_title": "star wars",
        "_status": "released",
        "_tags": [],
        "_title": "Star Wars",
        "_title_slug": "star-wars-11",
        "_tmdb_id": 11,
        "_ratings": {
            "votes": 11789,
            "value": 8.2
        },
        "_year": 1977,
        "_studio": "",
        "_website": "",
        "_you_tube_trailer_id": "",
        "_overview": "Princess Leia is captured and held hostage by the evil Imperial forces in their effort to take over the galactic Empire. Venturesome Luke Skywalker and dashing captain Han Solo team together with the loveable robot duo R2-D2 and C-3PO to rescue the beautiful princess and restore peace and justice in the Empire.",
        "_last_info_sync": "",
        "_in_cinemas": "1977-05-25T00:00:00Z",
        "_minimum_availability": "tba",
        "_remote_poster": "http://image.tmdb.org/t/p/original/btTdmkgIvOi0FFip1sPuZI2oQG6.jpg"
    }),…,
    RadarrMovie ({
        "_added": "0001-01-01T00:00:00Z",
        "_alternative_titles": [],
        "_clean_title": "",
        "_downloaded": false,
        "_genres": [],
        "_has_file": false,
        "_id": "",
        "_images": [
            {
                "coverType": "poster",
                "url": "http://image.tmdb.org/t/p/original/sgZvwdGuqOfbJTfUNq5lh9B4HQy.jpg"
            }
        ],
        "_imdb_id": "",
        "_monitored": false,
        "_path": "",
        "_profile_id": 0,
        "_quality_profile_id": 0,
        "_runtime": 0,
        "_size_on_disk": 0,
        "_sort_title": "star wars rebels spark rebellion",
        "_status": "released",
        "_tags": [],
        "_title": "Star Wars Rebels: Spark of Rebellion",
        "_title_slug": "star-wars-rebels-spark-of-rebellion-287663",
        "_tmdb_id": 287663,
        "_ratings": {
            "votes": 59,
            "value": 7.0
        },
        "_year": 2014,
        "_studio": "",
        "_website": "",
        "_you_tube_trailer_id": "",
        "_overview": "A Long Time Ago In A Galaxy Far, Far Away\u2026 Against the might of the Galactic Empire, an unlikely band of heroes emerges to renew the fight for freedom.  Five years before the events of Star Wars Episode IV: A New Hope, the reigning evil Empire continues to tighten its grip of power and fear throughout the cosmos. But even amidst the tyranny and oppression of these dark days, a glimmer of light emerges. Meet the ragtag crew of the starship Ghost: Twi\u2019lek pilot Hera, street-smart pickpocket Ezra, team leader Kanan, alien enforcer Zeb, explosives expert Sabine, and Chopper, the cantankerous Droid. Together, they embark on action-packed adventures, battle ruthless villains, and ignite the very first Spark Of Rebellion against a surging tide of Stormtroopers, TIE fighters and the mysterious Inquisitor.",
        "_last_info_sync": "",
        "_in_cinemas": "2014-10-03T00:00:00Z",
        "_minimum_availability": "tba",
        "_remote_poster": "http://image.tmdb.org/t/p/original/sgZvwdGuqOfbJTfUNq5lh9B4HQy.jpg"
    })
]
```

# TODO
- [ ] Add missing features
- [ ] Add missing documentation
- [ ] Add logging
- [ ] Add option to convert to JSON
- [ ] Make the code less ugly