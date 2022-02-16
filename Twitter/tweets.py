import requests
import os

class Tweet:
    def __init__(self, tweet_dict, author_id ) -> None:
        self.id = tweet_dict.get( 'id' )
        self.author_id = author_id
        self.text = tweet_dict.get( 'text' )
        
        attachments = tweet_dict.get( 'attachments' )
        if None == attachments:
            attachments = 0
        else:
            al = attachments.values()
            attachments = list( al )[ 0 ]
            attachments = len( attachments )
        
        self.attachments = attachments
        self.created_at = tweet_dict.get( 'created_at' )
        self.lang = tweet_dict.get( 'lang' )

        public_metrics = tweet_dict.get( 'public_metrics' )
        self.retweet_count = public_metrics.get( 'retweet_count' )
        self.reply_count = public_metrics.get( 'reply_count' )
        self.like_count = public_metrics.get( 'like_count' )
        self.quote_count = public_metrics.get( 'quote_count' )

        self.source = tweet_dict.get( 'source' )

    def __str__(self) -> str:
        return self.text

    def to_tuple( self ) -> tuple:
        return (
            self.id,
            self.author_id,
            self.text,
            self.attachments,
            self.created_at,
            self.lang,
            self.retweet_count,
            self.reply_count,
            self.like_count,
            self.quote_count,
            self.source,
        )


def _get_url( user_id ):
    url = f'https://api.twitter.com/2/users/{ user_id }/tweets'
    return url


def _get_params( since_id ):
    params = {
        'exclude':'retweets',
        'max_results':'100',
        'tweet.fields':'attachments,created_at,lang,public_metrics,source',
    }
    if None != since_id:
        params.update({'since_id':since_id})
    return params


def _get_bearer_token():
    return  os.environ.get("BEARER_TOKEN")



def _get_headers():
    bearer_token = _get_bearer_token()
    headers = { "Authorization":f"Bearer { bearer_token }" }
    return headers


def _parse_response( response, user_id ):
    response = response.json()
    data = response.get( 'data' )
    meta = response.get( 'meta' )
    if None == data:
        tweets_list = None
    else:
        tweets_list = [ Tweet( x, user_id ) for x in data ]
    
    pagination_token = meta.get( 'pagination_token' )
    return tweets_list, pagination_token

def get_tweets( user_id, since_id = None ):
    url = _get_url( user_id )
    params = _get_params( since_id )
    headers = _get_headers()
    pagination_token = 'Not Empty'
    tweets_list = []

    while None !=pagination_token:
        response = requests.get( url = url, params = params, headers = headers )
        next_tweets, pagination_token = _parse_response( response, user_id )
        if None != next_tweets:
            tweets_list = tweets_list + next_tweets
        params.update( {'pagination_token':pagination_token } )

    return tweets_list