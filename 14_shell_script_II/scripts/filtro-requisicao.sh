#!/bin/bash

cd ~/devops/courses/devops_alura/14_shell_script_II/apache-log

if [ -z $1 ]
then
    while [ -z $requisicao ]
    do
        read -p "Voce esqueceu de colocar um parametro (GET,PUT,POST,DELETE): " requisicao
        maiusculo=$( echo $requisicao | awk '{ print toupper($1) }' )
    done
else
    maiusculo=$( echo $1 | awk '{ print toupper($1) }' )
fi


case $maiusculo in

    GET)
        cat apache.log | grep 'GET'
    ;;

    PUT)
        cat apache.log | grep 'PUT'
    ;;

    DELETE)
        cat apache.log | grep 'DELETE'
    ;;

    POST)
        cat apache.log | grep 'POST'
    ;;

    *)
        echo 'O parametro passado nao é valido'
    ;;
esac


