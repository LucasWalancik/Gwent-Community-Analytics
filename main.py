from Twitter.users import get_user
from Database.users_DAO import get_usernames
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

if __name__ == '__main__':

    if not open_database( 'DATABASE.db' ):
        exit( 0 )
    
    usernames = get_usernames()