#!/bin/bash

cd imagens-livros/asdasd

function conversao (){
if [ ! -d png ]
then
    mkdir png
fi

for img in *.jpg
do
    imgc=$(ls $img | awk -F. '{print $1}')
    convert $img png/$imgc.png
done 
}

conversao 2> errosdeconversao.txt

if [ $? -eq 0 ] 
then
    echo "Conversão realizada com sucesso"
else
    echo "Houve alguma falaha no processo"
fi