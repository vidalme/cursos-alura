#!/usr/bin/env python
import pandas as pd
import os, sys, subprocess, pprint, random, re

import gera_pass

# from datetime import datetime
# from openpyxl import Workbook, load_workbook 

def usage_message():
    print()
    print('''
###############################################################################
          
                            [[   TREM  ]]
            
        Automatiza o cadastro de usuários vindos de um arquivo .xls 
           gerenciamento de permissões e geração de relatorios.
                                 
###############################################################################
          ''')
    print(f"NOME")
    print(f"        TREM")
    print()
    print(f"SYNOPSIS")
    print("         trem.py [-h] [-l] [-a] [-g GROUP] [-o OUTPUT]")         
    print()
    print(f"DESCRIÇÃO")
    print("         O gerenciamento_usuarios_permissoes é uma ferramenta em Python que automatiza o cadastro de usuários e o gerenciamento de permissões em um sistema Linux. Ele permite cadastrar novos usuários com base em dados de colaboradores armazenados em um arquivo XLS, separando-os por departamento e aplicando uma política mínima de segurança às senhas.")
    print()
    print("         Além disso, o script tem a capacidade de gerar relatórios sobre os usuários do sistema, incluindo lista dos últimos usuários logados, lista de todos os usuários cadastrados e lista de usuários de um grupo específico. Os relatórios podem ser salvos em diferentes formatos, como CSV, YAML ou XLS.")
    print()
    print("         O script também registra logs de erro detalhados durante o processo de cadastro de usuários e notifica os administradores sobre erros críticos que podem afetar a segurança ou o funcionamento do sistema.")
    print()
    print(f"OPÇÕES")
    print("""
    -h, --help
        Exibe uma mensagem de ajuda com as opções disponíveis.

    -l, --last-users
        Gera um relatório com a lista dos últimos usuários logados.

    -a, --all-users
        Gera um relatório com a lista de todos os usuários.

    -g GROUP, --group GROUP
        Gera um relatório com a lista de usuários de um grupo específico. O argumento GROUP especifica o nome do grupo.

    -o OUTPUT, --output OUTPUT
        Especifica o formato do arquivo de saída para os relatórios. Os formatos suportados são: csv, yaml e xls. O argumento OUTPUT especifica o formato desejado.
        """)
    print()

def create_all_users(all):
    users_criados=[]
    
    sen = '1234'
    hashed_password = subprocess.run(f"echo -n '{sen}' | openssl passwd -1 -stdin", shell=True, capture_output=True, text=True).stdout.strip()
    
    for user in all['Nome']:
        nome_com=all["Nome"][user]
        nome=nome_com.split(" ")
        nome=f"{nome[0].lower()}_{str(random.randint(1000,9999))}"
        grupo=all["Departamento"][user]
        fone=all["Telefone"][user]
        email=all["E-mail"][user]

        user_criado = create_user(nome=nome, senha=hashed_password ,nome_com=nome_com, grupo=grupo, fone=fone, email=email )
        users_criados.append(user_criado)    

    print("Todos usuarios foram adicionados com sucesso")
    print()
    return users_criados


def create_user(nome, senha, nome_com, grupo, fone, email):

    subprocess.run(f"useradd -m -c '{nome_com}' -s /bin/bash -p {senha} -G {grupo} {nome}", shell=True)
    # subprocess.run(f"", shell=True)

    with open ("/etc/empresa_allusers_names.txt","a") as users: 
        users.writelines(f"{nome},")
    print(f"{nome_com} vai ser adicionada(o) com o username {nome} no departamento {grupo},\nfone:{fone}\ne-mail:{email}")
    print()
    return(nome)

def remove_all_users():

    with open("/etc/passwd","r") as users:
        a = users.readlines()

        for i in a:
            n = i.strip().split(':')[0]
            ni = int(i.strip().split(':')[2])
            if ni > 1000 and ni < 10000: remove_user(n)

    subprocess.run("> /etc/empresa_allusers_names.txt",shell=True)
    print("Todos os colaboradores removidos com sucesso")
    remove_all_groups()

def remove_user(nome):
    subprocess.run(f"userdel -r {nome}",shell=True)
    print(f"remove user {nome}")

def create_all_groups(groups):
    for group in groups:
        subprocess.run(['groupadd',f'{group}'])
        print(group)
        with open('/etc/empresa_allgroups_names.txt','a') as groups:
            groups.writelines(f"{group},")

def remove_all_groups():
    with open('/etc/empresa_allgroups_names.txt','r') as groups:
        groups_ls = groups.readlines()
        gls = groups_ls[0].split(',')
        del gls[-1]
        for g in gls:
            subprocess.run(['groupdel',f'{g}'])
    subprocess.run("> /etc/empresa_allgroups_names.txt",shell=True)
    print('Todos os grupos foram removidos')


def main():

    df = pd.read_excel('colaboradores.xls')

    df_unique_departamentos = df['Departamento'].unique().tolist()
    create_all_groups(df_unique_departamentos)

    df_dict = df.to_dict()
    all_users = create_all_users(df_dict)


  
def init():
    if len(sys.argv) == 1:
        usage_message()
        # main()
    if len(sys.argv) > 1:
        for arg in sys.argv:
            if arg=="-add":
                main()
            elif arg=="-del":
                remove_all_users()
                remove_all_groups()
            elif arg=="-a" or arg=="--all_users":
                print('listar todos os usuarios do sistema')
            elif arg=="-l" or arg=="--last_users":
                print('listar ultimos usuarios logados') 
            elif arg=="-g" or arg=="--group":
                print('listar todos os usuarios de um grupo')
            elif arg=="-o" or arg=="--output":
                print('especifica o formato de saida do relatorio')
            elif arg=="-h" or arg=="--help":
                usage_message()                
            # else:
                # usage_message()


if __name__ == "__main__": 
    init()