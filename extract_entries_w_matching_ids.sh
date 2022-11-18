#!/bin/bash

ids=$( cat ids_matching_sorted.txt );
sz=$( echo "$ids" | grep -c "^" )

echo "num ids = $sz"

INP=db_relev_no_empty_parsed_san.csv
OUTP=db_relev_no_empty_parsed_san_matching.csv

pct_prev=0
pct=0

i=0

cat /dev/null > $OUTP

for s in $ids;
do
    i=$((i + 1))
    pct=$(( ( i * 100 ) / sz ))

    [[ $pct -gt $pct_prev ]] && { pct_prev=$pct; echo "$i, $pct %"; }

    grep "^$s," -m 1 $INP >> $OUTP;
done
