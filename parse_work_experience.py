import csv
import re
import sys

def quotify( s ):
    return '"' + s.replace( '"', '""' ) + '"'

def sanitize_phone( s ):
    return s.replace( ' ', '' ).replace( '-', '' )

def remove_empty_lines( v ):

    res = []

    for s in v:
        if s:
            res.append( s )

    return res


def find_index_of_duration_field( v ):
    size = len( v )
    idx = 0

    pattern = "^(Январь|Февраль|Март|Апрель|Май|Июнь|Июль|Август|Сентябрь|Октябрь|Ноябрь|Декабрь) [0-9]+ — "

    for s in v:
        result = re.match(pattern, s)
        if result:
            return idx
        idx += 1

    return -1

def validate_position( s ):

    pattern = " [0-9]+ сотрудников"

    result = re.match( pattern, s )
    if result:
        return 0
    return 1

def extract( s, line_nr, row_nr ):
    tmp = re.split( '<NL>', s )

    res = remove_empty_lines( tmp )

    duration_idx = find_index_of_duration_field( res )

    if duration_idx == -1:
        return [ 0, "" ]

    company = ""
    tagline = ""
    location = ""
    position = ""
    duration = ""

    duration = res[ duration_idx ]

    if duration_idx >= 5 and duration_idx <= 10:
        company  = res[ 0 ]
        location = res[ duration_idx - 2 ]
        position = res[ duration_idx - 1 ]

    elif duration_idx == 4:
        company  = res[ 0 ]
        tagline  = res[ 1 ]
        location = res[ 2 ]
        position = res[ 3 ]

    elif duration_idx == 3:
        company  = res[ 0 ]
        location = res[ 1 ]
        position = res[ 2 ]

    elif duration_idx == 2:
        company  = res[ 0 ]
        position = res[ 2 ]

    elif duration_idx == 1:
        company  = res[ 0 ]

    else:
        print( "WARNING: broken record {0}:{1}: {2}".format( line_nr, row_nr, s ), file=sys.stderr )
        return [0, "" ]

    if validate_position( position ) == 0:
        print( "WARNING: broken position {0}:{1}: {2}".format( line_nr, row_nr, position ), file=sys.stderr )
        return [0, "" ]

    company  = quotify( company )
    tagline  = quotify( tagline )
    location = quotify( location )
    position = quotify( position )
    duration = quotify( duration )

    return [ 1, f'{company},{tagline},{location},{position},{duration}' ]


db_filename = "db_10_relev.csv"       # test
db_filename = "db_relev_no_empty.csv" # prod

reader = csv.reader(open( db_filename, "r"))

line_nr = 0

total_num_broken = 0
total_num_valid = 0

for row in reader:

    line_nr += 1

    res = ""

    num_res = 0

    for i in range( 1, 6 ):
        is_company, r = extract( row[i], line_nr, i )
        if is_company:
            res += f",{r}"
            num_res += 1
            total_num_valid += 1
        else:
            total_num_broken += 1

    if num_res > 0:
        print( "{0},{1}{2}".format( row[0], num_res, res ) )

print( "INFO: number of records: valid {0}, broken {1}".format( total_num_valid, total_num_broken ), file=sys.stderr )
