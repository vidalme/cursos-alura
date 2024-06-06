#!/bin/bash

echo "digite o diretorio de backup: "
read diretorio_bkp

cp -rv $diretorio_bkp ~/backup
echo ""
echo "Backup concluido"
echo ""
