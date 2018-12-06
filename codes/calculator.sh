#!/bin/bash

pierwszaliczba=$1
znak=$2
drugaliczba=$3

let "a = $pierwszaliczba $znak $drugaliczba"
echo $a

