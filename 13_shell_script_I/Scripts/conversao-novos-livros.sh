#!/bin/bash

function converte_imagem(){
    local caminho_imagem=$1
    local imagem_sem_extsensao=$(ls $caminho_imagem | awk -F. '{ print $1 }')
    convert $imagem_sem_extensao.jpg $imagem_sem_extensao.png
}


function varrer_diretorio(){
    cd $1
    for arquivo in *
    do
        local caminho_arquivo=$(find ~/devops/courses/devops_alura/13_shell_script_I/universe -name $arquivo)
        if [ -d $caminho_arquivo ]
        then
            varrer_diretorio $caminho_arquivo
            echo $caminho_arquivo
        else
            echo 'converteria'
            converte_imagem $caminho_arquivo
        fi
    done
}

varrer_diretorio ~/devops/courses/devops_alura/13_shell_script_I/universe

if [ $? -eq 0 ]
then
    echo 'A conversão foi um sucesso'
else
    echo 'Houve algum problema na conversão'
fi