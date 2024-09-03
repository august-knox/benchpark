#!/bin/bash
compilers=("gcc10" "gcc11" "gcc9" "gcc12" "gcc8" "gcc13" "gcc14")
optParams=("O0" "O2" "O3" "Os")
scaling=("weak" "strong")
outputFolder="/usr/workspace/knox10/gccResults"
destUrl="/usr/workspace/knox10/newBMs"
for i in ${compilers[@]}
    do
     for j in ${optParams[@]}
     do
         for scale in ${scaling[@]}
         do
             echo $i $j $scale
             rm $destUrl/quicksilver/$i$j$scale/barryEx/workspace/results.2*
             ramble -P -D $destUrl/quicksilver/$i$j$scale/barryEx/workspace workspace analyze
             wait
             cp $destUrl/quicksilver/$i$j$scale/barryEx/workspace/results.202*  $outputFolder
        done
    done
done
