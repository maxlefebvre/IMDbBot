import praw
from imdb import IMDb

ia = IMDb()
reddit = praw.Reddit('bot1', user_agent='testing bot stuff') 
subreddit=reddit.subreddit('MovieSuggestions')


REPLY_TEMPLATE = (  'Title | {0}\n'
                    'Directors | {1}\n'
                    'Rating | {2}/10\n'
                    'Summary | {3}\n' )  

def main():
    # Fetches top 25 posts from specfic subreddit
    for submission in subreddit.hot(limit=5):
        process_comments(submission)


def process_comments(submission):
    submission.comments.replace_more(limit=None)
    for comment in submission.comments.list():
        movies = ia.search_movie(comment.body)
        if movies:
            movie = ia.get_movie(movies[0].movieID)
            #print('Comment: ' + comment.body)
            print_movie(movie)

            
def print_movie(movie):
    if (movie['title']):
        title = movie['title']
        rating = str(movie['rating'])
        directors = ''
        for person in movie['director']:
            directors += person['name'] + ' '
        summary = ''
        for line in movie['plot summary'][0]:
            summary += line
        summary += '...'
        reply = REPLY_TEMPLATE.format(title, directors, rating, summary)
        print(reply)

if __name__ == '__main__':
    main()

        

