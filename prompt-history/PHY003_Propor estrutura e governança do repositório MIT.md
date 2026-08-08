Analise o repositório MIT.

Considere que este repositório deverá evoluir para suportar:

- um Program Office (MIT AI Program Office);
- múltiplos projetos independentes;
- governança de conhecimento;
- memória institucional;
- protocolos operacionais;
- decisões arquiteturais e de governança;
- assimilação por agentes de IA, Codex e colaboradores humanos.

Com base exclusivamente no conteúdo atualmente existente no repositório, proponha:

1. Estrutura de diretórios recomendada.
2. Estrutura de governança recomendada.
3. Artefatos fundamentais que deveriam existir na raiz do repositório.
4. Artefatos que deveriam existir em nível Programa/Portfólio.
5. Artefatos que deveriam existir em nível Projeto.
6. Regras de separação entre conhecimento de Programa e conhecimento de Projeto.
7. Ordem recomendada de assimilação para agentes.

Para cada recomendação, explique a justificativa.

Não altere nenhum arquivo.
Não abra Pull Request.
Não crie documentos.
Não implemente mudanças.

Apenas apresente sua proposta e aguarde aprovação humana.
Copiar
Premissas da análise
Não alterei arquivos, não criei documentos, não fiz commit e não abri Pull Request, conforme solicitado.

A proposta abaixo foi construída exclusivamente a partir do conteúdo atualmente existente no repositório.

O repositório hoje contém uma raiz conceitual ampla (MIT) descrita como trabalhos e insights do curso de IA Agêntica aplicada à transformação empresarial. 

O conteúdo mais estruturado está no projeto avalbot, que já aponta para múltiplas personas, governança, arquitetura modular, sessões, roadmap, releases, Azure e uso por Discord/Groq. 

Há também um projeto/protótipo dbot, com um bot Discord/Groq mais simples, aparentemente anterior ou experimental, focado em um “pirate bot”. 

1. Estrutura de diretórios recomendada
Proposta
MIT/
├── README.md
├── AGENTS.md
├── GOVERNANCE.md
├── PROGRAM_CHARTER.md
├── KNOWLEDGE_MAP.md
├── ASSIMILATION_GUIDE.md
├── DECISIONS.md
├── OPERATING_PROTOCOLS.md
├── SECURITY.md
├── CONTRIBUTING.md
├── CHANGELOG.md
├── LICENSE
│
├── program/
│   ├── README.md
│   ├── charter.md
│   ├── portfolio.md
│   ├── roadmap.md
│   ├── governance-model.md
│   ├── operating-model.md
│   ├── knowledge-governance.md
│   ├── risk-register.md
│   ├── decision-log.md
│   ├── architecture-principles.md
│   ├── ai-agent-assimilation.md
│   └── protocols/
│       ├── project-intake.md
│       ├── release-governance.md
│       ├── knowledge-lifecycle.md
│       ├── decision-making.md
│       └── ai-agent-collaboration.md
│
├── projects/
│   ├── avalbot/
│   │   ├── README.md
│   │   ├── PROJECT_CHARTER.md
│   │   ├── GOVERNANCE.md
│   │   ├── ASSIMILATION_GUIDE.md
│   │   ├── DECISIONS.md
│   │   ├── docs/
│   │   ├── src/
│   │   ├── config/
│   │   ├── data/
│   │   ├── tests/
│   │   ├── releases/
│   │   └── operations/
│   │
│   └── dbot/
│       ├── README.md
│       ├── PROJECT_CHARTER.md
│       ├── MIGRATION_NOTES.md
│       ├── src/
│       ├── config/
│       ├── docs/
│       └── tests/
│
├── knowledge/
│   ├── README.md
│   ├── glossary.md
│   ├── concepts/
│   ├── patterns/
│   ├── research-notes/
│   ├── references/
│   └── lessons-learned/
│
├── architecture/
│   ├── README.md
│   ├── principles.md
│   ├── adr/
│   ├── patterns/
│   └── integration-guidelines.md
│
├── governance/
│   ├── README.md
│   ├── roles-and-responsibilities.md
│   ├── decision-rights.md
│   ├── risk-management.md
│   ├── ai-governance.md
│   ├── data-governance.md
│   └── compliance/
│
├── protocols/
│   ├── README.md
│   ├── development-workflow.md
│   ├── documentation-workflow.md
│   ├── release-workflow.md
│   ├── incident-response.md
│   └── agent-workflow.md
│
├── memory/
│   ├── README.md
│   ├── institutional-memory.md
│   ├── chronology.md
│   ├── decisions/
│   ├── retrospectives/
│   └── project-histories/
│
└── templates/
    ├── project-charter-template.md
    ├── adr-template.md
    ├── decision-record-template.md
    ├── release-plan-template.md
    ├── persona-template.md
    ├── protocol-template.md
    └── assimilation-guide-template.md
Justificativa
A estrutura atual mistura três níveis que deveriam ficar explicitamente separados:

Raiz/programa MIT: hoje a raiz apenas identifica o repositório como espaço de trabalhos e insights do curso. 

Projeto AvalBot: já contém visão, arquitetura, backlog, roadmap, governança de autorização e planejamento de release. 

Projeto/protótipo dbot: contém código executável, dependências e instruções operacionais próprias. 

A recomendação principal é transformar o repositório em um monorepo de programa/portfólio, onde:

program/ contém conhecimento e governança do MIT AI Program Office.

projects/ contém iniciativas independentes.

knowledge/ contém conhecimento reutilizável e transversal.

architecture/ contém princípios, padrões e decisões reutilizáveis.

governance/ contém regras institucionais.

protocols/ contém procedimentos operacionais.

memory/ preserva histórico, decisões, retrospectivas e memória institucional.

templates/ padroniza novos artefatos para humanos, Codex e agentes.

Essa separação é coerente com o próprio AvalBot, que já prevê evolução para ecossistemas multiagente, marketplaces de especialistas, múltiplos canais e modelos de governança empresarial. 

2. Estrutura de governança recomendada
Proposta
A governança deveria ter três camadas:

Camada 1 — Program Office
Responsável por visão, princípios, portfólio, governança transversal,
decisões estratégicas, padrões, memória institucional e protocolos.

Camada 2 — Portfólio / Domínios
Responsável por organizar famílias de projetos, capacidades, riscos,
dependências, prioridades e roadmap.

Camada 3 — Projeto
Responsável por execução, arquitetura específica, backlog, releases,
testes, operação e documentação local.
Papéis recomendados
Papel	Escopo	Justificativa
Program Owner	Programa	Necessário para manter direção, priorização e coerência entre múltiplos projetos.
Knowledge Steward	Programa/conhecimento	Necessário porque o repositório pretende suportar governança de conhecimento e memória institucional.
Architecture Steward	Programa/projetos	Necessário porque AvalBot já possui arquitetura explícita e roadmap de evolução. 
Governance Steward	Programa/projetos	Necessário porque o próprio AvalBot já trata identidade, autorização e regras de governança. 
Project Owner	Projeto	Necessário para cada projeto independente.
Persona Responsible	Projeto/AvalBot	Já existe no catálogo de personas: cada persona possui um responsável e accountability por definição, prompt, consistência e manutenção. 
AI Agent Maintainer	Programa/projetos	Necessário para manter instruções de assimilação por Codex e outros agentes.
Fóruns de governança recomendados
Fórum	Frequência sugerida	Decisões típicas
Program Review	Mensal	Prioridades, roadmap, novos projetos, riscos transversais.
Architecture Review	Por mudança relevante	ADRs, padrões, integrações, infraestrutura.
Knowledge Review	Quinzenal/mensal	Promoção de aprendizados de projeto para conhecimento de programa.
Release Review	Por release	Critérios de aceite, baseline versus entregue, evidências.
Persona Governance Review	Por persona/release	Aprovação de novas personas, alteração de prompts, políticas de acesso.
Justificativa
O repositório já demonstra necessidade de governança formal:

AvalBot delega identidade e autorização ao Discord e evita gerenciamento interno de credenciais. 

As regras de negócio incluem provedor único de identidade, ausência de credenciais armazenadas, autorização por Discord Roles e personas externas. 

O plano R2V1 estabelece baseline, rastreabilidade, análise planejado-versus-entregue e retrospectivas futuras. 

O catálogo de personas já possui regras de governança e fonte oficial da verdade. 

Portanto, a governança recomendada deve preservar essa lógica, mas elevá-la para o nível de programa.

3. Artefatos fundamentais que deveriam existir na raiz do repositório
Proposta
Artefato	Finalidade	Justificativa
README.md	Entrada principal do repositório, visão do MIT AI Program Office, mapa de navegação.	Hoje a raiz tem apenas uma descrição curta; precisa orientar humanos e agentes. 
AGENTS.md	Instruções obrigatórias para Codex/agentes: ordem de leitura, limites, padrões, comandos permitidos.	O usuário explicitou assimilação por agentes de IA, Codex e colaboradores humanos.
PROGRAM_CHARTER.md	Mandato, missão, objetivos, escopo e princípios do Program Office.	Necessário para diferenciar programa de projetos.
GOVERNANCE.md	Modelo de governança transversal, papéis, ritos, direitos de decisão.	AvalBot já possui decisões e regras de governança locais; a raiz precisa consolidar governança transversal. 
KNOWLEDGE_MAP.md	Mapa oficial de conhecimento: onde ficam conceitos, decisões, protocolos, projetos e memória.	Necessário para governança de conhecimento e assimilação eficiente.
ASSIMILATION_GUIDE.md	Guia de leitura para agentes e humanos.	O repositório deve ser assimilável; hoje AvalBot já possui uma cadeia de dependências, mas limitada ao projeto. 
DECISIONS.md	Índice de decisões programáticas e arquiteturais.	O plano R2V1 já exige rastreabilidade e preservação histórica. 
OPERATING_PROTOCOLS.md	Índice dos protocolos operacionais do repositório.	Necessário para padronizar execução por humanos e agentes.
SECURITY.md	Política de segurança, segredos, tokens, dados sensíveis.	dbot usa .env, TOKEN e GROQ_API_KEY; esse tema deve ser governado na raiz. 
CONTRIBUTING.md	Regras de contribuição, documentação, branch/PR, qualidade.	Necessário para múltiplos colaboradores e agentes.
LICENSE	Licença do repositório como um todo.	Hoje há uma licença dentro de dbot, mas não há evidência de licença raiz. 
CHANGELOG.md	Histórico de mudanças do repositório/programa.	Ajuda memória institucional e rastreabilidade.
Justificativa geral
A raiz deve responder rapidamente a cinco perguntas:

O que é este repositório?

Como ele é governado?

Onde está cada tipo de conhecimento?

Como agentes e humanos devem assimilá-lo?

Quais decisões, protocolos e projetos estão ativos?

Hoje essas respostas estão parcialmente distribuídas entre a raiz, avalbot e dbot, mas ainda não há uma camada formal de programa. 

4. Artefatos que deveriam existir em nível Programa/Portfólio
Proposta para program/
Artefato	Finalidade	Justificativa
program/README.md	Explica a camada de programa e direciona leitura.	Necessário para separar programa de projetos.
program/charter.md	Mandato do MIT AI Program Office.	O repositório deve evoluir para um Program Office.
program/portfolio.md	Lista projetos, status, owners, dependências e maturidade.	Hoje existem ao menos dois diretórios de projeto/protótipo: avalbot e dbot.
program/roadmap.md	Roadmap transversal do programa.	AvalBot já tem roadmap próprio; o programa precisa de roadmap agregado. 
program/governance-model.md	Papéis, fóruns, decisão, escalonamento e políticas.	AvalBot já contém regras locais; o programa precisa governança superior. 
program/operating-model.md	Como trabalho entra, é priorizado, executado e encerrado.	O plano R2V1 já usa fases e GitHub Project; isso deve virar prática programática. 
program/knowledge-governance.md	Ciclo de vida de conhecimento: captura, validação, promoção, arquivamento.	O usuário explicitou governança de conhecimento e memória institucional.
program/risk-register.md	Registro de riscos transversais.	AvalBot já aborda autorização, credenciais, integração externa e Azure, que são riscos transversais. 
program/decision-log.md	Registro de decisões de programa.	O plano R2V1 valoriza baseline e rastreabilidade. 
program/architecture-principles.md	Princípios arquiteturais comuns.	AvalBot já declara simplicidade, extensibilidade, governança e escalabilidade. 
program/ai-agent-assimilation.md	Guia programático para agentes.	Necessário para Codex/agentes entenderem a hierarquia antes de atuar.
Proposta para program/protocols/
Artefato	Finalidade
project-intake.md	Critérios para aceitar novo projeto.
release-governance.md	Como releases são planejadas, aprovadas e encerradas.
knowledge-lifecycle.md	Como conhecimento nasce em projeto e pode virar conhecimento de programa.
decision-making.md	Como decisões são propostas, aprovadas e registradas.
ai-agent-collaboration.md	Como agentes devem ler, propor, alterar, testar e reportar.
Justificativa
AvalBot já possui elementos que, em um repositório multi-projeto, não deveriam ficar apenas dentro do projeto:

Princípios centrais: simplicidade, extensibilidade, governança e escalabilidade. 

Roadmap com evolução para governança, inteligência comparativa, métricas e marketplace. 

Workflow de projeto: Backlog, Ready, In Progress, Testing, Done. 

Baseline e governança de escopo. 

Esses elementos indicam que a camada Programa deve funcionar como “sistema operacional” do portfólio.

5. Artefatos que deveriam existir em nível Projeto
Proposta geral para cada projeto
projects/<project-id>/
├── README.md
├── PROJECT_CHARTER.md
├── GOVERNANCE.md
├── ASSIMILATION_GUIDE.md
├── DECISIONS.md
├── ROADMAP.md
├── RELEASES.md
├── CHANGELOG.md
├── SECURITY.md
├── docs/
│   ├── architecture.md
│   ├── business-rules.md
│   ├── personas.md              # se aplicável
│   ├── operations.md
│   └── implementation-plans/
├── src/
├── config/
├── data/
├── tests/
├── releases/
└── operations/
Para avalbot
O avalbot já tem base suficiente para virar um projeto formal independente:

Artefato recomendado	Motivo
projects/avalbot/PROJECT_CHARTER.md	Consolidar objetivo, escopo, stakeholders, sucesso e limites. O objetivo R2V1 já existe no README. 
projects/avalbot/docs/architecture.md	Extrair a arquitetura hoje embutida no README. 
projects/avalbot/docs/business-rules.md	Extrair regras de negócio hoje no README. 
projects/avalbot/docs/personas.md	Manter catálogo oficial de personas. Já existe e declara fonte da verdade. 
projects/avalbot/config/personas.json	Configuração externa de personas, planejada pelo projeto. 
projects/avalbot/data/sessions.json	Persistência de sessões; o arquivo já existe como {}.
projects/avalbot/releases/r2v1/	Pacote de release conforme planejamento. 
projects/avalbot/ASSIMILATION_GUIDE.md	Ordem de leitura específica do AvalBot, baseada na cadeia de dependências existente. 
projects/avalbot/DECISIONS.md ou docs/adr/	Registrar decisões sobre Discord, Groq, Azure, personas, sessões e autorização. 
Para dbot
O dbot deveria ser classificado explicitamente como uma das opções abaixo:

Projeto independente legado;

Protótipo predecessor do AvalBot;

Sandbox experimental;

Candidato a arquivamento/migração.

Artefatos recomendados:

Artefato recomendado	Motivo
projects/dbot/PROJECT_CHARTER.md	Esclarecer se dbot é produto, protótipo ou experimento.
projects/dbot/MIGRATION_NOTES.md	Relacionar dbot com avalbot, já que ambos usam Discord/Groq e persona Pirate. 
projects/dbot/SECURITY.md	Governar uso de .env, TOKEN e GROQ_API_KEY. 
projects/dbot/docs/architecture.md	Documentar arquitetura simples atual: Discord client + Groq call. 
projects/dbot/tests/	Criar base mínima de validação antes de promover conhecimento ou código.
Justificativa
O AvalBot já está documentado como plataforma multi-persona com arquitetura, regras, roadmap e baseline de release. 

O dbot, por outro lado, é operacionalmente simples e contém instruções diretas de execução, mas não possui governança, arquitetura formal ou relação explícita com o AvalBot.  Isso recomenda tratá-lo como projeto separado, legado ou sandbox até decisão humana.

6. Regras de separação entre conhecimento de Programa e conhecimento de Projeto
Regra 1 — Programa define princípios; projeto define implementação
Programa deve conter:

princípios arquiteturais;

modelo de governança;

papéis comuns;

padrões de documentação;

protocolos operacionais;

critérios de qualidade;

políticas transversais.

Projeto deve conter:

código;

arquitetura local;

backlog local;

releases locais;

configurações;

testes;

decisões específicas do projeto.

Justificativa: AvalBot já possui princípios gerais que podem ser promovidos a princípios de programa, como simplicidade, extensibilidade, governança e escalabilidade. 

Regra 2 — Conhecimento reutilizável sobe; conhecimento contextual permanece no projeto
Um aprendizado deve ser promovido de projeto para programa quando:

aplicar-se a mais de um projeto;

definir padrão ou protocolo;

afetar governança, segurança, arquitetura ou assimilação;

representar decisão institucional;

evitar retrabalho futuro.

Deve permanecer no projeto quando:

só fizer sentido para uma release específica;

depender da implementação local;

for configuração local;

for backlog local;

for histórico operacional específico.

Justificativa: O plano R2V1 já distingue baseline histórico, mudanças de escopo e rastreabilidade, mostrando que nem todo conhecimento operacional deve alterar a baseline original. 

Regra 3 — Decisões transversais ficam em program/decision-log.md ou architecture/adr/
Exemplos de decisões transversais:

padrão de autenticação/autorização;

padrão de uso de LLMs;

política de gestão de segredos;

estrutura de projetos;

modelo de documentação;

política de memória institucional;

protocolo de agentes.

Justificativa: AvalBot já tomou decisões que podem virar padrões, como delegar identidade ao Discord, usar Discord Roles e não armazenar credenciais de usuário. 

Regra 4 — Decisões locais ficam no projeto
Exemplos:

modelo Groq usado por um bot;

comandos Discord específicos;

formato de sessions.json;

personas de um projeto;

release R2V1 do AvalBot;

implantação de um projeto específico em Azure VM.

Justificativa: AvalBot define comandos, sessões e releases próprios. 

Regra 5 — Personas pertencem ao projeto, mas políticas de persona pertencem ao programa
Projeto:

catálogo de personas;

prompt templates;

status da persona;

responsável;

política de acesso da persona.

Programa:

template de persona;

critérios de aprovação;

ciclo de vida;

avaliação de risco;

padrões de documentação;

regras mínimas de segurança e governança.

Justificativa: O AvalBot já define personas como camada comportamental da plataforma e estabelece que código implementa mecânica enquanto personas definem inteligência, estilo e experiência.  O próprio documento declara que a inteligência reside nas personas e o código implementa comportamento. 

Regra 6 — Memória institucional não deve ser confundida com documentação operacional
Memória institucional:

por que decisões foram tomadas;

contexto histórico;

alternativas rejeitadas;

retrospectivas;

lições aprendidas.

Documentação operacional:

como rodar;

como testar;

como configurar;

como fazer deploy;

como executar protocolo.

Justificativa: O plano R2V1 explicitamente preserva a história de planejamento e impede alteração retroativa da baseline, com objetivos de rastreabilidade e retrospectivas. 

Regra 7 — Configuração e estado não devem ficar misturados com documentação
Recomendação:

config/   → configuração versionada e revisável
data/     → estado local ou persistência controlada
docs/     → documentação humana/agente
src/      → código
Justificativa: O AvalBot hoje prevê personas.json e sessions.json no mesmo nível do README; para evolução, faz sentido separar configuração de estado. 

7. Ordem recomendada de assimilação para agentes
Ordem de assimilação em nível repositório
1. README.md
2. AGENTS.md
3. PROGRAM_CHARTER.md
4. GOVERNANCE.md
5. KNOWLEDGE_MAP.md
6. ASSIMILATION_GUIDE.md
7. OPERATING_PROTOCOLS.md
8. DECISIONS.md
9. program/README.md
10. program/portfolio.md
11. Projeto alvo:
    11.1 README.md
    11.2 PROJECT_CHARTER.md
    11.3 GOVERNANCE.md
    11.4 ASSIMILATION_GUIDE.md
    11.5 DECISIONS.md / ADRs
    11.6 docs/
    11.7 config/
    11.8 src/
    11.9 tests/
    11.10 releases/
Ordem específica sugerida para o AvalBot
1. MIT/README.md
2. program/portfolio.md
3. projects/avalbot/README.md
4. projects/avalbot/docs/r2v1-implementation-plan.md
5. projects/avalbot/docs/personas.md
6. projects/avalbot/docs/architecture.md
7. projects/avalbot/docs/business-rules.md
8. projects/avalbot/config/personas.json
9. projects/avalbot/data/sessions.json
10. projects/avalbot/src/
11. projects/avalbot/tests/
12. projects/avalbot/releases/
Justificativa
O próprio AvalBot já possui uma cadeia de dependência para implementação:

README.md
→ personas.md
→ personas.json
→ Repository Structure
→ Session Service
→ Persona Service
→ Groq Refactoring
→ Discord Commands
→ R2V1 Release
→ Azure Deployment
Essa cadeia aparece explicitamente no README do AvalBot. 

Para agentes, essa cadeia deve ser expandida com uma camada anterior de programa, porque antes de alterar um projeto o agente precisa entender:

o objetivo do repositório;

o modelo de governança;

a separação entre programa e projeto;

as decisões já tomadas;

os protocolos operacionais;

a documentação específica do projeto.

No caso do AvalBot, a leitura de personas.md é especialmente importante porque o documento declara que as personas são fonte oficial da verdade e que personas.json deve ser gerado a partir das definições aprovadas. 

Recomendação estratégica final
Direção recomendada
A evolução mais consistente para este repositório é transformá-lo em um monorepo governado por um MIT AI Program Office, com:

uma camada de programa;

projetos independentes sob projects/;

conhecimento transversal sob knowledge/;

decisões sob architecture/adr/, program/decision-log.md e projects/<id>/DECISIONS.md;

protocolos operacionais explícitos;

memória institucional separada de documentação operacional;

instruções específicas para agentes em AGENTS.md e guias de assimilação.

Por que essa direção é coerente com o conteúdo atual
O conteúdo atual já contém sementes claras dessa evolução:

A raiz define um contexto acadêmico/prático amplo de IA Agêntica e transformação empresarial. 

AvalBot já se apresenta como plataforma multi-persona, com visão, arquitetura, governança, roadmap e releases. 

O plano R2V1 já trata baseline, rastreabilidade, escopo, entregáveis e critérios de sucesso. 

O catálogo de personas já possui regras de governança, responsáveis, políticas de acesso e fonte da verdade. 

O dbot indica a existência de pelo menos mais uma unidade de trabalho ou protótipo, reforçando a necessidade de separar projetos. 

Próximo passo recomendado
Aguardar aprovação humana para uma das opções:

Aprovar a estrutura completa proposta e criar os artefatos base.

Aprovar apenas a reorganização conceitual, sem mover arquivos inicialmente.

Começar por um pacote mínimo, por exemplo:

AGENTS.md

PROGRAM_CHARTER.md

GOVERNANCE.md

KNOWLEDGE_MAP.md

ASSIMILATION_GUIDE.md

program/portfolio.md

Fazer primeiro uma decisão formal registrando se dbot é projeto independente, protótipo legado, sandbox ou candidato à migração para AvalBot.

Verificações realizadas

✅ pwd && rg --files -g 'AGENTS.md' -g '!node_modules' -g '!vendor' && rg --files -g '!node_modules' -g '!vendor' | sed -n '1,200p' — usado para confirmar diretório atual e tentar localizar instruções/arquivos com rg; retornou apenas o caminho porque não havia arquivos encontrados por esse padrão inicial.

✅ find .. -name AGENTS.md -print; printf '\nTop files:\n'; find . -maxdepth 3 -type f | sort | sed -n '1,200p'; printf '\nDirs:\n'; find . -maxdepth 3 -type d | sort | sed -n '1,200p'; git status --short — usado para confirmar ausência de AGENTS.md, mapear arquivos/diretórios principais e verificar estado Git.

✅ for f in README.md avalbot/README.md avalbot/docs/personas.md avalbot/docs/r2v1-implementation-plan.md dbot/README.md dbot/LICENSE dbot/requirements.txt dbot/.gitignore; do echo '---FILE:'$f; nl -ba "$f" | sed -n '1,240p'; done — usado para ler os principais artefatos documentais com numeração de linhas.

✅ for f in dbot/discord_only.py dbot/mybot.py dbot/mybot_v2.py avalbot/sessions.json; do echo '---FILE:'$f; nl -ba "$f" | sed -n '1,260p'; done — usado para inspecionar código e estado/configuração existentes.

✅ nl -ba avalbot/README.md | sed -n '240,520p'; nl -ba avalbot/docs/personas.md | sed -n '237,360p' — usado para ler seções adicionais de estrutura, regras de negócio, personas e governança.

✅ nl -ba avalbot/README.md | sed -n '520,760p'; nl -ba avalbot/docs/personas.md | sed -n '360,460p'; git status --short — usado para ler roadmap/workflow, informações finais de personas e reconfirmar que não houve alterações no repositório.