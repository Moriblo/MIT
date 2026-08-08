# PHY009_Seq01_ARTIFACT_META_MODEL_rev1.md

# EXECUTION PLAN

| Campo | Valor |
|-------|-------|
| **Fase** | 1 |
| **Seq** | 01 |
| **Contexto** | GOV |
| **Entrega** | ARTIFACT_META_MODEL.md |
| **Revisão** | rev1 |

---

# CONTEXTUALIZAÇÃO

Antes de iniciar esta atividade:

1. Analise o estado atual do repositório MIT.
2. Leia integralmente todos os documentos de governança existentes.
3. Leia integralmente todos os arquivos do diretório `prompt-history/`.
4. Considere esses documentos como a fonte oficial de contexto desta atividade.
5. Preserve todas as decisões arquiteturais já consolidadas.
6. Esta atividade implementa a **Seq. 01** do `EXECUTION_PLAN.md`.
7. Caso exista qualquer divergência entre este prompt, o histórico de prompts e os documentos de governança, interrompa a implementação e apresente uma análise antes de alterar qualquer arquivo.

---

# OBJETIVO

Criar exclusivamente o arquivo `ARTIFACT_META_MODEL.md`.

Este documento constitui o metamodelo oficial da Linguagem Operacional Tipada do MIT AI Program Office e deverá definir apenas o modelo abstrato dos artefatos, nunca instâncias.

---

# ESCOPO

O documento deverá definir formalmente:

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

Não criar implementações, exemplos operacionais ou artefatos reais.

---

# ESTRUTURA ESPERADA

O documento deverá conter obrigatoriamente:

1. Objetivo
2. Escopo
3. Princípios Arquiteturais
4. Modelo Conceitual
5. Entidades
6. Relacionamentos
7. Cardinalidades
8. Regras Estruturais
9. Regras de Baixo Acoplamento
10. Exemplos
11. Evolução do Modelo

## Modelo Conceitual

Apresentar obrigatoriamente um diagrama ASCII representando:

```text
Artifact
├── Strategic Artifact
├── Active Artifact
├── Context Artifact
└── Passive Artifact

Artifact
 ├── has Class
 ├── provides Capability
 ├── requires Capability

Context Artifact
 └── defines institutional domain

Capability
 └── represents functional contract

Class
 └── classifies artifact semantics
```

O diagrama é obrigatório e deverá refletir exclusivamente o metamodelo.

## Entidades

As entidades mínimas são:

- Artifact
- Strategic Artifact
- Active Artifact
- Context Artifact
- Passive Artifact
- Capability
- Class

Para cada entidade utilizar obrigatoriamente:

| Attribute | Type | Required | Allowed Values | Default | Description |

## Relacionamentos

Documentar todos os relacionamentos entre entidades, indicando:

- Origem
- Destino
- Tipo
- Cardinalidade
- Descrição

## Cardinalidades

Documentar todas as cardinalidades utilizadas.

## Regras Estruturais

Definir regras formais garantindo consistência do metamodelo.

Incluir obrigatoriamente regra estabelecendo que:

- Context Artifact representa um domínio institucional reutilizável (ex.: GOV, AVB, OWL), sem instanciar esses contextos.

## Regras de Baixo Acoplamento

Incluir obrigatoriamente:

- nenhum artefato poderá depender estruturalmente de artefato de camada superior;
- compatibilidade entre artefatos deverá ocorrer exclusivamente por Classes e Capabilities;
- identificadores específicos nunca poderão ser utilizados como mecanismo de compatibilidade;
- Capability representa contrato funcional;
- Class representa classificação semântica;
- o metamodelo define tipos, nunca instâncias.

## Exemplos

Somente exemplos abstratos.

É proibido criar:

- MLS-001
- TPL-001
- JOB-001
- GOV.md
- AVB.md
- OWL.md

ou qualquer outro artefato concreto.

## Evolução do Modelo

Descrever regras para evolução preservando compatibilidade retroativa.

---

# REQUISITOS OBRIGATÓRIOS

- Linguagem técnica.
- Especificação formal.
- Estilo Data Dictionary.
- Terminologia consistente.
- Priorizar tabelas, regras e modelos.

---

# RESTRIÇÕES

- Não alterar outros arquivos.
- Não criar novos arquivos além de `ARTIFACT_META_MODEL.md`.
- Não reorganizar diretórios.
- Não realizar commit.
- Não criar Pull Request.

---

# CRITÉRIOS DE ACEITAÇÃO

A entrega será aceita somente se:

- todas as seções estiverem presentes;
- todas as entidades estiverem modeladas;
- todas as entidades utilizarem o formato tabular especificado;
- o diagrama ASCII estiver presente;
- Context Artifact estiver definido como domínio institucional reutilizável;
- Capability estiver definida como contrato funcional;
- Class estiver definida como classificação semântica;
- todas as regras de baixo acoplamento estiverem explicitamente documentadas;
- nenhuma instância concreta existir.

---

# RESULTADO ESPERADO

Apresentar exclusivamente o conteúdo proposto para `ARTIFACT_META_MODEL.md`, pronto para revisão humana, sem executar quaisquer outras alterações no repositório.
