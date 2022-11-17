import csv

def quotify( s ):
    return '"' + s.replace( '"', '""' ) + '"'

def sanitize_nl( s ):
    return quotify( s.replace( "\n", "<NL>" ) )

def sanitize_id( s ):
    return s.replace( "https://career.habr.com/", "" )

def sanitize_phone( s ):
    return quotify( s.replace( ' ', '' ).replace( '-', '' ) )

def sanitize_skype( s ):
    return quotify( s.replace( ' ', '' ).replace( 'live:', '' ) )

def sanitize_telegram( s ):
    return quotify( s.replace( ' ', '' ).replace( '-', '' ) )

def sanitize_email( s ):
    return quotify( s.replace( ' ', '' ) )

#db_filename = "db_10_relev.csv"       # test
db_filename = "db_relev.csv"          # prod

reader = csv.reader(open( db_filename, "r"))

for row in reader:
    idd   = sanitize_id( row[0] )
    phone = sanitize_phone( row[1] )
    skype = sanitize_skype( row[2] )
    telegram = sanitize_telegram( row[3] )
    email    = sanitize_email( row[4] )

    print ( "{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10}".format(
        idd,
        phone,
        skype,
        telegram,
        email,
        sanitize( row[5] ),
        sanitize( row[6] ),
        sanitize( row[7] ),
        sanitize( row[8] ),
        sanitize( row[9] ),
        sanitize( row[10] )
        ) )
