## Linux Onboarding: trabalhe com usuários, permissões e dispositivos

## Localizando conteúdos e trabalhando com as saídas 
<b>grep</b> -> busca por conteudo dentro de arquivo(s)<br>
<b>grep</b> -i -> case insensitive<br>
<b>grep</b> -l -> retorna o arquivo em que o nosso conteudo se encontra<br>
<b>grep</b> -L -> retorna tudo que não tem no conteudo da pesquisa<br>
<b>grep</b> -r -> recursividade<br>
<br>

<b>less</b> -> limita a busca (normalmente é mais usado, more parece deprecated)
<b>more</b> -> limita a busca<br>
b - volta uma pagina<br>
p - para sair<br>

<b>head</b> - primeiras linhas do arquivo (default 10 linhas)
<b>tail</b> - ultimas linhas do arquivos (default 10 linhas)
<b>tail</b> or head n5 - (muda o numero de linhas default)

## Procurando arquivos no sistema

<b>find</b> - Utilizado para encontrar arquivos espalhados pelo sistema. (ao contrario do grep que faz buscas dentro de um ou varios arquivos)<br>
usage:<br>
```
sudo find /etc -maxdepth 2 -name *.conf<br>
```
-name - procura arquivos pelo nome<br>
-maxdepth 2 - limita a profundidade de sub diretorios da busca <br>
-amin -5 - limita a pesquisa a arquivos que foram atualizados nos ultimos 5 minutos<br>
-atime -5 - limita a pesquisa a arquivos que foram atualizados nos ultimos 2 dias<br>
-size +100M - limita a pesquisa a arquivos de ate 100 megabytes<br>
<i>-size 3G - limita a pesquisa a arquivos de exatamente 3 gigas</i><br>

<b>sudo</b> - usado para adquirir permissoes de root user 

## Redirecionamentos e pipe

redirecionamento é feito com:<br>
``` 
grep ssh services > listagem.txt
```
<b>></b> - recria o arquivo e inclui o texto que foi enviado <br>
``` 
grep 3389 services >> listagem.txt
```
<b>>></b>  - adiciona texto a um arquivo<br>

``` 
cat listagem.txt | sort
```
<b>|</b> - pipe, usado para linkar correntes de comandos (muito utilizado)<br>
<b>sort</b> - ordena os resultados<br>
``` 
tail -n 5 syslog | grep systemd > ~/labs/redirecionamento/listagem.txt
```
<b>wc</b> - conta numero de linhas, palavras e letras de uma pesquyusa<br>
-l - retorna apenas as linhas<br>

```
cut logs | curt -d " " -f6-9
``` 
<b>cut</b> - utilizado para extrair colunas de uma pesquisa, podemos setar o delimitador que desejarmos<br>
-d - usamos nosso delimitador
-f - seleciona qual a "coluna"

## Utilizando as Regex

Instalamos o wamerican
```
sudo apt install wamerican -y
```
^ - seleciona texto que comecam com a expressao vinda apos<br>
$ - seleciona texto que terminam com a expressao vainda antes

'grep -E' é a mesma coisa de usar 'egrep'

```
cut american-english | grep -E "^computer$"
```

"^[abcd]oot" - pega palavras que comecam com letras a,b,c ou d seguidas de "oot"<br>
"^[abcd]..oot" - podem ter outras letras apos abcd<br>
"^[l-p]oot$" - primeira letra tem que estar entre l e p no alfabeto, a expresao tem que terminar em oot

### Editores de Texto

Eu ja usso vim, não sou muito experiente mas acho que é o tipo da coisa que so melhora usando e praticando mesmo, as funcoes vao sendo aprendidas de acordo a necessidade. Parece tambem ser bem basico esse modulo de vi.

<b>find and replace</b><br>
:s/encontra essa/substitui por essa<br>
o "%s" é utilizado para fazer o replace no arquivo inteiro<br>
:%s/ssh/SSH/g<br>