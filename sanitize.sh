#!/bin/bash

INP=$1
OUTP=$2

[[ -z $INP ]] && exit 1
[[ -z $OUTP ]] && exit 1

#sed 's/По настоящее время\s\+([0-9а-я ]*)/now/g' $INP > ${OUTP}.1
#sed 's/&#8203;[0-9\.]*&#8203;//g' ${OUTP}.1 > ${OUTP}.2
#sed 's/\&amp;/\&/g' ${OUTP}.2 > ${OUTP}.3
#sed 's/\&amp;/\&/g' ${OUTP}.3 > ${OUTP}.4
#sed 's/\&amp;/\&/g' ${OUTP}.4 > ${OUTP}.5
#sed 's/\&quot;/""/g' ${OUTP}.5 > ${OUTP}.6
cp ${OUTP}.6 ${OUTP}.7

declare -A MYMAP
MYMAP[Январь]="01"
MYMAP[Февраль]="02"
MYMAP[Март]="03"
MYMAP[Апрель]="04"
MYMAP[Май]="05"
MYMAP[Июнь]="06"
MYMAP[Июль]="07"
MYMAP[Август]="08"
MYMAP[Сентябрь]="09"
MYMAP[Октябрь]="10"
MYMAP[Ноябрь]="11"
MYMAP[Декабрь]="12"

for s in "${!MYMAP[@]}"
do
    echo "step $s"
    val=${MYMAP[$s]}
    sed -i "s/\(${s}\) \([0-9]\+\)/${val}-\2/g" ${OUTP}.7
done
