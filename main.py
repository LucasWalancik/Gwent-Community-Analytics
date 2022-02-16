from Database import users_DAO
from Database import tweets_DAO
from Twitter.tweets import get_tweets
from Twitter.users import get_user_info
from Database.db_utils import open_database
# Workflow of server.py:
# Update database
    # Get usernames list from the database
    # For every username
    # get User data from users.py, run update_user in users_DAO.py
    # Get latest tweets from tweets.py


# Generate analysis
# Push to Pages
# sleep( SOME AMOUNT OF TIME (HOUR, COUPLE OF HOURS, DAY, WEEK ) )
def update_users() -> None:
    user_ids = users_DAO.get_user_ids()
    for id in user_ids:
        user = get_user_info( id = id )
        users_DAO.update_user( user )
        if user.get_protected():
            pass
        else:
            latest_id = tweets_DAO.get_latest_tweet_id( user.get_id() )
            if None != latest_id:
                tweets_list = get_tweets( user.get_id(), since_id=latest_id )
                tweets_list = [ x.to_tuple() for x in tweets_list ]
                tweets_DAO.add_tweets( tweets_list )

if __name__ == '__main__':

    if not open_database( 'DATABASE.db' ):
        exit( 0 )
    
    update_users()