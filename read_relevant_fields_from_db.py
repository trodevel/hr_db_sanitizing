import csv

def sanitize( s ):
    res = s.replace( "\n", "<NL>" ).replace( '"', '""' )
    return '"' + res + '"'

import csv
reader = csv.reader(open("db.csv", "r"))
for row in reader:
    print ( "{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10}".format( row[0].replace( "https://career.habr.com/", "" ),
        sanitize( row[14] ).replace( ' ', '' ),
        sanitize( row[16] ),
        sanitize( row[17] ),
        sanitize( row[19] ),
        sanitize( row[29] ),
        sanitize( row[30] ),
        sanitize( row[31] ),
        sanitize( row[32] ),
        sanitize( row[33] ),
        sanitize( row[34] )
        ) )
