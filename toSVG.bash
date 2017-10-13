#!/bin/bash
rm -rf svg
mkdir svg

echo "---- PROCESSING VEGA FILES ---"
for vg in $(ls spec/*.vg.json | sort -n)
do
    jsonName=svg/$(basename -s .vg.json $vg).svg
    vg2svg $vg > $jsonName 2> errorlog.txt || echo $vg "failed VG"
done
echo "---- PROCESSING VEGA-LITE FILES ---"
for vl in $(ls spec/*.vl.json | sort -n)
do
    jsonName=svg/$(basename -s .vl.json $vl).svg
    vl2svg $vl > $jsonName 2> errorlog.txt || echo $vl "failed VL"
done

echo "---- FAILED FILES ---"
find svg -size 0 
find svg -size 0 -print0 | xargs -0 rm
echo "---- Copying to book release dir ... ---"
cp svg/singleview*.svg ../making_sense_of_data/images/singleview
cp svg/multiview*.svg ../making_sense_of_data/images/multiview

