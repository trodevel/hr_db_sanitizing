import csv
import re

def quotify( s ):
    return '"' + s.replace( '"', '""' ) + '"'

def sanitize_nl( s ):
    return s.replace( "\n", "<NL>" )

def sanitize_id( s ):
    return s.replace( "https://career.habr.com/", "" )

def sanitize_phone( s ):
    return s.replace( ' ', '' ).replace( '-', '' )

def sanitize_skype( s ):
    return s.replace( ' ', '' ).replace( 'live:', '' )

def sanitize_telegram( s ):
    return s.replace( ' ', '' ).replace( 'https://t.me/', '' ).replace( '@', '' )

def sanitize_email( s ):
    return s.replace( ' ', '' )

def is_valid_id( s ):
    if re.match( "[A-Za-z0-9_-]", s ):
        return True
    return False

db_filename = "samples/db_relev.csv"       # test
#db_filename = "db_relev.csv"          # prod

reader = csv.reader(open( db_filename, "r"))

for row in reader:
    idd   = sanitize_id( row[0] )
    phone = sanitize_phone( row[1] )
    skype = sanitize_skype( row[2] )
    telegram = sanitize_telegram( row[3] )
    email    = sanitize_email( row[4] )

    if is_valid_id( idd ) == False:
        continue

    print ( "{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10}".format(
        idd,
        phone,
        skype,
        telegram,
        email,
        sanitize_nl( row[5] ),
        sanitize_nl( row[6] ),
        sanitize_nl( row[7] ),
        sanitize_nl( row[8] ),
        sanitize_nl( row[9] ),
        sanitize_nl( row[10] )
        ) )
