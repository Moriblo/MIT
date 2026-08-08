# PHY009_Seq01_ARTIFACT_META_MODEL.md

Este arquivo contém o prompt completo conforme definido na conversa.

# EXECUTION PLAN

| Campo | Valor |
|-------|-------|
| **Fase** | 1 |
| **Seq** | 01 |
| **Contexto** | GOV |
| **Entrega** | ARTIFACT_META_MODEL.md |

---

# CONTEXTUALIZAÇÃO

Antes de iniciar esta atividade:

1. Analise o estado atual do repositório MIT.
2. Leia integralmente todos os documentos de governança existentes no repositório.
3. Leia integralmente todos os arquivos existentes no diretório `prompt-history/`.
4. Considere os documentos de governança e o histórico de prompts como parte integrante do contexto desta atividade.
5. Preserve todas as decisões arquiteturais já consolidadas.
6. Esta atividade implementa a Seq. 01 do EXECUTION_PLAN.md.
7. Caso identifique inconsistências entre os documentos de governança, os arquivos de `prompt-history/`, o estado atual do repositório e este prompt, interrompa a implementação e apresente uma análise antes de prosseguir.

---

# OBJETIVO

Criar o arquivo `ARTIFACT_META_MODEL.md`.

Este documento constituirá o metamodelo oficial da Linguagem Operacional Tipada adotada pelo MIT AI Program Office.

Seu objetivo é definir formalmente a estrutura dos artefatos institucionais utilizados pelo programa, servindo como referência única para colaboradores humanos e agentes de IA.

---

# ESCOPO

Criar exclusivamente o arquivo `ARTIFACT_META_MODEL.md`.

O documento deverá definir:

- modelo conceitual;
- entidades;
- atributos;
- tipos;
- obrigatoriedade;
- valores permitidos;
- valores default;
- relacionamentos;
- cardinalidades;
- regras estruturais;
- regras de baixo acoplamento.

Definir apenas tipos, nunca instâncias.

---

# ESTRUTURA ESPERADA

Objetivo
Escopo
Princípios Arquiteturais
Modelo Conceitual
Entidades
Relacionamentos
Cardinalidades
Regras Estruturais
Regras de Baixo Acoplamento
Exemplos
Evolução do Modelo

Incluir um diagrama ASCII semelhante ao discutido na conversa.

Para cada entidade utilizar a tabela:

| Attribute | Type | Required | Allowed Values | Default | Description |

Entidades mínimas:
- Artifact
- Strategic Artifact
- Active Artifact
- Context Artifact
- Passive Artifact
- Capability
- Class

---

# REQUISITOS OBRIGATÓRIOS

- Linguagem técnica.
- Especificação técnica.
- Priorizar tabelas e regras formais.
- Abordagem de Data Dictionary.
- Consistência terminológica.

---

# RESTRIÇÕES

- Não alterar outros arquivos.
- Não reorganizar diretórios.
- Não criar novos arquivos além de `ARTIFACT_META_MODEL.md`.
- Não realizar commit.
- Não criar Pull Request.

---

# CRITÉRIOS DE ACEITAÇÃO

- Estrutura completa.
- Entidades definidas.
- Relacionamentos documentados.
- Cardinalidades definidas.
- Regras estruturais e de baixo acoplamento completas.
- Nenhuma instância concreta.
- Documento apto a servir de referência oficial.

---

# RESULTADO ESPERADO

Apresentar exclusivamente o conteúdo proposto para `ARTIFACT_META_MODEL.md`, pronto para revisão humana.
