from matplotlib.pyplot import connect
from . import db_utils



def get_words_from_period( start, end ):
    sql = f"""
        SELECT Tweets.text
        FROM Tweets
        WHERE date( Tweets.created_at ) >= '{ start }'
        AND date( Tweets.created_at ) <= '{ end }'
    """
    connection = db_utils.get_connection()
    cursor = connection.cursor()
    cursor.execute( sql )
    result = cursor.fetchall()
    tweets = [ x[ 0 ] for x in result ]
    return tweets

def get_period_activity( period ):
    sql = f"""
        SELECT COUNT( id ), {period}
        FROM Tweets
        WHERE date( created_at ) >= '2017-05-24'
        GROUP BY {period}
        ORDER BY {period} ASC;
    """
    connection = db_utils.get_connection()
    cursor = connection.cursor()
    cursor.execute( sql )
    result = cursor.fetchall()
    connection.close()
    dates = [ x[ 1 ] for x in result ]
    tweet_counts = [ x[ 0 ] for x in result ]
    result_dict = { 'Date':dates, 'Number of Tweets':tweet_counts }
    return result_dict



def get_latest_tweet_id( user_id ):
    sql = """
        SELECT id
        FROM Tweets
        WHERE author_id = ?
        ORDER BY created_at DESC
        LIMIT 1
        """
    connection = db_utils.get_connection()
    cursor = connection.cursor()
    cursor.execute( sql, ( user_id, ) )
    latest_id = cursor.fetchone()
    if None == latest_id:
        return None
    
    connection.close()
    return latest_id[ 0 ]
    


def add_tweets( tweets_list ):
    sql = """
        INSERT INTO Tweets
        VALUES (?,?,?,?,?,?,?,?,?,?,?)
    """
    connection = db_utils.get_connection()
    try:
        connection.executemany( sql, tweets_list )
        connection.commit()
    except Exception as e:
        print( e )
    connection.close()
    print( f'Successfully added {len( tweets_list ) } Tweets' )