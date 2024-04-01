#!/bin/bash

CAMINHO_BACKUP=/home/andre/devops/courses/devops_alura/14_shell_script_II/scripts/backup_mutillidae_amazon
cd $CAMINHO_BACKUP
echo $(pwd)

data=$(date +%F)
echo $data
if [ ! -d $data ]
then
    mkdir $data
fi

tabelas=$(sudo mysql -u root mutillidae -e "show tables;" | grep -v "Tables")
for tabela in $tabelas
do
    mysqldump -u root mutillidae $tabela > $CAMINHO_BACKUP/$data/$tabela.sql
done

aws s3 sync $CAMINHO_BACKUP s3://curso-shell-script-andre