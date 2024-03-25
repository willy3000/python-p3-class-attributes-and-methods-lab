class Song:
    # Class attributes
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        # Instance attributes
        self.name = name
        self.artist = artist
        self.genre = genre
        
        # Increment count of songs
        Song.add_song_to_count()
        
        # Add genre to genres list
        Song.add_to_genres(genre)
        
        # Add artist to artists list
        Song.add_to_artists(artist)
        
        # Add to genre count
        Song.add_to_genre_count(genre)
        
        # Add to artist count
        Song.add_to_artist_count(artist)
    
    @classmethod
    def add_song_to_count(cls):
        cls.count += 1
    
    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)
    
    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)
    
    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1
    
    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1