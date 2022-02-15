from . import db_utils

def get_usernames() -> list:
    connection = db_utils.get_connection()