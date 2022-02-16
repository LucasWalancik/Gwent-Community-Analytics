
# URL for getting specified user by their username
# https://api.twitter.com/2/users/by/username/:username

# Source: https://developer.twitter.com/en/docs/twitter-api/users/lookup/api-reference/get-users-by-username-username

import os
import requests

class User:
    
    def __init__( self, user_dict ) -> None:
        self.id = user_dict.get( 'id' )
        self.name = user_dict.get( 'name' )
        self.username = user_dict.get( 'username' )
        self.created_at = user_dict.get( 'created_at' )
        self.description = user_dict.get( 'description' )
        self.protected = user_dict.get( 'protected' )
        
        public_metrics = user_dict.get( 'public_metrics' )
        self.followers_count = public_metrics.get( 'followers_count' )
        self.following_count = public_metrics.get( 'following_count' )
        self.tweet_count = public_metrics.get( 'tweet_count' )
        self.listed_count = public_metrics.get( 'listed_count' )

        self.verified = user_dict.get( 'verified' )

    def __str__( self ) -> str:
        return f"{ self.username }"


    def to_tuple( self ) -> tuple:
        return(
            self.name,
            self.username,
            self.created_at,
            self.description,
            self.protected,
            self.followers_count,
            self.following_count,
            self.tweet_count,
            self.listed_count,
            self.verified,
            self.id
            )

    def get_username( self ):
        return self.username

    def get_id( self ):
        return self.id

    def get_protected( self ):
        return self.protected


def _get_bearer_token():
    return  os.environ.get("BEARER_TOKEN")

def _get_url_with_username( username ):
    return f"https://api.twitter.com/2/users/by/username/{username}"

def _get_url_with_id( id ):
    return f'https://api.twitter.com/2/users/{ id }'

def _get_params():
    params = {"user.fields":"created_at,description,protected,public_metrics,verified"}
    return params

def _get_headers():
    bearer_token = _get_bearer_token()
    headers = { "Authorization":f"Bearer {bearer_token}" }
    return headers

def get_user_info( username = '', id = '' ):
    if '' != id:
        url = _get_url_with_id( id )
    elif '' != username:
        url = _get_url_with_username( username )

    params = _get_params()
    headers = _get_headers()

    response = requests.get( url=url, params=params, headers=headers )
    if 200 != response.status_code:
        response.raise_for_status()
    
    else:
        user_dict = response.json()
        errors = user_dict.get( 'errors' )
        if None != errors:
            return None
        else:
            user_dict = user_dict.get( 'data' )
            user = User( user_dict )
            return user