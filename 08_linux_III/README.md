## Linux Onboarding: obtendo e tratando informações do sistema

## Criando e configurando scripts

Essa aula acompanhei mais escrevendo codigo jundo com o professor 

Entendendo a estrutura de um script<br>
Variáveis do sistema (env, PATH, etc)<br>
Alterando as permissões para executar o script<br>
Conhecendo o arquivo .profile e suas aplicações<br>

## Informações do sistema - hardware

```
ip addr
ip route
```
comando para mostrar o ip e rotas

```
sudo lshw
```
mostra todas as infos de hardware

A maioria das infos sobre o sistema ficam em /dev

alguns comandos muito utilizados
```
free
df -h
```

## Informações do sistema - logs

<h3>/var/log</h3>
directorio encontramos todas as infos para desbugar qualquer coisa que esteja dando errado<br><br>

<b>dmesg</b> -> mostra muita informação sobre o boot do sistema, sabermos se um certo disco subiu funcionando ou não, tambem todas as autenticacoes aparecem aqui, falhando ou não<br>
<b>syslog</b> -> mostra os logs do sistema
<b>auth.log</b> -> todos os logs de autenticacao,  usuarios que tentam se concetar ao server ssh por exemplo

## Visualizando e gerenciando processos
<b>
<b>ps</b><br>
<b>ps -a</b><br>
<b>ps -ef</b><br>
<b>ps -aux</b><br>
<b>top</b>
<br><br>
<b>Finalizando processos</b><br>

<b>kill</b><br>
<b>kill -l </b>-> mostra os metodos de finalizar processos<br>
<b>kill -9 </b>-> haduken dos kill de processos<br>

## Tipos de usuários e os seus papéis

<h3>Permissoes definidas no diretorio</h3>
<b><i>/etc/sudoers</i></b><br>
<b><i>/etc/shadow</i></b><br>

<b>visudo</b> -> edita os arquivos de sudo<br>
<b>groups</b> -> mostra todos os groups<br>
<b>su </b>-> muda os usuarios<br>
<b>passwd</b> -> muda a senha<br>