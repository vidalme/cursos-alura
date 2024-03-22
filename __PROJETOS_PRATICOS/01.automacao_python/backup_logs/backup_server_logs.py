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
    ano = t.strftime("%Y")
    mes = t.strftime("%m")
    dia = t.strftime("%d")
    hora = t.strftime("%H")
    minuto = t.strftime("%M")
    segundo = t.strftime("%S")
    time_label = f"{ano}{mes}{dia}_{hora}-{minuto}---{segundo}_"
    # time_label = f"{ano}-{mes}-{dia}"
    return time_label

def main():
    
    try:

        with open("config.yaml","r") as f:

            #carrega as configuracoes do serviço
            config = yaml.safe_load(f)
            
            #destino de todos os backups é definido no arquivo config.yaml e pode ser alterado pra qualquer lugar
            destiny = config['destiny']
            #numero maximo de arquivos acumulados de backup
            max_acumulado = config['period']
            #cria a pasta destino caso ainda nao exista
            if not os.path.exists(destiny): subprocess.run(['mkdir',f'{destiny}'])

            #variavel com os nomes dos diretorios separados pelos bem sucedidos e os que falharam
            sl_fol = "successful_logins"
            fl_fol = "failed_logins"

        #loop na lista de servidores a fazerem backup dos seus logs
        for s in config['servers']:
            #usuario que logara no sistema
            u = s['user']
            #ip do servidor
            ip = s['server_ip']
            #hosname
            name = s['name']

            #conecta simplao
            c = Connection(host=f"{u}@{ip}")
            
            #cria o um path especifico para esse servidor do loop
            destiny_plus = os.path.join(destiny,name)

            #cria paths para os diretorios dentro do diretorio do servidor
            sl_dir = os.path.join(destiny_plus,sl_fol)    
            fl_dir = os.path.join(destiny_plus,fl_fol)    

            #cria diretorio com nome do servidor
            if not os.path.exists(destiny_plus):subprocess.run(['mkdir',f'{destiny_plus}'])
            #cria diretorio para os logins de sucesso
            if not os.path.exists(sl_dir):subprocess.run(['mkdir',f'{sl_dir}'])
            #cria diretorio para os logins que falharam
            if not os.path.exists(fl_dir):subprocess.run(['mkdir',f'{fl_dir}'])

            #cria paths pros arquivos de backuip, logins de sucesso e falhos
            sl_filename = os.path.join(sl_dir,f"{time_stamp()}.txt")
            fl_filename = os.path.join(fl_dir,f"{time_stamp()}.txt")

            if len(os.listdir(sl_dir)) == max_acumulado:
                all_sl_files = [ os.path.join(sl_dir,f) for f in os.listdir(sl_dir) ] 
                all_sl_files.sort()
                os.remove(all_sl_files[0])
                print('agora estou com o maximo numero de arquivios! Apague o arquivo mais antigo.')

            if len(os.listdir(fl_dir)) == max_acumulado:
                all_fl_files = [ os.path.join(fl_dir,f) for f in os.listdir(fl_dir) ] 
                all_fl_files.sort()
                os.remove(all_fl_files[0])
                print('agora estou com o maximo numero de arquivios! Apague o arquivo mais antigo.')

            #aqui temos que separar os try pois se o servidor nao tiver um dos logs 
            #o outro log automaticamente nao funciona
            try:
                # pass
                successful_logins = c.run(f"journalctl -q -S today | grep -iE 'sshd:session'")
                with open (sl_filename,"w") as sl:
                    sl.write(successful_logins.stdout)

            except Exception as e:
                print('======')
                print(e)
                print('======')

            try:
                # pass
                failed_logins = c.run(f"journalctl -q -S today | grep -iE 'sshd.+failed'")
                with open (fl_filename,"w") as fl:
                    fl.write(failed_logins.stdout)

            except Exception as e:
                print('======')
                print(e)
                print('======')


    except Exception as e:
        pass
        # print('nao foi possivel executar os comandos')
        # print(f'sssss ----> {e}')   

if __name__ == "__main__":
    main()
    # usage_message()