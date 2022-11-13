#!/bin/bash

INP=$1
OUTP=$2

[[ -z $INP ]] && exit 1
[[ -z $OUTP ]] && exit 1

echo "."; sed 's/По настоящее время\s\+([0-9а-я ]*)/now/g' $INP > ${OUTP}.1
echo "."; sed 's/\(\(Январь\|Февраль\|Март\|Апрель\|Май\|Июнь\|Июль\|Август\|Сентябрь\|Октябрь\|Ноябрь\|Декабрь\) [0-9]\+\)\s\+([0-9а-я ]*)/\1/g' ${OUTP}.1 > ${OUTP}.2
echo "."; sed 's/\(\(Январь\|Февраль\|Март\|Апрель\|Май\|Июнь\|Июль\|Август\|Сентябрь\|Октябрь\|Ноябрь\|Декабрь\) [0-9]\+\) — /\1","/g' ${OUTP}.2 > ${OUTP}.3
echo "."; sed 's/&#8203;[0-9\.]*&#8203;//g' ${OUTP}.3 > ${OUTP}.4
echo "."; sed 's/\&amp;/\&/g' ${OUTP}.4 > ${OUTP}.5
echo "."; sed 's/\&amp;/\&/g' ${OUTP}.5 > ${OUTP}.6
echo "."; sed 's/\&amp;/\&/g' ${OUTP}.6 > ${OUTP}.7
echo "."; sed 's/\&quot;/""/g' ${OUTP}.7 > ${OUTP}.8
echo "."; cp ${OUTP}.8 ${OUTP}.9

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
    sed -i "s/\(${s}\) \([0-9]\+\)/\2-${val}/g" ${OUTP}.9
done

echo "."; sed 's/\( - \)*От [0-9]\+ до [0-9]\+ сотрудников//g' ${OUTP}.9 > ${OUTP}.10
echo "."; sed 's/\( - \)*Более [0-9]\+ сотрудников//g' ${OUTP}.10 > ${OUTP}.11
echo "."; sed 's~@https://t.me/@~@~g' ${OUTP}.11 > ${OUTP}.12
echo "."; sed 's~@https://t.me/~@~g' ${OUTP}.12 > ${OUTP}.13
echo "."; sed 's~"@@~"@~g' ${OUTP} > ${OUTP}.14

mv ${OUTP}.14 ${OUTP}
rm ${OUTP}.*
