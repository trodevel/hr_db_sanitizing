import csv
import re
import sys

def quotify( s ):
    return '"' + s.replace( '"', '""' ) + '"'

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

    print( f"DEBUG: line {s}", file=sys.stderr )

    duration = res[ duration_idx ]

    if duration_idx >= 5 and duration_idx <= 10:
        print( "DEBUG: A", file=sys.stderr )
        company  = res[ 0 ]
        location = res[ duration_idx - 2 ]
        position = res[ duration_idx - 1 ]

    elif duration_idx == 4:
        print( "DEBUG: B", file=sys.stderr )
        company  = res[ 0 ]
        tagline  = res[ 1 ]
        location = res[ 2 ]
        position = res[ 3 ]

    elif duration_idx == 3:
        print( "DEBUG: C", file=sys.stderr )
        company  = res[ 0 ]
        location = res[ 1 ]
        position = res[ 2 ]

    elif duration_idx == 2:
        print( "DEBUG: D", file=sys.stderr )
        company  = res[ 0 ]
        position = res[ 2 ]

    elif duration_idx == 1:
        print( "DEBUG: E", file=sys.stderr )
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


#db_filename = "samples/db_relev_no_empty.csv"       # test
db_filename = "db_relev_no_empty.csv" # prod

reader = csv.reader(open( db_filename, "r"))

line_nr = 0

total_num_broken = 0
total_num_valid = 0
total_outp_lines = 0
total_num_w_contacts = 0
total_num_w_experience = 0

for row in reader:

    line_nr += 1

    res = ""

    num_res = 0

    for i in range( 5, 10 ):
        is_company, r = extract( row[i], line_nr, i )
        if is_company:
            res += f",{r}"
            num_res += 1
            total_num_valid += 1
        else:
            total_num_broken += 1

    phone    = row[1]
    skype    = row[2]
    telegram = row[3]
    email    = row[4]

    has_contacts = False

    if phone or skype or telegram or email:
        has_contacts = True
        total_num_w_contacts += 1

    if num_res > 0:
        total_num_w_experience += 1

    if num_res > 0 or has_contacts:
        total_outp_lines += 1
        print( "{0},{1},{2},{3},{4},{5}{6}".format( row[0], quotify( phone ), quotify( skype ), quotify( telegram ), quotify( email ), num_res, res ) )

print( "INFO: read lines {0}, wrote lines {1} (with contacts {2}, with experience {3}), number of experience records: valid {4}, broken {5}".
        format( line_nr, total_outp_lines, total_num_w_contacts, total_num_w_experience, total_num_valid, total_num_broken ),
        file=sys.stderr )
