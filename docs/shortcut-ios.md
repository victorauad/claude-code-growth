# Como configurar o Apple Shortcut para enviar links

Este Shortcut aparece no menu "Compartilhar" de qualquer app (Safari, YouTube, Notion...). Com um toque, o link vai direto para o repo e a Action processa automaticamente.

## Pré-requisitos

1. **Token do GitHub (PAT):** Acesse github.com → Settings → Developer Settings → Personal access tokens → Tokens (classic) → Generate new token.
   - Escopos necessários: `repo` (marque apenas este)
   - Copie o token gerado (começa com `ghp_...`)

2. **App Atalhos** no iPhone (vem pré-instalado no iOS).

## Criando o Shortcut (5 min)

1. Abra o app **Atalhos** → toque em **+** (novo atalho).

2. Toque em **Adicionar ação** → pesquise **"Receber entrada"** → adicione **"Receber entrada de atalho"**.
   - Tipo: URL

3. Adicione a ação **"Obter conteúdos de URL"** e configure:
   - **URL:** `https://api.github.com/repos/victorauad/claude-code-growth/issues`
   - **Método:** POST
   - **Cabeçalhos:**
     - `Authorization` → `Bearer SEU_TOKEN_AQUI`
     - `Accept` → `application/vnd.github+json`
     - `X-GitHub-Api-Version` → `2022-11-28`
   - **Corpo:** JSON
     ```json
     {
       "title": "add-link",
       "body": "[Entrada de Atalho]",
       "labels": ["add-link"]
     }
     ```
     (No campo "body", use a variável dinâmica **Entrada de atalho** do iOS, não o texto literal)

4. Adicione a ação **"Mostrar resultado"** com o texto "Link enviado ✅" (feedback visual).

5. Toque no nome do atalho (topo) e renomeie para **"Add to Growth Repo"**.

6. Toque nos três pontos (···) → **Adicionar à Tela de Início** e/ou **Aparecer no Share Sheet** (marque esta opção).

## Como usar

1. Abra qualquer link (YouTube, artigo, etc.) no Safari ou Chrome.
2. Toque no botão **Compartilhar** (quadrado com seta).
3. Role até encontrar **"Add to Growth Repo"** → toque.
4. Aguarde o feedback "Link enviado ✅".
5. Em 2–3 minutos, o arquivo aparece em `07-inbox/` e no feed mobile.

## Verificando se funcionou

- Acesse github.com/victorauad/claude-code-growth → aba **Issues** → você verá a issue criada (e fechada automaticamente após o processamento).
- Acesse o feed mobile para ver o card novo.

## Criando o label "add-link" no repo (uma vez só)

Acesse github.com/victorauad/claude-code-growth → Issues → Labels → New label → Nome: `add-link` → Cor: qualquer → Create label.
