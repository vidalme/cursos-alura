#!/usr/bin/env python

import os, sys, subprocess
import yaml

from fabric import Connection
from datetime import datetime

def usage_message():
    print()
    print('''
#########################################################################  
          
                    [[   backup_server_logs.py   ]]
          
        Script para coletar logs de varios servidores e guada-los
        configurações carregadas do arquivo -> // config.yaml // 
                  
#########################################################################
          ''')
    print(f"NOME")
    print(f"backup_server_logs.py")
    print()
    print(f"SINOPSE")
    print()
    print(f"DESCRÇÃO")
    print()
    print(f"OPÇÕES")
    print()

    print("Command [ path destino ] [ path alvo ]")
    print(f"")
    print(f'''[ path destino ]    --  O path do diretorio destino: todos os arquivos desse diretorio serao 
                        enviados para a lista de servidores que estão lsitadas no arquivo 
                        server_list.txt''')
    print()
    print(f'''[ path alvo ]       --  O path do diretorio alvo: cada servidor remoto recebera os arquivos na 
                        pasta do usuario $USUARIO/[path alvo], se esse diretorio não existir 
                        ele sera criado atuomaticamente''')
    print()

def time_stamp():
    t = datetime.now()
    time_label = f"{t.year}-{t.month}-{t.day}_{t.hour}-{t.minute}-{t.second}-{t.microsecond}_"
    return time_label

def main():
    
    # encontra_ip = "grep -E '^\\s{4}inet\\s.+enp0s3$'"
    # encontra_successful_logins = "grep -iE 'sshd:session' | grep -vi 'failed'"
    # encontra_successful_logins = "grep -iE 'sshd'"
    # encontra_failed_logins = "grep -iE 'sshd.+failed'"

    try:
        pass

        with open("config.yaml","r") as f:
            config = yaml.safe_load(f)



        for s in config['servers']:
            u = s['user']
            ip = s['server_ip']
            name = s['name']

            c = Connection(host=f"{u}@{ip}")

            # print(f"{time_stamp()}successful_logins.txt")

            successful_logins = c.run(f"journalctl -S today | grep -iE 'sshd:session'")
            failed_logins = c.run(f"journalctl -S today | grep -iE 'sshd.+failed'")

            with open (f"{name}_{time_stamp()}successful_logins.txt","w") as sl:
                sl.write(successful_logins.stdout)

            with open (f"{name}_{time_stamp()}failed_logins.txt","w") as fl:
                fl.write(failed_logins.stdout)

            # print(successful_logins)
            # print(failed_logins)
            print('--------------')

    except Exception as e:
        print('nao foi possivel executar os comandos')
        # print(e)   

if __name__ == "__main__":
    main()
    # time_stamp()
    # pass
    # usage_message()