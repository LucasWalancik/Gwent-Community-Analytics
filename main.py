from Analysis import analysis
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


def update_analysis():
    periods ={
        'Daily-Activity': 'date( Tweets.created_at )',
        'Weekly-Activity': 'strftime( "%Y-%W", Tweets.created_at)',
        'Monthly-Activity': 'strftime( "%Y-%m", TWeets.created_at)'
    }

    expansions = [
            ( '2019-03-27','2019-03-30' ),
            ( '2019-06-27', '2019-06-30' ),    
            ( '2019-10-01', '2019-10-03' ),    
            ( '2019-12-09', '2019-12-11' ),    
            ( '2020-06-29', '2020-06-31' ),    
            ( '2020-12-07', '2020-12-10' ),    
            ( '2021-06-07', '2021-06-10' ),    
            ( '2021-06-07', '2021-06-10' ),    
            ( '2021-08-02', '2021-08-04' ),    
            ( '2021-10-04', '2021-10-06' ),    
                ]
    #for period in periods.items():
    #    activities = tweets_DAO.get_period_activity( period[ 1 ] )
    #    analysis.period_activity( activities, period[ 0 ] )
    used_words = []
    for expansion in expansions:
        used_words = used_words + tweets_DAO.get_words_from_period( start = expansion[ 0 ], end = expansion[ 1 ])
    #used_words = tweets_DAO.get_words_from_period( start='2020-06-30', end='2020-07-02' )
    analysis.most_used_words( used_words )
    


if __name__ == '__main__':

    if not open_database( 'DATABASE.db' ):
        exit( 0 )
    
    #update_users()
    update_analysis()
    #daily_activity( 1 )