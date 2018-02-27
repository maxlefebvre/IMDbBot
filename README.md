# IMDbBot

Reddit bot that looks for comments that are the name of a movie in  /r/MovieSuggestions. Table contains Title, Directors, Rating, and a brief summary of the movie.

Currently very incomplete.

### TODO list

* [x] Parse Comments for Movie titles
* [x] Create reply template
* [x] Create link to IMDb page for more info
* [ ] Add movie cover to reply table
* [ ] Post Reply to comment
* [ ] Make comment parsing more accurate so that comment body can contain movit title without it being the only title
* [ ] Make reply more malleable,e.g. if rating is unavailable, post but with it it.
* [ ] Eliminate false positives

## Built With

* [PRAW](https://praw.readthedocs.io/en/latest/)
* [IMDbPY](https://github.com/alberanid/imdbpy)

## Author

* Maximillian Lefebvre

### Limitations
Comment must only be the name of movie. Currently uses the IMDbPY to search for movies that match the comment's body and return the first result. 
