import praw
from imdb import IMDb

ia = IMDb()
reddit = praw.Reddit('bot1', user_agent='testing bot stuff') 
subreddit=reddit.subreddit('MovieSuggestions')

IMDB_LINK = 'https://www.imdb.com/title/{}'
REPLY_TEMPLATE = (  '|||\n'
                    '---|---\n'
                    'Title | [{0}]({1})\n'
                    'Director(s) | {2}\n'
                    'Rating | {3}/10\n'
                    'Summary | {4}\n' )  

def main():
    # Fetches top 25 posts from specfic subreddit

    # With stream
    # for comment in subreddit.stream.comments():
    #     process_comments(comment)

    # No stream
    for submission in subreddit.hot(limit=5):
        submission.comments.replace_more(limit=None)
        for comment in submission.comments.list():
            process_comments(comment)
    
    # For Testing: 
    # for comment in reddit.submission(url='https://www.reddit.com/r/testingground4bots/comments/80o6x7/test123/?st=je5x4yv3&sh=f4d798b9').comments.list():
    #     process_comments(comment)


def process_comments(comment):
    # TODO: Check author so bot doesn't reply to itself
    movies = ia.search_movie(comment.body)
    if movies:
        movie = ia.get_movie(movies[0].movieID)
        #print('Comment: ' + comment.body)

        # TODO: Remove this for testing on live subreddits
        # reply = print_movie(movie)
        # comment.reply(reply)

            
def print_movie(movie):
    # TODO: Improve exception handling to display available info but not crash when missing one key
    try:
        title = movie['title']
        rating = str(movie['rating'])
        directors = ''
        for person in movie['director']:
            directors += person['name'] + ' '
        summary = ''
        for line in movie['plot summary'][0]:
            summary += line
        summary += '...'
        link = IMDB_LINK.format(movie.movieID)
        reply = REPLY_TEMPLATE.format(title, link, directors, rating, summary)
        print(reply)
        return reply
    except KeyError:
        print('KeyError: Missing some info, going to next movie')

if __name__ == '__main__':
    main()

        

