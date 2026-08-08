Analise o documento anexo.

O documento contém uma proposta de governança e organização do conhecimento previamente elaborada para o repositório MIT.

Considere esse documento como referência arquitetural aprovada para esta análise.

Com base na proposta apresentada no documento anexo, e sem reorganizar diretórios existentes, proponha o conteúdo inicial do arquivo KNOWLEDGE\_MODEL.md.

Objetivos do KNOWLEDGE\_MODEL.md:

- Definir a separação entre Programa/Portfólio e Projeto.
- Definir o modelo de governança de conhecimento.
- Definir o princípio de memória institucional.
- Definir os níveis de conhecimento existentes no repositório.
- Definir quais artefatos pertencem ao nível Programa.
- Definir quais artefatos pertencem ao nível Projeto.
- Definir a ordem recomendada de assimilação para agentes de IA, Codex e colaboradores humanos.
- Definir as regras de herança de conhecimento entre Programa e Projeto.
- Preservar a estrutura atual do repositório.

Importante:

- O documento deve ser tratado como um artefato fundador da governança do MIT AI Program Office.
- O conteúdo deve ser escrito em formato Markdown.
- O documento deve ser adequado para leitura por humanos e agentes de IA.
- O documento deve privilegiar clareza, governança e evolução futura do portfólio.

Não altere arquivos.
Não abra Pull Request.
Não implemente mudanças.

Apenas apresente a proposta completa do conteúdo de KNOWLEDGE\_MODEL.md para revisão humana.
Copiar
Abaixo está a proposta completa de conteúdo inicial para KNOWLEDGE_MODEL.md, em Markdown, preservando a estrutura atual do repositório e tratando o documento como artefato fundador de governança do MIT AI Program Office.

# KNOWLEDGE_MODEL.md

## MIT AI Program Office — Modelo de Conhecimento e Governança

Este documento define o modelo inicial de organização, governança e assimilação do conhecimento do repositório MIT.

Ele deve ser tratado como um artefato fundador da governança do **MIT AI Program Office** e serve como referência para colaboradores humanos, agentes de IA, Codex e demais sistemas automatizados que interajam com este repositório.

O objetivo deste documento não é reorganizar diretórios existentes, mas estabelecer uma interpretação comum sobre os níveis de conhecimento já presentes ou futuros no repositório, bem como orientar sua evolução de forma consistente.

---

## 1. Propósito

O `KNOWLEDGE_MODEL.md` tem como objetivos:

- Definir a separação conceitual entre **Programa/Portfólio** e **Projeto**.
- Estabelecer um modelo de governança de conhecimento para o repositório MIT.
- Preservar memória institucional e contexto histórico.
- Definir níveis de conhecimento aplicáveis ao repositório.
- Identificar quais artefatos pertencem ao nível de Programa.
- Identificar quais artefatos pertencem ao nível de Projeto.
- Definir uma ordem recomendada de assimilação para:
  - agentes de IA;
  - Codex;
  - colaboradores humanos;
  - revisores técnicos;
  - mantenedores do portfólio.
- Definir regras de herança de conhecimento entre Programa e Projeto.
- Preservar a estrutura atual do repositório, evitando reorganizações prematuras.

---

## 2. Princípios orientadores

A governança de conhecimento do repositório MIT é guiada pelos seguintes princípios:

### 2.1 Clareza antes de automação

A automação deve operar sobre conhecimento explícito, legível e governado.

Antes de adicionar novas automações, agentes, scripts ou integrações, o repositório deve manter clareza sobre:

- o propósito do artefato;
- o nível de conhecimento ao qual ele pertence;
- sua relação com o Programa;
- sua relação com projetos específicos;
- sua relevância para agentes humanos e automatizados.

---

### 2.2 Preservação da estrutura existente

Este modelo não exige reorganização física imediata do repositório.

A governança deve ser introduzida por documentação, convenções e regras de interpretação, preservando os diretórios existentes.

Mudanças estruturais futuras somente devem ocorrer quando:

- houver consenso arquitetural;
- o impacto sobre projetos existentes for compreendido;
- a migração puder ser feita sem perda de contexto;
- a nova estrutura trouxer ganho claro de governança, manutenção ou assimilação.

---

### 2.3 Separação entre conhecimento programático e conhecimento projetual

O repositório pode conter artefatos em diferentes níveis de abstração.

Nem todo artefato técnico pertence ao mesmo nível de governança.

Este documento estabelece a separação entre:

- **Programa/Portfólio**: conhecimento transversal, institucional, estratégico ou comum a múltiplos projetos.
- **Projeto**: conhecimento específico de uma iniciativa, implementação, produto, experimento ou sistema.

Essa separação é conceitual e governamental, não necessariamente física.

---

### 2.4 Memória institucional como ativo do Programa

A memória institucional é parte essencial do MIT AI Program Office.

Ela inclui decisões, aprendizados, convenções, justificativas, restrições, riscos conhecidos, padrões adotados e contexto histórico.

Essa memória deve ser preservada para reduzir retrabalho, evitar perda de racionalidade arquitetural e permitir que novos colaboradores — humanos ou agentes de IA — assimilem o repositório com segurança.

---

### 2.5 Evolução incremental

O modelo de conhecimento deve permitir evolução progressiva.

A governança deve ser suficientemente clara para orientar decisões atuais, mas flexível para acomodar novos projetos, agentes, metodologias, documentos e práticas futuras.

O objetivo é criar uma base estável, não uma estrutura rígida.

---

## 3. Definições fundamentais

### 3.1 Programa

O **Programa** representa o nível institucional e estratégico do repositório MIT.

Ele consolida conhecimento que orienta o conjunto do portfólio, incluindo:

- visão geral;
- princípios;
- governança;
- padrões;
- decisões arquiteturais;
- convenções de trabalho;
- diretrizes para agentes de IA;
- memória institucional;
- regras de assimilação;
- critérios para evolução do portfólio.

O Programa não é um único projeto. Ele é a camada de coordenação e coerência entre múltiplos projetos.

---

### 3.2 Portfólio

O **Portfólio** é o conjunto de projetos, experimentos, protótipos, bots, agentes, integrações, documentos e iniciativas mantidos no repositório MIT.

No contexto deste documento, **Programa** e **Portfólio** são conceitos relacionados:

- o **Programa** define a governança, princípios e direção;
- o **Portfólio** representa o conjunto de iniciativas sob essa governança.

Assim, o Programa governa o Portfólio.

---

### 3.3 Projeto

Um **Projeto** é uma unidade de trabalho específica dentro do Portfólio.

Um projeto pode conter:

- código-fonte;
- documentação própria;
- scripts;
- configurações;
- experimentos;
- planos de implementação;
- arquivos operacionais;
- dados de exemplo;
- instruções específicas;
- decisões técnicas locais.

Um projeto deve respeitar as diretrizes de Programa, salvo quando houver decisão documentada em contrário.

---

### 3.4 Artefato

Um **Artefato** é qualquer elemento versionado ou documentado que contribua para o conhecimento do repositório.

Exemplos:

- arquivos Markdown;
- código-fonte;
- scripts;
- configurações;
- planos de implementação;
- documentos de arquitetura;
- arquivos de requisitos;
- instruções operacionais;
- decisões técnicas;
- registros de sessão;
- exemplos;
- documentação de personas, agentes ou workflows.

---

### 3.5 Agente de IA

Um **Agente de IA** é qualquer sistema automatizado que leia, interprete, modifique, analise ou gere conteúdo com base no repositório.

Isso inclui, mas não se limita a:

- Codex;
- assistentes de programação;
- agentes de documentação;
- agentes de revisão;
- bots operacionais;
- sistemas de análise automatizada;
- pipelines de geração ou manutenção de conhecimento.

Agentes de IA devem tratar este documento como referência de contexto institucional.

---

## 4. Separação entre Programa/Portfólio e Projeto

A separação entre Programa/Portfólio e Projeto é central para evitar confusão entre diretrizes institucionais e decisões locais.

---

### 4.1 Nível Programa/Portfólio

Pertencem ao nível Programa/Portfólio os artefatos que:

- orientam mais de um projeto;
- definem governança;
- estabelecem princípios institucionais;
- descrevem o modelo de conhecimento;
- documentam decisões transversais;
- definem padrões reutilizáveis;
- orientam a assimilação por agentes e humanos;
- preservam memória institucional;
- registram regras de evolução do portfólio;
- definem políticas de organização, manutenção ou documentação.

Esses artefatos têm precedência conceitual sobre artefatos de projeto, salvo exceções explicitamente documentadas.

---

### 4.2 Nível Projeto

Pertencem ao nível Projeto os artefatos que:

- dizem respeito a uma iniciativa específica;
- descrevem uma implementação local;
- documentam decisões técnicas restritas a um diretório, bot, agente ou produto;
- definem comandos, dependências ou fluxos específicos;
- registram sessões, planos ou contextos de execução de um projeto;
- contêm código-fonte ou configuração de uma aplicação específica;
- descrevem personas, comportamentos ou recursos pertencentes a um projeto delimitado.

Esses artefatos devem ser interpretados dentro do escopo do projeto ao qual pertencem.

---

### 4.3 Regra geral de classificação

Quando houver dúvida sobre o nível de um artefato, aplicar a seguinte pergunta:

> Este artefato governa o portfólio como um todo ou apenas uma iniciativa específica?

Se governa o portfólio como um todo, é um artefato de Programa.

Se orienta apenas uma iniciativa delimitada, é um artefato de Projeto.

Se o artefato contém ambos os tipos de conhecimento, ele deve explicitar suas seções programáticas e projetuais ou ser futuramente dividido mediante decisão governada.

---

## 5. Modelo de governança de conhecimento

O modelo de governança de conhecimento do repositório MIT é organizado em camadas.

Cada camada possui um papel específico na preservação, interpretação e evolução do conhecimento.

---

## 6. Níveis de conhecimento do repositório

O repositório reconhece os seguintes níveis de conhecimento:

1. **Conhecimento Institucional**
2. **Conhecimento de Governança**
3. **Conhecimento Arquitetural**
4. **Conhecimento de Portfólio**
5. **Conhecimento de Projeto**
6. **Conhecimento Operacional**
7. **Conhecimento de Execução**
8. **Conhecimento Histórico**

---

### 6.1 Conhecimento Institucional

Representa a identidade, propósito e princípios do MIT AI Program Office.

Inclui:

- missão;
- visão;
- princípios de governança;
- escopo do Programa;
- vocabulário institucional;
- responsabilidades de alto nível;
- critérios de coerência do portfólio.

Este conhecimento deve ser estável e alterado apenas mediante revisão consciente.

---

### 6.2 Conhecimento de Governança

Define como o conhecimento deve ser criado, interpretado, mantido e evoluído.

Inclui:

- regras de classificação entre Programa e Projeto;
- regras de herança;
- diretrizes para documentação;
- diretrizes para agentes de IA;
- critérios para criação de novos artefatos;
- critérios para alteração de artefatos existentes;
- regras de precedência entre documentos.

O `KNOWLEDGE_MODEL.md` pertence a este nível.

---

### 6.3 Conhecimento Arquitetural

Define decisões estruturais, padrões e justificativas técnicas ou organizacionais.

Inclui:

- decisões de arquitetura;
- modelos de integração;
- padrões de organização;
- modelos de agentes;
- dependências conceituais;
- restrições técnicas;
- critérios de modularidade;
- estratégias de evolução.

Esse conhecimento pode existir tanto no nível Programa quanto no nível Projeto.

Quando for transversal, pertence ao Programa.

Quando for específico, pertence ao Projeto.

---

### 6.4 Conhecimento de Portfólio

Representa o mapa das iniciativas existentes no repositório.

Inclui:

- lista de projetos;
- objetivos de cada projeto;
- relações entre projetos;
- status de maturidade;
- dependências entre iniciativas;
- critérios de priorização;
- histórico de evolução do conjunto.

Esse nível permite compreender o repositório como um ecossistema, e não como arquivos isolados.

---

### 6.5 Conhecimento de Projeto

Representa o conhecimento necessário para compreender, executar, manter e evoluir um projeto específico.

Inclui:

- README do projeto;
- planos de implementação;
- código-fonte;
- documentação local;
- dependências;
- comandos de execução;
- configurações;
- decisões técnicas locais;
- escopo funcional;
- limitações conhecidas;
- instruções de manutenção.

Esse conhecimento deve ser consistente com o nível Programa.

---

### 6.6 Conhecimento Operacional

Representa instruções práticas para execução, teste, manutenção e operação.

Inclui:

- comandos de instalação;
- comandos de teste;
- variáveis de ambiente;
- procedimentos de deploy;
- scripts operacionais;
- fluxos de uso;
- instruções para diagnóstico;
- tarefas recorrentes.

Esse conhecimento normalmente pertence ao nível Projeto, exceto quando define práticas comuns a todo o repositório.

---

### 6.7 Conhecimento de Execução

Representa registros ou artefatos produzidos durante a execução de agentes, bots, sessões ou experimentos.

Inclui:

- logs;
- sessões;
- arquivos de estado;
- resultados intermediários;
- saídas de agentes;
- snapshots de execução;
- registros de conversas ou interações;
- evidências temporais.

Esse conhecimento pode ter valor histórico, mas deve ser claramente diferenciado de documentação normativa.

---

### 6.8 Conhecimento Histórico

Representa o registro da evolução do Programa e dos Projetos.

Inclui:

- decisões anteriores;
- planos antigos;
- mudanças de direção;
- justificativas de refatoração;
- experimentos encerrados;
- aprendizados;
- contexto de decisões;
- versões anteriores de propostas.

O conhecimento histórico não deve ser descartado sem avaliação, pois pode conter racionalidade institucional útil.

---

## 7. Artefatos do nível Programa

Os artefatos de Programa devem orientar o repositório como um todo.

Exemplos de artefatos pertencentes ao nível Programa:

- `README.md` raiz, quando usado como visão geral do repositório.
- `KNOWLEDGE_MODEL.md`.
- Documentos de governança.
- Documentos de arquitetura transversal.
- Documentos de princípios do MIT AI Program Office.
- Mapas do portfólio.
- Diretrizes para agentes de IA.
- Convenções gerais de documentação.
- Convenções gerais de contribuição.
- Registros de decisões arquiteturais transversais.
- Documentos de taxonomia e vocabulário comum.
- Políticas de evolução do repositório.
- Instruções comuns para assimilação por agentes.
- Estratégias de memória institucional.

Artefatos de Programa devem evitar detalhes excessivamente locais de implementação, salvo quando necessários para explicar uma decisão transversal.

---

## 8. Artefatos do nível Projeto

Os artefatos de Projeto pertencem ao escopo de uma iniciativa específica.

Exemplos de artefatos pertencentes ao nível Projeto:

- README local de um projeto.
- Código-fonte de uma aplicação, bot, agente ou serviço.
- Scripts específicos.
- Arquivos de configuração específicos.
- Planos de implementação locais.
- Documentação funcional local.
- Documentação técnica local.
- Arquivos de dependências.
- Arquivos de ambiente.
- Registros de sessão específicos.
- Documentação de personas ou comportamentos específicos de um projeto.
- Testes locais.
- Dados de exemplo ou fixtures específicos.
- Instruções operacionais de execução local.

Artefatos de Projeto podem estender o conhecimento de Programa, mas não devem contradizê-lo sem justificativa explícita.

---

## 9. Ordem recomendada de assimilação

Esta seção define a ordem recomendada de leitura para agentes de IA, Codex e colaboradores humanos.

A assimilação correta do conhecimento reduz erros de interpretação, evita mudanças desalinhadas e preserva coerência institucional.

---

### 9.1 Ordem geral de assimilação

Ao iniciar trabalho no repositório, recomenda-se a seguinte ordem:

1. **Modelo de Conhecimento**
   - Ler `KNOWLEDGE_MODEL.md`.
   - Entender a separação entre Programa e Projeto.
   - Identificar regras de governança e herança.

2. **Visão geral do repositório**
   - Ler o `README.md` raiz, quando existente.
   - Identificar o propósito geral do repositório.
   - Compreender quais projetos compõem o portfólio.

3. **Documentos de Programa**
   - Ler documentos transversais de governança, arquitetura e princípios.
   - Identificar diretrizes aplicáveis a todos os projetos.

4. **Mapa de Portfólio**
   - Identificar projetos existentes.
   - Entender relações, escopos e dependências entre eles.

5. **Documentação do Projeto alvo**
   - Ler o README local do projeto.
   - Ler documentação técnica e funcional do projeto.
   - Identificar comandos, dependências e limitações locais.

6. **Artefatos operacionais**
   - Ler arquivos de configuração.
   - Ler scripts.
   - Ler instruções de execução e teste.
   - Identificar variáveis de ambiente e dependências.

7. **Código-fonte e implementação**
   - Analisar o código somente após compreender o contexto documental.
   - Relacionar decisões de implementação com documentação existente.

8. **Histórico e registros auxiliares**
   - Consultar planos, sessões, logs ou decisões anteriores quando necessário.
   - Tratar esses registros como contexto, não necessariamente como norma vigente.

---

### 9.2 Ordem recomendada para agentes de IA e Codex

Agentes de IA devem seguir uma ordem de assimilação explícita antes de propor ou realizar alterações.

#### Etapa 1 — Contexto institucional

O agente deve identificar:

- qual é o Programa;
- qual é o Portfólio;
- qual é o Projeto alvo;
- quais documentos têm precedência;
- quais regras de governança se aplicam.

#### Etapa 2 — Escopo da tarefa

O agente deve determinar:

- se a tarefa afeta o Programa;
- se a tarefa afeta apenas um Projeto;
- se a tarefa altera conhecimento normativo;
- se a tarefa altera conhecimento operacional;
- se a tarefa cria novo artefato;
- se a tarefa exige atualização documental.

#### Etapa 3 — Herança aplicável

O agente deve verificar:

- quais regras de Programa são herdadas pelo Projeto;
- se há instruções locais mais específicas;
- se existe conflito entre diretrizes;
- se o conflito exige esclarecimento humano.

#### Etapa 4 — Execução controlada

O agente deve:

- preservar a estrutura existente;
- evitar reorganizações não solicitadas;
- modificar apenas arquivos necessários;
- registrar alterações de forma clara;
- atualizar documentação quando a mudança afetar conhecimento compartilhado;
- evitar transformar registros históricos em normas sem validação.

#### Etapa 5 — Síntese

Ao concluir uma análise ou alteração, o agente deve informar:

- quais arquivos foram considerados;
- qual nível de conhecimento foi afetado;
- quais decisões foram tomadas;
- quais comandos foram executados, quando aplicável;
- quais riscos, limitações ou pendências permanecem.

---

### 9.3 Ordem recomendada para colaboradores humanos

Colaboradores humanos devem assimilar o repositório na seguinte ordem:

1. Ler o `KNOWLEDGE_MODEL.md`.
2. Ler o `README.md` raiz.
3. Identificar o projeto ou área de interesse.
4. Ler a documentação local do projeto.
5. Executar ou testar o projeto conforme instruções locais.
6. Consultar documentos históricos ou planos quando necessário.
7. Propor alterações respeitando a separação entre Programa e Projeto.

---

## 10. Regras de herança de conhecimento

A herança de conhecimento define como diretrizes de Programa se aplicam aos Projetos.

---

### 10.1 Regra de precedência

O conhecimento de Programa tem precedência sobre o conhecimento de Projeto quando tratar de:

- governança;
- princípios institucionais;
- padrões transversais;
- taxonomia;
- regras de documentação;
- regras de assimilação;
- memória institucional;
- critérios de evolução do portfólio.

O conhecimento de Projeto tem precedência apenas dentro de seu escopo local quando tratar de:

- comandos específicos;
- dependências específicas;
- implementação local;
- detalhes operacionais locais;
- escolhas técnicas justificadas para aquele projeto.

---

### 10.2 Regra de especialização

Projetos podem especializar diretrizes de Programa, desde que:

- a especialização seja documentada;
- a justificativa esteja clara;
- o escopo da exceção seja delimitado;
- não comprometa princípios institucionais;
- não crie ambiguidade para outros projetos.

Exemplo:

> O Programa pode definir que todos os projetos devem documentar instruções de execução.
> Um Projeto pode definir comandos específicos de execução conforme sua tecnologia.

---

### 10.3 Regra de não contradição

Projetos não devem contradizer diretrizes de Programa sem registrar uma exceção explícita.

Quando houver contradição aparente:

1. verificar se a regra de Programa ainda está vigente;
2. verificar se o Projeto documenta uma exceção;
3. verificar se a exceção é local e justificada;
4. se não houver justificativa, tratar como desalinhamento;
5. solicitar revisão humana antes de consolidar mudanças estruturais.

---

### 10.4 Regra de propagação

Quando uma decisão local de Projeto demonstrar valor para múltiplos projetos, ela pode ser promovida ao nível Programa.

A promoção deve ocorrer quando:

- a prática se tornar reutilizável;
- houver benefício transversal;
- a decisão impactar governança;
- a decisão afetar padrões de documentação;
- a decisão orientar agentes ou colaboradores em mais de um projeto.

A promoção não deve ocorrer automaticamente.

Ela exige revisão humana e documentação explícita.

---

### 10.5 Regra de contenção

Nem todo conhecimento de Projeto deve se tornar conhecimento de Programa.

Detalhes locais devem permanecer no projeto quando:

- forem específicos de uma implementação;
- não forem reutilizáveis;
- dependerem de contexto operacional local;
- forem experimentais;
- não tiverem maturidade suficiente;
- não forem necessários para outros projetos.

Essa regra evita que o Programa se torne excessivamente detalhado ou instável.

---

### 10.6 Regra de memória institucional

Decisões relevantes devem preservar sua justificativa.

Sempre que uma decisão alterar governança, arquitetura, organização do conhecimento ou direção do portfólio, deve-se registrar:

- o que foi decidido;
- por que foi decidido;
- quais alternativas foram consideradas, quando aplicável;
- quais impactos são esperados;
- quais riscos foram aceitos;
- qual escopo é afetado;
- se a decisão pertence ao Programa ou a um Projeto.

A ausência de justificativa enfraquece a memória institucional.

---

## 11. Princípio de memória institucional

A memória institucional do MIT AI Program Office deve ser preservada como parte do conhecimento vivo do repositório.

---

### 11.1 O que deve ser preservado

Devem ser preservados:

- decisões arquiteturais relevantes;
- justificativas de governança;
- mudanças de direção;
- critérios de organização;
- aprendizados obtidos em projetos;
- padrões consolidados;
- exceções aprovadas;
- limitações conhecidas;
- riscos recorrentes;
- histórico de propostas relevantes;
- contexto necessário para futuros agentes e colaboradores.

---

### 11.2 O que não deve ser tratado como memória normativa

Nem todo registro histórico é uma regra vigente.

Não devem ser automaticamente tratados como norma:

- logs antigos;
- sessões temporárias;
- rascunhos;
- experimentos abandonados;
- propostas não aprovadas;
- saídas intermediárias de agentes;
- notas sem validação;
- arquivos gerados automaticamente;
- estados transitórios.

Esses elementos podem ser úteis como contexto, mas não devem prevalecer sobre documentos de governança.

---

### 11.3 Memória viva

A memória institucional deve ser viva, mas governada.

Isso significa que ela pode evoluir, desde que mudanças relevantes:

- sejam explícitas;
- sejam revisáveis;
- preservem contexto;
- evitem apagar racionalidade histórica sem substituição;
- mantenham compatibilidade com a visão do Programa.

---

## 12. Preservação da estrutura atual do repositório

Este documento não determina alteração da estrutura física atual do repositório.

A estrutura existente deve ser preservada até que haja uma decisão específica de reorganização.

---

### 12.1 Diretrizes de preservação

Ao trabalhar no repositório:

- não mover diretórios sem solicitação explícita;
- não renomear projetos sem decisão documentada;
- não consolidar projetos apenas por similaridade superficial;
- não dividir projetos sem análise de impacto;
- não transformar convenções locais em globais sem revisão;
- não remover artefatos históricos sem avaliação;
- não introduzir nova hierarquia de diretórios apenas para adequação estética.

---

### 12.2 Governança antes de reorganização

Antes de qualquer reorganização estrutural futura, recomenda-se produzir:

- justificativa;
- escopo da mudança;
- impactos esperados;
- projetos afetados;
- plano de migração;
- riscos;
- critérios de sucesso;
- plano de rollback, quando aplicável.

---

## 13. Critérios para criação de novos artefatos

Antes de criar um novo artefato, deve-se responder:

1. Este artefato pertence ao Programa ou a um Projeto?
2. Ele é normativo, explicativo, operacional ou histórico?
3. Quem deve lê-lo?
4. Ele duplica conhecimento existente?
5. Ele deve herdar regras de outro documento?
6. Ele precisa ser citado por agentes de IA?
7. Ele deve ser estável ou experimental?
8. Ele afeta apenas uma iniciativa ou o portfólio inteiro?

---

### 13.1 Artefatos normativos

Artefatos normativos definem regras, políticas ou diretrizes.

Eles devem:

- ser claros;
- indicar escopo;
- evitar ambiguidade;
- declarar precedência;
- ser mantidos com cuidado;
- evitar detalhes transitórios.

---

### 13.2 Artefatos explicativos

Artefatos explicativos ajudam a compreender decisões, sistemas ou projetos.

Eles devem:

- contextualizar;
- explicar racionalidade;
- conectar conceitos;
- facilitar assimilação;
- evitar impor regras quando não forem normativos.

---

### 13.3 Artefatos operacionais

Artefatos operacionais orientam execução prática.

Eles devem:

- ser atualizados conforme o funcionamento real;
- conter comandos concretos;
- indicar dependências;
- indicar pré-requisitos;
- distinguir ambiente local, teste e produção, quando aplicável.

---

### 13.4 Artefatos históricos

Artefatos históricos preservam contexto.

Eles devem:

- indicar data ou contexto quando possível;
- evitar ambiguidade com normas vigentes;
- ser consultáveis;
- não substituir documentos governados.

---

## 14. Diretrizes para agentes de IA

Agentes de IA devem operar de forma conservadora em relação à governança do conhecimento.

---

### 14.1 Antes de alterar

Antes de propor ou realizar alterações, o agente deve:

- identificar o escopo da tarefa;
- localizar documentos relevantes;
- verificar se há instruções de Programa;
- verificar se há instruções locais de Projeto;
- preservar estrutura existente;
- evitar alterações não solicitadas;
- diferenciar análise, proposta e implementação.

---

### 14.2 Durante a alteração

Durante a alteração, o agente deve:

- modificar apenas o necessário;
- manter consistência com o nível de conhecimento afetado;
- atualizar documentação relacionada quando apropriado;
- não promover conhecimento local ao Programa sem justificativa;
- não apagar memória institucional sem autorização;
- registrar claramente a intenção da mudança.

---

### 14.3 Após a alteração

Após a alteração, o agente deve relatar:

- resumo da mudança;
- arquivos afetados;
- nível de conhecimento afetado;
- testes ou verificações executadas;
- limitações encontradas;
- pendências para revisão humana.

---

## 15. Diretrizes para evolução futura do portfólio

A evolução futura do portfólio deve respeitar a separação entre governança e implementação.

Novos projetos podem ser adicionados sem alterar este modelo, desde que sejam classificados corretamente e documentem seu escopo.

Novos documentos de Programa podem ser criados quando houver necessidade de:

- consolidar decisões transversais;
- definir políticas;
- registrar princípios;
- orientar múltiplos projetos;
- melhorar assimilação por humanos e agentes;
- reduzir ambiguidade institucional.

Novos documentos de Projeto podem ser criados quando houver necessidade de:

- explicar uma implementação;
- registrar comandos locais;
- documentar decisões específicas;
- orientar manutenção;
- preservar contexto técnico local.

---

## 16. Critérios de revisão humana

Mudanças em documentos de Programa devem receber revisão humana quando:

- alterarem regras de governança;
- redefinirem níveis de conhecimento;
- mudarem precedência entre documentos;
- criarem novas responsabilidades;
- afetarem múltiplos projetos;
- promoverem decisões locais ao nível Programa;
- alterarem princípios de memória institucional.

Mudanças em documentos de Projeto devem receber revisão humana quando:

- afetarem execução;
- alterarem arquitetura local;
- criarem dependências relevantes;
- modificarem comportamento funcional;
- introduzirem exceções às regras de Programa;
- impactarem outros projetos.

---

## 17. Tabela de referência rápida

| Dimensão | Programa/Portfólio | Projeto |
|---|---|---|
| Escopo | Transversal | Local |
| Finalidade | Governar e coordenar | Implementar e operar |
| Estabilidade | Maior | Variável |
| Exemplos | Governança, princípios, arquitetura transversal | Código, README local, scripts, configs |
| Precedência | Alta para regras gerais | Alta apenas no escopo local |
| Público | Todos os colaboradores e agentes | Colaboradores do projeto |
| Mudança | Requer maior cautela | Pode evoluir com o projeto |
| Memória | Institucional | Técnica e contextual |

---

## 18. Estado inicial deste modelo

Este documento estabelece o modelo inicial de conhecimento do repositório MIT.

Ele não implica reorganização imediata de arquivos ou diretórios.

Ele deve ser usado como referência para:

- interpretar artefatos existentes;
- orientar novos documentos;
- guiar agentes de IA;
- apoiar revisões humanas;
- preservar memória institucional;
- evoluir o portfólio de forma governada.

---

## 19. Declaração de governança

O repositório MIT deve ser compreendido como um portfólio em evolução sob governança do MIT AI Program Office.

A clareza entre Programa e Projeto é essencial para permitir crescimento sustentável, colaboração humana, operação por agentes de IA e preservação da memória institucional.

Este modelo deve evoluir conforme o portfólio amadurece, sempre preservando a rastreabilidade das decisões e a coerência entre os níveis de conhecimento.
Verificações realizadas

✅ pwd && find .. -name AGENTS.md -print && rg -n "governança|governanca|KNOWLEDGE|Programa|Portfólio|Portfolio|MIT AI Program Office" -S . --glob '!node_modules' --glob '!vendor'

✅ find . -maxdepth 3 -type f | sed 's#^./##' | sort | head -200

✅ git status --short && find /workspace -name AGENTS.md -print

Nenhum arquivo foi alterado, nenhum commit foi criado e nenhum Pull Request foi aberto.

Utilize a resposta anterior contendo a proposta de governança aprovada como referência arquitetural. Com base nesse documento, crie o arquivo `KNOWLEDGE_MODEL.md`. Preserve a estrutura atual do repositório. Não altere outros arquivos. Abra um Draft Pull Request e aguarde revisão humana.
Copiar
Summary

Criei o arquivo KNOWLEDGE_MODEL.md na raiz do repositório, preservando a estrutura atual e sem alterar outros arquivos. O documento estabelece o modelo fundador de governança e organização do conhecimento do MIT AI Program Office. 

Documentei os objetivos centrais do modelo, incluindo separação entre Programa/Portfólio e Projeto, memória institucional, níveis de conhecimento, ordem de assimilação e regras de herança. 

Incluí a distinção conceitual entre conhecimento programático e projetual, com preservação explícita da estrutura existente do repositório. 

Defini Programa, Portfólio, Projeto, Artefato e Agente de IA como conceitos fundamentais para leitura humana e por agentes automatizados. 

Adicionei os níveis de conhecimento reconhecidos no repositório e o enquadramento do KNOWLEDGE_MODEL.md como conhecimento de governança. 

Incluí a ordem recomendada de assimilação para agentes de IA, Codex e colaboradores humanos. 

Documentei regras de herança, precedência, especialização, não contradição, propagação, contenção e memória institucional entre Programa e Projeto. 

Reforcei as diretrizes para preservar a estrutura atual do repositório e evitar reorganizações não solicitadas. 

Adicionei critérios para evolução futura do portfólio, revisão humana e tabela de referência rápida entre Programa/Portfólio e Projeto. 

Realizei o commit 09e6d0e Add knowledge governance model.

Testing

✅ git diff -- KNOWLEDGE_MODEL.md && git status --short && git add KNOWLEDGE_MODEL.md && git commit -m "Add knowledge governance model"

✅ git status --short && git log -1 --oneline

⚠️ `gh pr create --draft --title "Add knowledge governance model" --body "## Summary

Add KNOWLEDGE_MODEL.md as the founding governance and knowledge model for the MIT AI Program Office.

Define Program/Portfolio versus Project knowledge levels, inheritance rules, institutional memory, assimilation order, and repository preservation principles.

Testing
Documentation-only change; no automated tests run." — não foi possível abrir o Draft Pull Request porque o GitHub CLI não está autenticado no ambiente (gh auth login/GH_TOKEN` ausente).


Arquivo (1)

KNOWLEDGE_MODEL.md
KNOWLEDGE_MODEL.md
Novo