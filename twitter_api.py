import sys
import pandas as pd
from TwitterSearch import TwitterSearch, TwitterSearchOrder

class TwitterScrape:
    """Methods to gather data from twitter searches"""

    def __init__(self):
        # Login to twitter handle using oauth
        self.twitter = TwitterSearch(
            consumer_key = 'PYX15cyo7pBYyrny2kXomGf4N',
            consumer_secret = 'mCMtxofBFLtJv1GVRXeB9w0pw64ObRDPGmIZEGRo3uyl1oPVci',
            access_token = '3369817647-TTV9HTaWAIbvrbpJwgXkVQtm0akEMSihl43No3P',
            access_token_secret = 'WjxjNW8YWmRSL65eIYYhQd4DsBSECO7wKpZpKsfLcR99q'
        )

    def search( self, query, lang='en', n=10**5 ):
        """
        Search twitter for specified query.
        Function returns n tweets or as many as can be found for that query.

        Parameters:
        query -- Search query (String)
        lang -- Specify language of tweets, optional, default: 'en' (String)
        n -- Number of tweets to return, optional, default: 10**3 (Int)

        Returns: 
        tweets_out -- Pandas series of tweets of length n
        """
        # Initialise container
        tweets_out = []
        # Setup twitter search
        tso = TwitterSearchOrder()
        tso.set_keywords([query])
        tso.set_language(lang)
        tso.set_include_entities(False)

        # Begin search
        sys.stdout.write("Tweet number out of {0}: ".format(n))
        for i, tweet in enumerate(self.twitter.search_tweets_iterable(tso)):
            # Break from loop when n tweets are reached
            if i == n:
                break
            # Output progress
            if i % 100 == 0:
                sys.stdout.write('{0} '.format( i ))
                sys.stdout.flush()
            # Add the next tweet to the container
            tweets_out.append('%s' % ( tweet['text'] ))
        print
        # Return as pandas series as it's easier to work with
        return pd.Series( tweets_out )


if __name__ == '__main__':
    q = TwitterScrape()
    tweets =  q.search( 'Trump' )
    print tweets
