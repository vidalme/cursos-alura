## Redes: dos conceitos iniciais à criação de uma intranet

<h3>01.Camadas, protocolos, ping e traceroute</h3>

<p><b>ping</b> - Envia pacotes para algum servidor e espera pelas reposta, retorna o ip, latencia, etc...</p>
<p><b>traceroute</b> - Retorna todo a trajetoria entre quem enviou o comando e o servidor alvo, retorna todos os hops com ips e velocidades</p>

<hr>
<h3>02.Conectando computadores</h3>
<p>Primeiro instalamos o <b>packet tracer</b>, bem simples mas precisa de cadastro no curso de packet tracer da cisco.
<p>Monntamos uma pequena rede com 3 computadores conectados a um Hub, aprendemos que hub é no bueno, antigo e defasado, ameaça segurança e congestionamentos na rede pois não memoriza quem é quem na rede, apenas evia pra todos tudo que recebe.
<p>DNS e nslookup - Não explicou nada de DNS e mencionou rapidamente que o nslookup retorna os ips associados a uma URL e nos diz se está em algum servidor DNS proximo.
<p>Falamos de variados tipos de cabos, e como conecta-los.
<hr>
<h3>03.Switches e monitoramento de tráfego de redes</h3>
<p>Montamos a mesma rede anterior porem agora com um switch ao inves de um hub, entendemos as diferenças entre os dois e como o switch é superior ao hub.
<p>O switch tem a habilidade de memorizar quais ips estão associados a quais enderos mac. Dessa forma nãoprecisa ficar enviado frames para endpoints que não são o destino real e somente quem o frame era alvo recebe.
<p>Conhecemos o wireshark que serve para rastrear pacotes e como eles se movems, passando por diferentes camadas do tcp/ip e como se comporta em todas as camadas. Bem interessante.
<p>submask serve para separar um endereço IP em subnetworks, onde a primeira parte mascara é fixa, pertencente ao host e a segunda parte é alterada para cada maquina conectada nessaa network.
<hr>
<h3>04.Roteadores e endereçamento IP</h3>
<p>Agora sim a coisa vai ficando interessante, estamos criando redes diferentes para conecta-las com roteadores, basicamentes entramos na internet. Criamos uma pequena rede com router e configuramos tudo pela CLI do proprio cisco packet tracer.
<p>
<hr>
<h3>05.Construindo redes locais com servidores</h3>


