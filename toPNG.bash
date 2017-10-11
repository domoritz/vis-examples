#!/bin/bash
rm -rf png
mkdir png
for vg in spec/*.vg.json
do
	echo $vg
    jsonName=png/$(basename -s .vg.json $vg).png
    vg2png $vg > $jsonName
done
for vl in spec/*.vl.json
do
	echo $vl
    jsonName=png/$(basename -s .vl.json $vl).png
    vl2png $vl > $jsonName
done
