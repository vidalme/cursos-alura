#!/bin/bash

:resposta_http=$( curl --write-out %{http_code} --silent --output /dev/null http://localhost )

if [ $resposta_http -ne 200 ]
then
# lh=$(hostname)

mail -s "Problema no servidor" andrevidalme78@gmail.com <<del
Houve um problma no servidor, usuarios nao podem acessar seu conteudo web.
del

    systemctl restart apache2
fi
