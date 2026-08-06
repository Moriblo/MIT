````markdown
# AvalBot

> Plataforma Multi-Persona baseada em Discord + Groq desenvolvida no contexto dos estudos e experimentações em Inteligência Artificial, Governança de IA e Sistemas Conversacionais realizados durante o programa MIT.

---

# Visão

O AvalBot é uma plataforma conversacional que permite que um único bot Discord represente múltiplas personas especializadas, cada uma com identidade, conhecimento, estilo de comunicação e propósito próprios.

O objetivo é criar um ambiente flexível onde usuários possam:

- Conversar com especialistas distintos.
- Comparar perspectivas sobre um mesmo tema.
- Explorar diferentes abordagens para resolução de problemas.
- Avaliar aplicações práticas de IA Generativa.
- Experimentar conceitos de Governança de IA.
- Evoluir progressivamente para um marketplace de especialistas digitais.

---

# Objetivos Estratégicos

## Curto Prazo

- Criar um bot multi-persona.
- Utilizar Groq como mecanismo de inferência.
- Operar em um único servidor Discord.
- Operar em um único canal principal.
- Permitir seleção dinâmica de personas.
- Persistir contexto de perfil por usuário.

## Médio Prazo

- Controle de acesso baseado em Roles do Discord.
- Comparação entre múltiplas personas.
- Métricas de uso.
- Observabilidade.

## Longo Prazo

- Marketplace de especialistas.
- Personas plugáveis.
- Governança completa de IA.
- Framework de agentes especializados.

---

# Conceitos Fundamentais

## Persona

Uma persona representa um especialista digital.

Cada persona possui:

- Nome
- Emoji (Moji)
- Descrição
- Prompt
- Estilo de comunicação
- Especialidades
- Configurações do modelo

Exemplo:

```text
🏛️ Governança IA
```

ou

```text
🏴‍☠️ The Mo Pirate
```

---

## Perfil Ativo

Todo usuário possui exatamente um perfil ativo.

O perfil ativo é utilizado quando o usuário envia perguntas sem especificar explicitamente uma persona.

Exemplo:

```text
$perfil governanca
```

Após a seleção:

```text
Como implementar IA responsável?
```

A consulta será executada utilizando o perfil Governança IA.

---

## Consulta Pontual

Permite utilizar uma persona sem alterar o perfil ativo.

Exemplo:

```text
$perfil mopirate Como implementar IA responsável?
```

Neste caso:

- A pergunta utiliza The Mo Pirate.
- O perfil ativo do usuário permanece inalterado.

---

## Consulta Comparativa

Permite comparar respostas de múltiplas personas.

Exemplo:

```text
$compare default,governanca,mopirate Como a IA impactará a sociedade?
```

Retorno esperado:

```text
🧭 Aval
...

🏛️ Governança IA
...

🏴‍☠️ The Mo Pirate
...
```

---

# Personas Iniciais

## 1. Aval (Padrão)

### Emoji

🧭

### Objetivo

Assistente geral do sistema.

### Características

- Equilibrado
- Neutro
- Cordial
- Didático
- Generalista

### Casos de Uso

- Perguntas gerais
- Orientações
- Explicações
- Pesquisa

---

## 2. Governança IA

### Emoji

🏛️

### Objetivo

Especialista em Governança de IA.

### Especialidades

- IA Responsável
- IA Confiável
- Compliance
- LGPD
- ISO 42001
- NIST AI RMF
- Ética
- Regulamentação
- Gestão de Riscos

### Características

- Executivo
- Consultivo
- Estratégico
- Estruturado

---

## 3. The Mo Pirate

### Emoji

🏴‍☠️

### Objetivo

Especialista descontraído e criativo.

### Características

- Inteligente
- Divertido
- Educado
- Criativo
- Leve humor náutico

### Restrições

Não utilizar:

- Roleplay
- Encenações
- Ações entre parênteses

Exemplos proibidos:

```text
(pauses)
(smiles)
(in pirate accent)
```

---

# Arquitetura Conceitual

```text
Discord
    │
    └── Canal #aval
            │
            ├── Usuário A
            ├── Usuário B
            ├── Usuário C
            │
            ▼
        AvalBot
            │
            ▼
     Persona Service
            │
            ▼
      Session Service
            │
            ▼
        Groq API
```

---

# Estrutura Inicial do Repositório

```text
MIT/
│
└── avalbot/
    │
    ├── README.md
    ├── personas.json
    ├── sessions.json
    │
    ├── src/
    │   ├── main.py
    │   ├── commands.py
    │   ├── discord_service.py
    │   ├── groq_service.py
    │   ├── persona_service.py
    │   └── session_service.py
    │
    ├── docs/
    │   ├── architecture.md
    │   ├── roadmap.md
    │   ├── business-rules.md
    │   └── personas.md
    │
    └── releases/
        ├── r2v1/
        ├── r2v2/
        ├── r2v3/
        └── r3v0/
```

---

# Estrutura das Personas

Arquivo:

```text
personas.json
```

Exemplo:

```json
{
  "default": {
    "name": "Aval",
    "emoji": "🧭",
    "description": "Assistente geral.",
    "prompt": "..."
  },

  "governanca": {
    "name": "Governança IA",
    "emoji": "🏛️",
    "description": "Especialista em Governança de IA.",
    "prompt": "..."
  },

  "mopirate": {
    "name": "The Mo Pirate",
    "emoji": "🏴‍☠️",
    "description": "Pirata inteligente e divertido.",
    "prompt": "..."
  }
}
```

---

# Estrutura das Sessões

Arquivo:

```text
sessions.json
```

Exemplo:

```json
{
  "123456789": {
    "active_profile": "governanca"
  },

  "987654321": {
    "active_profile": "mopirate"
  }
}
```

---

# Regras de Negócio

## RB001

Todo usuário possui exatamente um perfil ativo.

---

## RB002

Novos usuários recebem automaticamente o perfil:

```text
Aval
```

---

## RB003

Perguntas sem comando utilizam o perfil ativo.

---

## RB004

O comando:

```text
$perfil <nome>
```

altera o perfil ativo.

---

## RB005

O comando:

```text
$perfil <nome> <pergunta>
```

não altera o perfil ativo.

---

## RB006

O comando:

```text
$compare
```

não altera o perfil ativo.

---

## RB007

Perfis disponíveis são determinados pelos Roles do Discord.

---

## RB008

O sistema não manterá credenciais próprias.

---

## RB009

O Discord é a única fonte de autenticação.

---

## RB010

Não haverá listas de usuários hardcoded.

---

## RB011

Todas as personas serão configuradas externamente.

---

# Comandos

## Listar Perfis

```text
$perfis
```

---

## Ajuda Geral

```text
$ajuda
```

---

## Ajuda da Persona

```text
$ajuda governanca
```

---

## Alterar Perfil Ativo

```text
$perfil governanca
```

---

## Consulta Pontual

```text
$perfil governanca Como implementar IA responsável?
```

---

## Consulta Utilizando Perfil Ativo

```text
Como implementar IA responsável?
```

---

## Consulta Comparativa

```text
$compare default,governanca,mopirate Como a IA impactará a sociedade?
```

---

# Integração Discord

## Canal Principal

```text
#aval
```

---

## Canal de Boas-Vindas

```text
#bem-vindos
```

Conteúdo:

- Apresentação do sistema
- Personas disponíveis
- Exemplos de comandos
- Regras de uso

---

# Roadmap

## Release R2V1

### Objetivo

Fundação Multi-Persona.

### Entregas

- Personas em JSON
- Sessões persistidas
- Perfil ativo
- $perfis
- $perfil
- $ajuda

---

## Release R2V2

### Objetivo

Governança e Segurança.

### Entregas

- Roles Discord
- Controle de acesso
- Logs estruturados
- Auditoria

---

## Release R2V3

### Objetivo

Análise Comparativa.

### Entregas

- $compare
- Múltiplas respostas
- Métricas por persona

---

## Release R2V4

### Objetivo

Observabilidade.

### Entregas

- Estatísticas
- Dashboard
- Consumo Groq
- Telemetria

---

## Release R3V0

### Objetivo

Marketplace de Especialistas.

### Entregas

- Personas plugáveis
- Catálogo de especialistas
- Instalação dinâmica
- Framework de agentes

---

# GitHub Project

Projeto:

```text
avalbot
```

Workflow:

```text
Backlog
Ready
In Progress
Testing
Done
```

---

# Backlog Inicial

## AB-001

Criar personas.json

## AB-002

Criar Session Service

## AB-003

Implementar comando $perfis

## AB-004

Implementar comando $perfil

## AB-005

Implementar comando $ajuda

## AB-006

Persistência de sessões

## AB-007

Refatorar integração Groq

## AB-008

Criar handbook automático

## AB-009

Documentar arquitetura

## AB-010

Publicar Release R2V1

---

# Licença

Em definição.

---

# Autor

Moacyr Ribeiro Blondet

Projeto desenvolvido no contexto dos estudos realizados no MIT sobre Inteligência Artificial, Governança de IA, Sistemas Conversacionais e Agentes Especializados.
````

