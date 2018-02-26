# IMDbBot

Reddit bot that looks for comments that are the name of a movie in  /r/MovieSuggestions. Table contains Title, Directors, Rating, and a brief summary of the movie.

Currently very incomplete.

## Built With

* [PRAW](https://praw.readthedocs.io/en/latest/)
* [IMDbPY](https://github.com/alberanid/imdbpy)

## Author

* Maximillian Lefebvre

### Limitations
Comment must only be the name of movie. Currently uses the IMDbPY to search for movies that match the comment's body and return the first result. 
