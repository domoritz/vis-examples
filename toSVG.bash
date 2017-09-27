#!/bin/bash
rm -rf svg
mkdir svg
for vg in spec/*.vg.json
do
	echo $vg
    jsonName=svg/$(basename -s .vg.json $vg).svg
    vg2svg $vg > $jsonName
done
for vl in spec/*.vl.json
do
	echo $vl
    jsonName=svg/$(basename -s .vl.json $vl).svg
    vl2svg $vl > $jsonName
done
cp svg/singleview*.svg ../making_sense_of_data/images/singleview
cp svg/multiview*.svg ../making_sense_of_data/images/multiview