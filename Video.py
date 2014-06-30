import uuid
from tmdbsimple import TMDB
tmdb = TMDB('3b2ff402b6a924b6caaa56f801fdb2e6') # API key given to me (had to register)

class Video(object):
    """
    a Video is an object in an video rental facility
    """
    def __init__(self, title):
        """
        constructor; search IMDB using TMDB for the tile provided
        retrieve attributes about the video from IMDB and save them
        """
        # will hit the TMDB API on every instantiation
        search = tmdb.Search()
        response = search.movie({'query': title})

        # if there are any results to querying for the title, take the first result
        if len(search.results) > 0:
            self.ID = uuid.uuid4()
            self.TMDB_ID = search.results[0]['id']
            movie = tmdb.Movies(self.TMDB_ID).info() # get all the information available

            # save off a few interesting attributes
            self.title = movie['title']
            self.release_date = movie['release_date']
            self.popularity = movie['popularity']
            self.overview = movie['overview']
        else:
            self.initialize()
            print " ##### Warning: could not find any matches for %s" % title

    def initialize(self):
        """invoked when a video title is not found in TMDB... initializes everything to zero values"""
        self.ID = uuid.uuid4()
        self.TMDB_ID = 0
        self.title = ""
        self.release_date = ""
        self.popularity = ""
        self.overview = ""

    def __str__(self):
        return self.print_me()

    def __repr__(self):
        return self.print_me()

    def print_me(self):
        """returns a string of the description of the Video"""
        return "ID: %s Title: %s" % (self.ID, self.title)