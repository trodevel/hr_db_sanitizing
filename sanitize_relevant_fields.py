import csv
import re
import sys

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

#db_filename = "samples/db_relev.csv"       # test
db_filename = "db_relev.csv"          # prod

num_read = 0
num_invalid_ids = 0
num_empty_lines = 0
num_outp = 0

reader = csv.reader(open( db_filename, "r"))

for row in reader:

    num_read += 1

    idd   = sanitize_id( row[0] )
    if is_valid_id( idd ) == False:
        #print( f"DEBUG: ignoring broken: {idd}", file=sys.stderr )
        num_invalid_ids += 1
        continue

    phone = sanitize_phone( row[1] )
    skype = sanitize_skype( row[2] )
    telegram = sanitize_telegram( row[3] )
    email    = sanitize_email( row[4] )

    w1 = sanitize_nl( row[5] )
    w2 = sanitize_nl( row[6] )
    w3 = sanitize_nl( row[7] )
    w4 = sanitize_nl( row[8] )
    w5 = sanitize_nl( row[9] )
    w6 = sanitize_nl( row[10] )

    if not ( phone or skype or telegram or email or w1 or w2 or w3 or w4 or w5 or w6 ):
        print( f"DEBUG: ignoring empty: {idd}", file=sys.stderr )
        num_empty_lines += 1
        continue

    print ( "{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10}".format(
        idd,
        quotify( phone ),
        quotify( skype ),
        quotify( telegram ),
        quotify( email ),
        quotify( w1 ),
        quotify( w2 ),
        quotify( w3 ),
        quotify( w4 ),
        quotify( w5 ),
        quotify( w6 )
        ) )

    num_outp += 1

print( f"INFO: read {num_read}, wrote {num_outp}, invalid ids {num_invalid_ids}, empty lines {num_empty_lines}", file=sys.stderr )
