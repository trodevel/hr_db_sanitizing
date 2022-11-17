#!/bin/bash

INP=$1
OUTP=$2

[[ -z $INP ]]  && echo "ERROR: input file is not given" && exit 1
[[ -z $OUTP ]] && echo "ERROR: output file is not given" && exit 1

[[ ! -f $INP ]] && echo "ERROR: file $INP not found" && exit 1

grep '^[A-Za-z0-9_-]\+,' $INP > $OUTP

sz_inp=$( cat $INP | wc -l )
sz_outp=$( cat $OUTP | wc -l )

echo "INFO: wrote $sz_outp of $sz_inp entries with valid ids to $OUTP"
