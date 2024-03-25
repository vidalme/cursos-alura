#!/usr/bin/env python
import pandas as pd
import os, sys, subprocess, pprint, random
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
    users_criados = []
    for user in all['Nome']:
        # create_user(user)
        nome_com = all["Nome"][user]
        nome = nome_com.split(" ")
        nome = f"{nome[0].lower()}_{str(random.randint(1000,9999))}"
        grupo = all["Departamento"][user]
        fone = all["Telefone"][user]
        email = all["E-mail"][user]
        user_criado = create_user(nome=nome ,nome_com=nome_com, grupo=grupo, fone=fone, email=email )
        users_criados.append(user_criado)    

    return users_criados

def create_user(nome, nome_com, grupo, fone, email):
    print(f"O {nome_com} vai ser adicionado com o nome de {nome} no grupo {grupo}, fone:{fone} e e-mail:{email}")
    subprocess.run(f"sudo useradd -md /home/{nome} -s /bin/bash {nome}",shell=True)
    return(nome)

def remove_all_users(all):
    for u in all:
        remove_user(u)

def remove_user(nome):
    # subprocess.run(f"userdel -r {nome}",shell=True)
    print(f"remove user {nome}")


def main():
    # subprocess.run("sudo -i",shell=True)

    df = pd.read_excel('colaboradores.xls')
    df_dict = df.to_dict()

    all_users = create_all_users(df_dict)
    print(all_users)

  
def init():

    if len(sys.argv) == 1:
        # usage_message()
        main()
    if len(sys.argv) > 1:
        for arg in sys.argv:
            print(arg)
            if arg=="-a" or arg=="--all_users":
                print('listar todos os usuarios do sistema')
            if arg=="-l" or arg=="--last_users":
                print('listar ultimos usuarios logados') 
            if arg=="-g" or arg=="--group":
                print('listar todos os usuarios de um grupo')
            if arg=="-o" or arg=="--output":
                print('especifica o formato de saida do relatorio')
            if arg=="-h" or arg=="--help":
                usage_message()                
            else:
                usage_message()


if __name__ == "__main__":

    #checa se o usuario precisa de ajuda
    init()

    

    # #a função principal é chamada se não tiverem argumentos
    # if len(sys.argv) == 1:
    #     main()