# Histórias de Usuário — Projeto MamoIA

> Formato: **Como <tipo de usuário>**, quero **<ação>** para **<benefício>**.  
> Cada história contém: descrição, critérios de aceitação, regras de negócio e cenários de validação (BDD).

---

## HU-01 — Autenticação com E-mail e Senha

**Como** pesquisador cadastrado  
**Quero** acessar o sistema usando meu e-mail e senha  
**Para** gerenciar meus uploads e relatórios com segurança  

### Critérios de Aceitação
- O login deve ocorrer apenas com credenciais válidas.
- O sistema deve exibir mensagem de erro caso e-mail/senha estejam incorretos.
- Após login, o usuário é redirecionado para a tela de upload.

### Regras de Negócio (RN)
- RN01: Cada e-mail é único no sistema.
- RN02: A senha deve ter no mínimo 8 caracteres.

### Cenário de Validação (BDD)
**Dado** que sou um pesquisador cadastrado  
**Quando** informo meu e-mail e senha válidos  
**Então** o sistema deve autenticar e redirecionar para a página inicial.  

---

## HU-02 — Cadastro de Novo Usuário

**Como** novo pesquisador  
**Quero** realizar meu cadastro no sistema  
**Para** poder fazer upload e gerar relatórios personalizados  

### Critérios de Aceitação
- Deve ser possível registrar e-mail, nome e senha.
- O sistema deve impedir e-mails duplicados.
- Após cadastro, o usuário pode realizar login normalmente.

### Regras de Negócio
- RN03: Todos os campos obrigatórios devem ser preenchidos.
- RN04: O e-mail deve seguir formato válido (`exemplo@dominio.com`).

### Cenário (BDD)
**Dado** que sou um novo usuário  
**Quando** preencho todos os campos e envio o formulário  
**Então** o sistema cria a conta e redireciona para o login.

---

## HU-03 — Upload de Imagem Médica

**Como** pesquisador autenticado  
**Quero** fazer upload de uma imagem de mamografia ou tomografia  
**Para** permitir a análise e geração de relatório automático  

### Critérios de Aceitação
- Aceitar formatos `.jpg`, `.png`, `.jpeg`, `.dcm`.
- Exibir confirmação de upload bem-sucedido.
- Armazenar a imagem associada ao usuário autenticado.

### Regras de Negócio
- RN05: O tamanho máximo do arquivo é 10 MB.
- RN06: O campo de tipo de arquivo (`file_type`) deve corresponder ao formato real do upload.

### Cenário (BDD)
**Dado** que estou logado  
**Quando** faço upload de um arquivo `.jpg` válido  
**Então** o sistema salva o arquivo e exibe mensagem de sucesso.

---

## HU-04 — Visualização de Relatórios

**Como** pesquisador autenticado  
**Quero** visualizar os relatórios gerados pelas imagens enviadas  
**Para** acompanhar resultados e exportá-los quando necessário  

### Critérios de Aceitação
- Listar todos os relatórios vinculados ao usuário logado.
- Exibir data, tipo de exame e link para download em PDF.
- Permitir visualização detalhada do resultado.

### Regras de Negócio
- RN07: Relatórios só podem ser acessados pelo usuário proprietário.
- RN08: Cada upload gera um relatório único e inalterável.

### Cenário (BDD)
**Dado** que enviei imagens anteriormente  
**Quando** acesso a aba “Relatórios”  
**Então** devo ver todos os meus relatórios com opção de download.

---

## HU-05 — Geração de Relatório em PDF

**Como** pesquisador autenticado  
**Quero** exportar o resultado da análise em formato PDF  
**Para** arquivar e compartilhar facilmente  

### Critérios de Aceitação
- O relatório deve conter cabeçalho, dados do usuário, data e resultado.
- Deve incluir miniatura da imagem analisada.
- Gerar PDF com formatação padronizada (WeasyPrint).

### Regras de Negócio
- RN09: PDFs são armazenados na pasta de mídia do sistema.
- RN10: O nome do arquivo PDF deve incluir data e identificador do exame.

### Cenário (BDD)
**Dado** que possuo um relatório finalizado  
**Quando** clico em “Exportar PDF”  
**Então** o arquivo é gerado e baixado automaticamente.

---

## HU-06 — Histórico de Uploads

**Como** pesquisador autenticado  
**Quero** visualizar o histórico de uploads realizados  
**Para** saber quais imagens já foram processadas  

### Critérios de Aceitação
- Listar todos os uploads do usuário.
- Exibir data, nome do arquivo e status (pendente / processado / falha).
- Permitir exclusão de uploads inválidos.

### Regras de Negócio
- RN11: Apenas o usuário criador pode excluir o upload.
- RN12: Uploads processados não podem ser removidos.

### Cenário (BDD)
**Dado** que já enviei imagens anteriormente  
**Quando** acesso o histórico  
**Então** vejo todas as imagens enviadas e seus respectivos status.

---

## HU-07 — Logout Seguro

**Como** usuário logado  
**Quero** sair do sistema com segurança  
**Para** proteger meus dados e sessões abertas  

### Critérios de Aceitação
- Ao clicar em “Sair”, a sessão deve ser encerrada.
- O botão de logout deve estar visível no cabeçalho.
- Após logout, o sistema redireciona para a tela de login.

### Cenário (BDD)
**Dado** que estou logado  
**Quando** clico em “Sair”  
**Então** o sistema encerra a sessão e retorna à tela de login.

---

## HU-08 — Gerenciamento via Admin

**Como** administrador do sistema  
**Quero** acessar o painel de administração do Django  
**Para** visualizar e gerenciar usuários, uploads e relatórios  

### Critérios de Aceitação
- Admin deve listar usuários, imagens e relatórios.
- Permitir busca e filtragem por e-mail e data.
- Permitir bloqueio e reativação de contas.

### Regras de Negócio
- RN13: Apenas superusuários têm acesso ao painel administrativo.
- RN14: Não é possível editar diretamente um relatório aprovado.

### Cenário (BDD)
**Dado** que sou superusuário  
**Quando** acesso `/admin`  
**Então** visualizo os modelos User, Upload e Relatório disponíveis.

---

## HU-09 — Filtragem e Pesquisa de Imagens

**Como** pesquisador autenticado  
**Quero** filtrar minhas imagens por data ou tipo  
**Para** localizar facilmente arquivos específicos  

### Critérios de Aceitação
- Campo de busca por nome ou data.
- Filtro rápido por tipo de arquivo.
- Resultados atualizados dinamicamente.

### Regras de Negócio
- RN15: A pesquisa só retorna resultados do próprio usuário.
- RN16: O filtro deve manter o estado entre navegações (session storage ou querystring).

### Cenário (BDD)
**Dado** que tenho diversas imagens enviadas  
**Quando** aplico um filtro de data  
**Então** apenas as imagens correspondentes são exibidas.

---

## HU-10 — Exibição de Status de Processamento

**Como** pesquisador autenticado  
**Quero** ver o status de análise de cada imagem enviada  
**Para** saber quando o relatório estiver disponível  

### Critérios de Aceitação
- Exibir status “Pendente”, “Em processamento”, “Concluído” ou “Erro”.
- Atualizar status automaticamente (refresh manual ou AJAX).
- Destacar uploads com falha em vermelho.

### Regras de Negócio
- RN17: O status “Concluído” indica que o relatório foi gerado.
- RN18: Apenas administradores podem alterar status manualmente.

### Cenário (BDD)
**Dado** que enviei uma imagem recentemente  
**Quando** o processamento for concluído  
**Então** o status deve mudar para “Concluído” e o relatório aparecer na lista.

---

## HU-11 — Integração Futura com IA 

**Como** pesquisador  
**Quero** que o sistema utilize um modelo de IA para classificar as imagens  
**Para** receber automaticamente o diagnóstico estimado  

### Critérios de Aceitação
- Enviar imagem para um modelo pretreinado (PyTorch ou TensorFlow).
- Exibir probabilidade e categoria do resultado.
- Registrar tempo de processamento no relatório.

### Regras de Negócio
- RN19: A classificação automatizada não substitui laudo médico.
- RN20: Logs de inferência devem ser armazenados para auditoria.

### Cenário (BDD)
**Dado** que envio uma imagem de mamografia  
**Quando** o modelo IA processa o exame  
**Então** o sistema retorna a categoria e probabilidade previstas.

---

## HU-12 — Recuperação de Senha

**Como** usuário cadastrado  
**Quero** redefinir minha senha caso a esqueça  
**Para** continuar acessando o sistema  

### Critérios de Aceitação
- O usuário informa o e-mail de cadastro.
- O sistema envia link de redefinição.
- Após redefinir, o login deve funcionar normalmente.

### Regras de Negócio
- RN21: O link de recuperação expira em 30 minutos.
- RN22: A nova senha deve atender aos requisitos mínimos de segurança.

### Cenário (BDD)
**Dado** que esqueci minha senha  
**Quando** solicito recuperação informando meu e-mail  
**Então** recebo um link de redefinição e posso criar uma nova senha.

---

## Referências Cruzadas

| História | Tela relacionada | Arquivo/Template |
|-----------|------------------|------------------|
| HU-01 / HU-02 | Login / Cadastro | `templates/home.html` |
| HU-03 / HU-04 / HU-05 | Upload / Relatórios | `templates/upload.html`, `templates/relatorio.html` |
| HU-06 / HU-07 | Histórico / Logout | `templates/base.html` |
| HU-08 | Painel Admin | `/admin` |
| HU-09 / HU-10 | Histórico de imagens | `views.py` + `models.MedicalImageUpload` |
| HU-11 | IA (futuro) | `services/ai_inference.py` *(planejado)* |
| HU-12 | Recuperação de senha | `views.password_reset` *(planejado)* |



