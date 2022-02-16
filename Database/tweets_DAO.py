from matplotlib.pyplot import connect
from . import db_utils

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