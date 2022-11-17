import csv

def sanitize( s ):
    res = s.replace( "\n", "<NL>" ).replace( '"', '""' )
    return '"' + res + '"'

#db_filename = "db_10.csv"       # test
db_filename = "db.csv"          # prod

reader = csv.reader(open( db_filename, "r"))
for row in reader:
    print ( "{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10}".format(
        row[0],
        sanitize( row[14] ),
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
