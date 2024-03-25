<h1>Trem</h1>
<h4>Gerenciamento de Usuários e Permissões com Python</h4>

<h3>Cenário</h3>

<p>Você administra um sistema Linux que precisa de um gerenciamento eficiente de usuários e suas permissões. Para otimizar esse processo, você precisa automatizar as seguintes tarefas:</p>

<h2>Requisitos Funcionais</h2>

<h3>Cadastro de Usuários</h3>
<ul>
<li>Os dados dos colaboradores estão armazenados em um arquivo XLS, incluindo nome de usuário, nome completo, e-mail, departamento e data de expiração da senha</li>
<li>Os usuários devem ser separados por departamento: marketing, financeiro, legal, administrativo ou TI.</li>
<li>Cada usuário deve ter um diretório pessoal criado em /home do sistema.</li>
<li>As senhas dos usuários devem seguir uma política mínima de segurança.</li>
</ul>

<h3>Geração de Relatórios:</h3>

<ul>
<li>O script deve ter a capacidade de gerar relatórios sobre os usuários do sistema.</li>
<li>Os relatórios devem incluir:</li>
<ul>
<li>Lista dos últimos usuários logados.</li>
<li>Lista de todos os usuários cadastrados.</li>
<li>Lista de usuários de um grupo específico.</li>
</ul>
<li>Os relatórios podem ser salvos em formatos .csv, .yaml ou .xls, conforme especificado.</li>
</ul>

<h3>Geração de Logs de Erro</h3>

<ul>
<li>O script deve registrar quaisquer erros que ocorram durante o processo de cadastro de usuários.</li>
<li>Os logs de erro devem incluir informações detalhadas sobre o erro e o contexto em que ocorreu.</li>
<li>Os logs devem ser salvos em algum lugar especifico</li>
</ul>

<h3>Notificação de Administradores</h3>
<ul>
<li>Registrar erros em um arquivo de log para análise e resolução de problemas.</li>
<li>Notificar os administradores sobre erros críticos que podem afetar a segurança ou o funcionamento do sistema.</li>
<li>As notificações devem ser enviadas por e-mail ou por outros meios de comunicação especificados.</li>
</ul>
