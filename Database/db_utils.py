import sqlite3
import os.path

from sympy import false

_DB_PATH = ''
_DB_CONNECTION = None

def open_database( db_path ):
    _DB_PATH = db_path
    if os.path.isfile( db_path ):
        _DB_CONNECTION = sqlite3.connect( db_path )
        print( "Succesfully connected to the database" )
        return True
    else:
        print( "There is no database to connect to" )
        _DB_CONNECTION = None

def get_connection():
    return _DB_CONNECTION