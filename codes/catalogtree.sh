#!/bin/bash

recurse(){
    userdivs=$*
    #echo $userdivs
    for dir in $userdivs
    do
        if [ -d $dir ] ; then
            echo "${dir}"
            recurse "$dir/*"
        fi
    done
}

recurse $* 