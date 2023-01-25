<h1>Coin-Backend</h1>

<h2>🔗 Tópicos</h2>
<ul>
<li><a href="#about">Sobre</a></li>
<li><a href="#tools">Ferramentas</a></li>
<li><a href="#db">Banco de dados</a></li>
<li><a href="#routes">Rotas</a></li>
</ul>

<br>
<h2 id="about">📖 Sobre</h2>
<p>
    Este é um projeto para controle financeiro, aqui contém apenas o back-end. Acesse o repositório front-end em: <a href="https://github.com/dhomini-rabelo/Coin-Frontend">https://github.com/dhomini-rabelo/Coin-Frontend</a>.
</p>

<h3 id="organization">Organização</h3>
<ul>
<li>
Os apps estão na pasta backend
</li>
<li>
A pasta COIN é onde está a configuração do projeto
</li>
</ul>

<br>
<h2 id="tools">🛠️ Ferramentas</h2>

<ul>
<li>Django</li>
<li>Django Rest Framework</li>
<li>django-cors-headers</li>
<li>simplejwt</li>
<li>Fast</li>
<li>Redis</li>
</ul>

<br>
<h2 id="db">🏷️ Modelagem do banco de dados</h2>

<h3>User</h3>
<ul>
<li>username</li>
<li>password</li>
<li>name</li>
<li>email</li>
<li>notification_time</li>
</ul>

<h3>Bill</h3>
<ul>
<li>user</li>
<li>title</li>
<li>description</li>
<li>bill_type</li>
<li>value</li>
<li>payment_method</li>
<li>day</li>
<li>partials</li>
<li>created_at</li>
</ul>

<br>
<br>
<h2 id="routes">🌐 Rotas</h2>

<ul>


<br>
<li>
    <h3>Cadastro - "/api/register"</h3>
    <img src="./readme/register.gif">
</li>

<br>
<li>
    <h3>Autenticação JWT - "/api/get-token"</h3>
    <img src="./readme/auth.gif">
</li>

<br>
<li>
    <h3>Atualizar token - "/api/refresh-token"</h3>
    <img src="./readme/refresh.gif">
</li>

<br>
<li>
    <h3>Sem autenticação</h3>
    <img src="./readme/status_401.gif">
</li>

<br>
<li>
    <h3>Atualizar horário de notificação - "/api/change-notification-time"</h3>
    <img src="./readme/change_notification_time.gif">
</li>

<br>
<li>
    <h3>Atualizar senha - "/api/change-password"</h3>
    <img src="./readme/change_password.gif">
</li>

<br>
<li>
    <h3>Atualizar email - "/api/change-email"</h3>
    <img src="./readme/change_email.gif">
</li>

<br>
<li>
    <h3>Cadastrar conta - "/api/bills"</h3>
    <img src="./readme/change_email.gif">
</li>

<br>
<li>
    <h3>Listar contas - "/api/bills"</h3>
    <img src="./readme/bills.gif">
</li>



</ul>