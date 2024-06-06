#!/bin/bash

cd ~/devops/courses/devops_alura/14_shell_script_II/apache-log

regex='\b([0-9]{1,3}\.){3}[0-9]{1,3}\b'

if [[ $1 =~ $regex ]]
then 
    cat apache.log | grep $1
    if [ $? -ne 0 ]
    then
        echo 'Esse numero de IP não foi encontrado'
    fi
else
    echo 'Formato não é válido'
fi