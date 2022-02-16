from . import db_utils

def get_usernames() -> list:
    connection = db_utils.get_connection()
    sql = """SELECT username FROM Users"""
    usernames = [ x[0] for x in connection.execute( sql ) ]
    print( usernames )
    connection.commit()
    connection.close()


def get_user_ids() -> list:
    connection = db_utils.get_connection()
    sql = 'SELECT id FROM Users'
    ids = [ id[0] for id in connection.execute( sql ) ]
    connection.commit()
    connection.close()
    return ids


def update_user( User ):
    sql = """
        UPDATE Users
        SET name = ?,
        username = ?,
        created_at = ?,
        description = ?,
        protected = ?,
        followers_count = ?,
        following_count = ?,
        tweet_count = ?,
        listed_count = ?,
        verified = ?
        WHERE id = ?
    """
    connection = db_utils.get_connection()
    connection.execute( sql, User.to_tuple() )
    connection.commit()
    connection.close()
    print( f'Succesfully updated: { User.get_username() } info')

