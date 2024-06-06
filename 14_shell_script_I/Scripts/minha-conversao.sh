#!/bin/bash

all=$(ls universe)

for i in $all
j=realpath $i
do
    if [ -d $j ]  
    then
        echo $i 'é um diretorio'
    else
        echo $i 'não é um diretorio'
    fi
done