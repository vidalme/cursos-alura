# Server Report


<p>Nome do script: <b>reporter.py</b>

<p>Script que coleta todos os processos ativos do sistema e salva a lista em um arquivo localizado no diretorio "/tmp/reports"<p>
<p>O arquivo será salvo com a tag do dia, mes e ano que foi criado (a intenção é que rode em um cronjob diariamente)

Para criar o Cronjob:
```
$ crontab -e
```
<p>Adiciona no arquivo cron a linha abaixo para rodar o script todos os dias ao meio dia.

```
00 12 * * * /home/andre/bin/reporter.py
```