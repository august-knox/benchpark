#!/bin/bash

compilers=("gcc10" "gcc11" "gcc9" "gcc12" "gcc8" "gcc13" "gcc14")
#compilers=("gcc14")
optParams=("O0" "O2" "O3" "Os")
scaling=("weak" "strong")
destUrl="/usr/workspace/knox10/newBMs"
for i in ${compilers[@]}
do 
    for j in ${optParams[@]}
    do
        for scale in ${scaling[@]}
        do
            echo $i $j $scale
            #./bin/benchpark experiment init --dest=experiments/quicksilver/$i$j$scale quicksilver compiler=$i optParam=$j scaling=$scale
            #wait
            #./bin/benchpark setup quicksilver/$i$j$scale barryEx $destUrl
            #wait
            #ramble -P -D $destUrl/quicksilver/$i$j$scale/barryEx/workspace workspace setup
            #wait
            ramble -P -D $destUrl/quicksilver/$i$j$scale/barryEx/workspace on
        done
    done
done
