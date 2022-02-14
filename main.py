from Twitter.users import get_user

if __name__ == '__main__':
    print( "Main Menu" )
    username = input( "Enter chosen username: " )
    user = get_user( username )
    if None == user:
        print( 'Could not download user with given username' )