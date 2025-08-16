<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Bíblia Paróquia São João Batista</title>
</head>
<body>

<div style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.6; color: #333; max-width: 900px; margin: auto; padding: 20px;">

  <!-- CABEÇALHO -->
  <div style="text-align: center; border-bottom: 2px solid #00529B; padding-bottom: 20px; margin-bottom: 30px;">
    <img src="logo_paroquia.png" alt="Logo da Paróquia" width="150">
    <h1 style="color: #00529B; margin-top: 10px;">📖 Bíblia Paróquia São João Batista</h1>
    <p style="font-size: 1.2em; color: #555;">
      Aplicativo interativo desenvolvido para a paróquia São João Batista – Sertãozinho/SP, com o objetivo de tornar a Palavra de Deus acessível e interativa para todos.
    </p>
  </div>

  <!-- SOBRE O PROJETO -->
  <h2 style="color: #00529B; border-bottom: 1px solid #ddd; padding-bottom: 5px;">📌 Sobre o Projeto</h2>
  <p>O projeto visa:</p>
  <ul>
    <li>Responder perguntas sobre a Bíblia e o <strong>Catecismo da Igreja Católica</strong> usando APIs do Gemini.</li>
    <li>Permitir a leitura de diversas versões da Bíblia, como:
      <ul>
        <li>Septuaginta</li>
        <li>Vulgata</li>
        <li>Ave Maria</li>
        <li>Bíblia Pastoral</li>
        <li>Bíblia de Jerusalém</li>
      </ul>
    </li>
    <li>Rodar localmente em um <strong>Raspberry Pi</strong> ou computador acessível, com interface em tablet.</li>
  </ul>
  <p><strong>Motivação:</strong> Este projeto nasce da <strong>fé em Jesus Cristo</strong> e do <strong>mandamento de ajudar a espalhar o Evangelho</strong>.</p>

  <!-- ARQUITETURA -->
  <h2 style="color: #00529B; border-bottom: 1px solid #ddd; padding-bottom: 5px; margin-top: 30px;">🛠️ Arquitetura do Projeto</h2>
  <ul>
    <li><strong>Backend/API:</strong> Python (<code>Flask</code> ou <code>FastAPI</code>) para processar perguntas e consultas à Bíblia/Catecismo.</li>
    <li><strong>Frontend/UI:</strong> Java (<code>JavaFX</code>) para interface gráfica interativa no tablet.</li>
    <li>Comunicação entre backend e frontend via <strong>requisições HTTP/JSON</strong>.</li>
  </ul>

  <!-- COMO EXECUTAR -->
  <h2 style="color: #00529B; border-bottom: 1px solid #ddd; padding-bottom: 5px; margin-top: 30px;">🚀 Como Executar</h2>
  <h3 style="color: #333;">1. Pré-requisitos</h3>
  <ul>
    <li>Python 3.8 ou superior.</li>
    <li>Raspberry Pi ou computador acessível.</li>
    <li>Tablet ou tela para a interface.</li>
    <li>Acesso à internet para configuração inicial do backend.</li>
  </ul>

  <h3 style="color: #333;">2. Instalação</h3>
  <pre style="background-color: #2d2d2d; color: #ccc; padding: 15px; border-radius: 5px; overflow-x: auto;"><code># Clone o repositório
git clone https://github.com/SeuUsuario/Biblia-Paroquia-SJB.git

# Instale as dependências Python
pip install -r requirements.txt
  </code></pre>

  <h3 style="color: #333;">3. Execução</h3>
  <ul>
    <li>Inicie o backend Python: <code>python app.py</code>.</li>
    <li>Abra a UI Java no tablet e conecte ao backend via HTTP.</li>
    <li>Digite perguntas ou navegue pelas versões da Bíblia disponíveis.</li>
  </ul>

  <!-- CONTRIBUIDORES -->
  <h2 style="color: #00529B; border-bottom: 1px solid #ddd; padding-bottom: 5px; margin-top: 30px;">👥 Contribuidores</h2>
  <ul>
    <li><strong>Antônio A. Meloni</strong> – Integração com APIs e backend.</li>
    <li><strong>Davi Pereira Souza</strong> – Desenvolvimento da arquitetura e frontend.</li>
  </ul>

  <!-- LICENÇA -->
  <h2 style="color: #00529B; border-bottom: 1px solid #ddd; padding-bottom: 5px; margin-top: 30px;">📄 Licença</h2>
  <p>Este projeto é para <strong>uso exclusivo da Paróquia São João Batista</strong> e não deve ser comercializado.</p>

  <!-- RODAPÉ -->
  <div style="text-align: center; margin-top: 50px; padding-top: 20px; border-top: 2px solid #00529B; font-size: 0.9em; color: #777;">
    <p>Bíblia Paróquia São João Batista &copy; 2025</p>
  </div>

</div>

</body>
</html>
