# Meu Ministério

App de bíblia, ministério e anotações. Funciona offline, instala na tela
inicial, e guarda tudo no próprio aparelho — com nuvem opcional para
sincronizar entre aparelhos.

Desenvolvido a partir de três apps existentes de Alan Correa: a casca (aba,
gestos de arrastar e o botão de voltar) vem do **Planejar**; Relatório de
Campo, Revisitas e Estudo vêm do **Caderno — Meu Estudo Pessoal**; a leitura
livre da Bíblia é nova neste app.

## O que tem dentro

- **Bíblia** — os 66 livros, organizados como nas Escrituras Hebraico-Aramaicas
  e Gregas Cristãs. Toque num capítulo para marcar como "onde parei" e abrir
  a leitura direto na biblioteca do jw.org, numa aba nova. Este app **não**
  copia texto bíblico nenhum — ele só guarda em qual capítulo você está e
  leva você até lá.
- **Ministério** — um hub com três telas, portadas com todos os campos e
  cálculos do Caderno — Meu Estudo Pessoal:
  - *Relatório de Campo*: toque num dia do calendário para lançar horas,
    minutos e uma nota; meta do mês (Auxiliar Campanha, Auxiliar, Regular
    ou Especial) com anel e barra de progresso; créditos e abonos por
    categoria (Escola, LDC, Construção ou uma categoria "Outros" com nome
    próprio), somando automaticamente o que já foi lançado nos dias;
    contador de estudos bíblicos dirigidos; acompanhamento do ano de
    serviço (setembro a agosto, meta de 600 h) para quem é Pioneiro
    Regular; gráfico dos 12 meses do ano de serviço; e um gerador de
    mensagem do mês pronta para copiar ou enviar no WhatsApp.
  - *Revisitas*: nome, endereço, data do contato, data para retornar,
    anotações e etiquetas; filtros por "Esperando retorno", "Nesta
    semana" e "Todas"; ações rápidas "Voltei hoje" e "Adiar 7 dias"; e um
    aviso automático, ao abrir o app, de quantas revisitas estão
    vencidas.
  - *Estudo*: nome, telefone, data, endereço, publicação, lição, ponto,
    quem acompanhou, etiquetas e uma lista de observações (data + texto)
    que você vai acrescentando a cada estudo.
- **Notas** — escrita livre com data, tema, título e um modo leitura em
  tela cheia (mesmo recurso de Anotações do Planejar).
- **Listas** — check-lists simples, com itens que se marcam, editam e
  removem direto na tela.
- **Lembretes** — uma agenda de avisos geral (não só de revisitas): título,
  data e hora, repetição (não repetir, todo dia, toda semana ou todo mês) e
  aviso opcional no aparelho quando a hora chegar. Ao abrir o app, ele avisa
  se algum lembrete já venceu.
- **Agenda** — um calendário do mês com três marcadores de cor por dia:
  estudos com data marcada, revisitas para retornar e compromissos. Toque
  num dia para ver o que tem nele e criar revisita, estudo ou compromisso
  direto dali.
- **Aparência** — 6 cores, modo claro/escuro, 3 tamanhos de letra, 3
  estilos de letra (padrão, clássico ou arredondado) e ordem das abas
  configurável.
- **Conta e sincronização (opcional)** — ao entrar com e-mail/senha ou
  Google, Relatório, Revisitas, Estudo, Notas, Listas, Lembretes,
  compromissos da Agenda e o marcador da Bíblia passam a sincronizar entre
  os aparelhos onde você estiver logado. Sem conta, tudo continua
  funcionando normalmente, só neste aparelho.

## Navegação

A casca é idêntica à do Planejar: as abas ficam em pílulas roláveis logo
abaixo do cabeçalho (não numa barra fixa no rodapé), e arrastar a tela para
a esquerda ou direita troca de aba, na ordem escolhida em Ajustes → Ordem
das abas. O botão de voltar do celular fecha primeiro as janelas abertas
(folha ou modo leitura), depois volta ao Início, e só sai do app se você
tocar voltar de novo com o Início já na tela. A saudação da tela inicial é
personalizável: toque no seu nome (ou em "+ pôr meu nome") para editar.

## Arquivos

```
index.html       o aplicativo inteiro, em arquivo único
manifest.json    nome, ícones, cores e atalhos do ícone do celular
sw.js            service worker: offline e controle de atualização
instalar.html    página de instalação para compartilhar com alguém
firestore.rules  regras de segurança do Firestore (cada um só vê o próprio)
icons/           ícones 192, 512, maskable, apple-touch e favicon
.nojekyll        impede o GitHub Pages de processar os arquivos
```

## Como publicar no GitHub Pages

1. Crie um repositório novo (por exemplo `meu-ministerio`).
2. Envie **todos** os arquivos desta pasta, mantendo a pasta `icons` como está.
3. No repositório, vá em **Settings → Pages**.
4. Em *Source*, escolha **Deploy from a branch**; em *Branch*, escolha `main`
   e a pasta `/ (root)`.
5. Salve e espere um ou dois minutos. O endereço fica
   `https://SEU-USUARIO.github.io/meu-ministerio/`.

O service worker só funciona em `https`, que é o caso do GitHub Pages.

## Como instalar no celular

Abra o endereço no Chrome, toque nos três pontinhos e escolha
**Adicionar à tela inicial** — ou mande a pessoa para `instalar.html`, que
tem o passo a passo pronto para Android, iPhone e computador.

## Como ligar a sincronização na nuvem (Firebase)

Sem fazer nada, o app já funciona 100% sozinho no aparelho. Se você quiser
que Relatório, Revisitas, Estudo, Notas, Listas e o marcador da Bíblia
sincronizem entre aparelhos:

1. Vá a [console.firebase.google.com](https://console.firebase.google.com)
   e crie um projeto (gratuito no plano Spark, que já é suficiente aqui).
2. Em **Build → Authentication → Sign-in method**, ative **E-mail/senha**
   e, se quiser, **Google**.
3. Em **Build → Firestore Database**, crie o banco (modo produção).
4. Em **Firestore → Regras**, cole o conteúdo do arquivo
   `firestore.rules` deste projeto e publique.
5. Em **Configurações do projeto → Geral → Seus apps**, crie um app da
   Web e copie o objeto `firebaseConfig` que aparece.
6. Abra `index.html`, procure por `window.__FIREBASE_CONFIG__` (perto do
   fim do `<head>`) e troque os valores de exemplo pelos que você copiou.
7. Publique o arquivo atualizado. Pronto — a tela de Ajustes passa a
   mostrar login em vez do aviso de "sincronização não configurada".

Essas chaves não são segredo — todo app Firebase do lado do cliente as
expõe. Quem protege os dados são as **regras do Firestore** do passo 4, que
garantem que cada conta só lê e escreve o próprio documento.

## Como publicar uma alteração

Sempre que mudar o `index.html`, abra o `sw.js` e troque a versão na
primeira linha:

```js
const VERSAO = 'meuministerio-v1.2.1';
```

Sem isso o celular continua mostrando a versão antiga guardada em cache.
Com a versão nova, o app avisa "Nova versão pronta — Atualizar".

## Onde ficam os dados

Localmente, tudo fica no `localStorage` do navegador, na chave
`meuministerio_v1`. Sem conta, nada sai do aparelho — limpar os dados do
navegador apaga tudo, e trocar de celular não leva nada junto (por isso o
**Ajustes → Cópia de segurança** exporta um `.json` de backup).

Com conta, os mesmos dados também ficam no Firestore, num documento por
usuário (`meuministerio_usuarios/{uid}`). A sincronização é a mesma
estratégia usada no Caderno: cada item (revisita, estudo, nota, item de
lista, lembrete, compromisso) carrega a hora da última alteração, e ao
sincronizar dois aparelhos o item mais recente vence — sem isso, o último
a sincronizar apagaria o trabalho do outro.

## Dependências externas

- **Google Fonts** (Fraunces, Nunito e Quicksand, para os estilos de letra)
  — sem internet, o app usa as letras do sistema (o estilo "Clássico" usa
  Georgia, que já vem com o aparelho).
- **SDK do Firebase** (`gstatic.com`), só carregado de verdade quando você
  configura suas credenciais.
- **jw.org** — é para lá que os links de cada capítulo apontam; a leitura
  em si acontece no navegador, fora do app.

## Limitações conhecidas (por design, para manter o app simples)

- Os avisos (lembretes e revisitas vencidas) usam a `Notification API` do
  navegador dentro da própria sessão, mesmo esquema do Planejar e do
  Caderno — não é um push de verdade em segundo plano; funciona bem se o
  aparelho tende a manter o app aberto ou for reaberto perto do horário.
  `avisarRevisitas` roda uma vez ao abrir o app; `agendaAvisos` reagenda os
  lembretes com aviso ligado sempre que o app volta ao primeiro plano.
- A sincronização é "o mais recente vence" por item. Editar a mesma
  revisita, estudo, lembrete, compromisso ou dia do relatório em dois
  aparelhos ao mesmo tempo, offline nos dois, faz o aparelho que
  sincronizar por último prevalecer para aquele item.
