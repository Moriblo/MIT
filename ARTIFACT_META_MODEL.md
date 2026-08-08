# ARTIFACT_META_MODEL.md

## 1. Objetivo

Definir o metamodelo oficial da Linguagem Operacional Tipada do MIT AI Program Office.

Este documento especifica, em nível abstrato, a estrutura formal dos artefatos institucionais utilizados para governança, contexto, execução, documentação e evolução do Programa. O metamodelo serve como referência única para colaboradores humanos e agentes de IA ao interpretar, criar, revisar ou validar artefatos.

O metamodelo define tipos, atributos, relacionamentos, cardinalidades e regras. Ele não define instâncias concretas.

---

## 2. Escopo

| Item | Incluído | Descrição |
|---|---:|---|
| Modelo conceitual | Yes | Representação abstrata das entidades centrais e suas relações. |
| Entidades | Yes | Tipos formais que compõem o metamodelo. |
| Atributos | Yes | Campos estruturais esperados em cada entidade. |
| Tipos | Yes | Domínios de dados permitidos para atributos. |
| Obrigatoriedade | Yes | Regras de presença obrigatória ou opcional. |
| Valores permitidos | Yes | Domínios controlados e enumerações. |
| Valores default | Yes | Valores assumidos quando aplicável. |
| Relacionamentos | Yes | Associações formais entre entidades. |
| Cardinalidades | Yes | Restrições quantitativas de relacionamento. |
| Regras estruturais | Yes | Condições formais de consistência do metamodelo. |
| Regras de baixo acoplamento | Yes | Restrições para compatibilidade por tipos, classes e capabilities. |
| Instâncias concretas | No | Artefatos reais, códigos de contexto, jobs, templates ou marcos não são definidos neste documento. |
| Implementações | No | Código, automações, parsers e workflows executáveis estão fora do escopo. |
| Artefatos operacionais reais | No | O documento não cria milestones, templates, jobs ou context artifacts concretos. |

---

## 3. Princípios Arquiteturais

| ID | Princípio | Definição Formal |
|---|---|---|
| PA-001 | Abstração | O metamodelo descreve somente tipos e relações abstratas. |
| PA-002 | Tipagem explícita | Todo Artifact deve possuir uma Class e declarar ou requerer Capabilities. |
| PA-003 | Separação entre semântica e função | Class representa classificação semântica; Capability representa contrato funcional. |
| PA-004 | Baixo acoplamento | Compatibilidade entre artefatos deve ocorrer por Class e Capability, não por identificadores específicos. |
| PA-005 | Reutilização institucional | Context Artifact representa domínio institucional reutilizável, não arquivo ou instância concreta. |
| PA-006 | Especialização controlada | Strategic, Active, Context e Passive Artifact especializam Artifact sem romper o contrato base. |
| PA-007 | Validação formal | Regras estruturais devem permitir validação objetiva de conformidade. |
| PA-008 | Compatibilidade retroativa | Evoluções do metamodelo devem preservar artefatos existentes sempre que possível. |
| PA-009 | Consistência terminológica | Os termos Artifact, Class, Capability e Context Artifact mantêm significado único no Programa. |
| PA-010 | Independência de camada superior | Nenhum artefato deve depender estruturalmente de artefato de camada superior. |

---

## 4. Modelo Conceitual

O metamodelo é composto por três conceitos centrais:

| Conceito | Papel no Metamodelo |
|---|---|
| Artifact | Unidade abstrata de conhecimento, governança, contexto, execução ou referência. |
| Class | Classificação semântica atribuída a um Artifact. |
| Capability | Contrato funcional provido ou requerido por um Artifact. |

`Artifact` é a entidade raiz. Suas especializações representam categorias arquiteturais, não instâncias. `Class` define a semântica do artefato. `Capability` define o contrato funcional utilizado para compatibilidade, validação e composição de baixo acoplamento.

### Diagrama ASCII

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

---

## 5. Entidades

### 5.1 Artifact

Entidade abstrata raiz para artefatos institucionais. Define o contrato mínimo comum herdado por todas as especializações.

| Attribute | Type | Required | Allowed Values | Default | Description |
|---|---|---:|---|---|---|
| artifact_id | Identifier | Yes | Unique identifier within artifact namespace | None | Identificador estável do artefato abstrato ou concreto. Não deve ser usado como mecanismo de compatibilidade. |
| name | String | Yes | Non-empty string | None | Nome legível do artefato. |
| artifact_category | Enum | Yes | Strategic Artifact; Active Artifact; Context Artifact; Passive Artifact | None | Categoria arquitetural do artefato. |
| class_id | Identifier | Yes | Existing Class identifier | None | Referência à Class que classifica a semântica do artefato. |
| provided_capability_ids | Identifier List | No | Existing Capability identifiers | Empty list | Capabilities providas pelo artefato como contratos funcionais. |
| required_capability_ids | Identifier List | No | Existing Capability identifiers | Empty list | Capabilities requeridas para uso, composição ou validação. |
| lifecycle_status | Enum | Yes | Draft; Proposed; Active; Deprecated; Retired | Draft | Estado de ciclo de vida do artefato. |
| abstraction_level | Enum | Yes | Meta Model; Type; Template; Instance | Type | Nível de abstração representado pelo artefato. |
| scope_level | Enum | Yes | Institutional; Portfolio; Project; Local | Institutional | Escopo de aplicabilidade do artefato. |
| description | Text | Yes | Non-empty text | None | Definição objetiva do propósito do artefato. |
| version | Semantic Version | No | MAJOR.MINOR.PATCH | 0.1.0 | Versão lógica do artefato. |
| owner_role | String | No | Non-empty string | Undefined | Papel responsável pela governança do artefato. |

### 5.2 Strategic Artifact

Especialização de Artifact que representa direção, intenção, decisão, marco, prioridade ou alinhamento estratégico.

| Attribute | Type | Required | Allowed Values | Default | Description |
|---|---|---:|---|---|---|
| artifact_id | Identifier | Yes | Unique identifier within artifact namespace | None | Identificador herdado de Artifact. |
| artifact_category | Enum | Yes | Strategic Artifact | Strategic Artifact | Categoria fixa desta especialização. |
| class_id | Identifier | Yes | Existing Class identifier compatible with Strategic Artifact | None | Class que define a semântica estratégica. |
| provided_capability_ids | Identifier List | No | Existing Capability identifiers | Empty list | Contratos funcionais providos pelo artefato estratégico. |
| required_capability_ids | Identifier List | No | Existing Capability identifiers | Empty list | Contratos funcionais requeridos para sua interpretação ou uso. |
| strategic_scope | Enum | Yes | Institutional; Portfolio; Project | Institutional | Escopo decisório da intenção estratégica. |
| strategic_function | Enum | Yes | Direction; Decision; Milestone; Principle; Objective; Constraint | Direction | Função estratégica abstrata exercida pelo artefato. |
| time_horizon | Enum | No | Short Term; Medium Term; Long Term; Continuous; Undefined | Undefined | Horizonte temporal de validade estratégica. |
| success_condition_type | Enum | No | Qualitative; Quantitative; Mixed; Not Applicable | Not Applicable | Tipo abstrato de condição de sucesso. |
| description | Text | Yes | Non-empty text | None | Definição da função estratégica sem instanciar conteúdo concreto. |

### 5.3 Active Artifact

Especialização de Artifact que representa estrutura acionável, reutilizável ou executável em nível operacional, sem definir uma execução concreta.

| Attribute | Type | Required | Allowed Values | Default | Description |
|---|---|---:|---|---|---|
| artifact_id | Identifier | Yes | Unique identifier within artifact namespace | None | Identificador herdado de Artifact. |
| artifact_category | Enum | Yes | Active Artifact | Active Artifact | Categoria fixa desta especialização. |
| class_id | Identifier | Yes | Existing Class identifier compatible with Active Artifact | None | Class que define a semântica operacional. |
| provided_capability_ids | Identifier List | No | Existing Capability identifiers | Empty list | Contratos funcionais providos pelo artefato ativo. |
| required_capability_ids | Identifier List | No | Existing Capability identifiers | Empty list | Contratos funcionais requeridos para execução ou composição. |
| action_type | Enum | Yes | Template; Job; Protocol; Command; Workflow; Checklist; Procedure | Template | Tipo abstrato de ação representada. |
| input_contract_type | Enum | No | None; Structured; Free Text; Artifact Reference; Mixed | None | Tipo de contrato abstrato de entrada. |
| output_contract_type | Enum | No | None; Structured; Free Text; Artifact Reference; Mixed | None | Tipo de contrato abstrato de saída. |
| execution_binding | Enum | Yes | Manual; Agent Assisted; Automated; Undefined | Undefined | Forma abstrata de vinculação à execução. |
| idempotency_requirement | Enum | No | Required; Recommended; Not Required; Not Applicable | Recommended | Requisito abstrato de repetibilidade segura. |
| description | Text | Yes | Non-empty text | None | Definição operacional abstrata, sem criar artefato executável real. |

### 5.4 Context Artifact

Especialização de Artifact que representa um domínio institucional reutilizável. Um Context Artifact delimita fronteiras semânticas, vocabulário e escopo interpretativo de um domínio. Códigos ou nomes de domínio podem existir em catálogos ou artefatos próprios, mas este metamodelo não instancia esses contextos.

| Attribute | Type | Required | Allowed Values | Default | Description |
|---|---|---:|---|---|---|
| artifact_id | Identifier | Yes | Unique identifier within artifact namespace | None | Identificador herdado de Artifact. |
| artifact_category | Enum | Yes | Context Artifact | Context Artifact | Categoria fixa desta especialização. |
| class_id | Identifier | Yes | Existing Class identifier compatible with Context Artifact | None | Class que define a semântica contextual. |
| provided_capability_ids | Identifier List | No | Existing Capability identifiers | Empty list | Contratos funcionais providos pelo contexto. |
| required_capability_ids | Identifier List | No | Existing Capability identifiers | Empty list | Contratos funcionais requeridos para interpretar o contexto. |
| domain_type | Enum | Yes | Institutional Domain; Portfolio Domain; Project Domain; Execution Domain; Knowledge Domain | Institutional Domain | Tipo abstrato de domínio representado. |
| boundary_definition | Text | Yes | Non-empty text | None | Definição abstrata das fronteiras semânticas do domínio. |
| vocabulary_policy | Enum | No | Controlled; Extensible; External; Undefined | Controlled | Política abstrata para vocabulário do domínio. |
| reuse_policy | Enum | Yes | Reusable; Restricted; Deprecated | Reusable | Política de reutilização institucional do contexto. |
| coupling_policy | Enum | Yes | Class and Capability Only; Explicit Reference Allowed; Undefined | Class and Capability Only | Política de compatibilidade do contexto com outros artefatos. |
| description | Text | Yes | Non-empty text | None | Definição do domínio institucional reutilizável, sem instanciar domínio concreto. |

### 5.5 Passive Artifact

Especialização de Artifact que representa conhecimento estável, documentação normativa, catálogo, especificação, registro ou referência.

| Attribute | Type | Required | Allowed Values | Default | Description |
|---|---|---:|---|---|---|
| artifact_id | Identifier | Yes | Unique identifier within artifact namespace | None | Identificador herdado de Artifact. |
| artifact_category | Enum | Yes | Passive Artifact | Passive Artifact | Categoria fixa desta especialização. |
| class_id | Identifier | Yes | Existing Class identifier compatible with Passive Artifact | None | Class que define a semântica documental ou referencial. |
| provided_capability_ids | Identifier List | No | Existing Capability identifiers | Empty list | Contratos funcionais providos pelo artefato passivo. |
| required_capability_ids | Identifier List | No | Existing Capability identifiers | Empty list | Contratos funcionais requeridos para validação ou interpretação. |
| knowledge_type | Enum | Yes | Meta Model; Catalog; Specification; Reference; Registry; Decision Record; Guide | Reference | Tipo abstrato de conhecimento representado. |
| normative_level | Enum | Yes | Informative; Normative; Authoritative | Normative | Grau de força normativa do artefato. |
| update_policy | Enum | No | Manual; Governed; Generated; Append Only | Governed | Política abstrata de atualização. |
| source_of_truth_policy | Enum | No | Source of Truth; Supporting Reference; Derived Reference; Undefined | Undefined | Papel do artefato como fonte de referência. |
| description | Text | Yes | Non-empty text | None | Definição documental abstrata, sem instanciar conteúdo concreto. |

### 5.6 Capability

Entidade que representa contrato funcional. Uma Capability define uma aptidão provida ou requerida por artefatos para fins de compatibilidade, validação e composição. Capabilities não representam instâncias, identificadores específicos ou nomes de arquivos.

| Attribute | Type | Required | Allowed Values | Default | Description |
|---|---|---:|---|---|---|
| capability_id | Identifier | Yes | Unique identifier within capability namespace | None | Identificador estável da Capability. Não deve ser usado isoladamente como compatibilidade sem o contrato associado. |
| name | String | Yes | Non-empty string | None | Nome legível do contrato funcional. |
| capability_kind | Enum | Yes | Functional Contract; Validation Contract; Governance Contract; Execution Contract; Documentation Contract | Functional Contract | Natureza abstrata do contrato. |
| contract_description | Text | Yes | Non-empty text | None | Definição formal da aptidão ou obrigação funcional. |
| input_expectation | Text | No | Abstract input expectation | None | Expectativa abstrata de entrada, quando aplicável. |
| output_expectation | Text | No | Abstract output expectation | None | Expectativa abstrata de saída, quando aplicável. |
| validation_criteria | Text List | No | Formal criteria statements | Empty list | Critérios abstratos para validar o contrato funcional. |
| compatible_class_ids | Identifier List | No | Existing Class identifiers | Empty list | Classes semanticamente compatíveis com a Capability. |
| incompatible_capability_ids | Identifier List | No | Existing Capability identifiers | Empty list | Capabilities incompatíveis com este contrato. |
| lifecycle_status | Enum | Yes | Draft; Proposed; Active; Deprecated; Retired | Draft | Estado de ciclo de vida da Capability. |

### 5.7 Class

Entidade que representa classificação semântica. Uma Class define a categoria semântica de um Artifact, suas compatibilidades, restrições e capabilities esperadas. Classes não representam execução, arquivo, instância ou identificador concreto de compatibilidade.

| Attribute | Type | Required | Allowed Values | Default | Description |
|---|---|---:|---|---|---|
| class_id | Identifier | Yes | Unique identifier within class namespace | None | Identificador estável da Class. Não substitui validação semântica. |
| name | String | Yes | Non-empty string | None | Nome legível da classificação semântica. |
| semantic_description | Text | Yes | Non-empty text | None | Definição formal da semântica classificada. |
| parent_class_id | Identifier | No | Existing Class identifier | None | Classe pai para especialização semântica controlada. |
| allowed_artifact_categories | Enum List | Yes | Strategic Artifact; Active Artifact; Context Artifact; Passive Artifact | Empty list | Categorias de Artifact compatíveis com a Class. |
| required_capability_ids | Identifier List | No | Existing Capability identifiers | Empty list | Capabilities obrigatórias para artefatos classificados nesta Class. |
| optional_capability_ids | Identifier List | No | Existing Capability identifiers | Empty list | Capabilities opcionais compatíveis. |
| semantic_constraints | Text List | No | Formal constraint statements | Empty list | Restrições semânticas aplicáveis. |
| compatibility_policy | Enum | Yes | Class Only; Class and Capability; Capability Required | Class and Capability | Política abstrata de compatibilidade semântica. |
| lifecycle_status | Enum | Yes | Draft; Proposed; Active; Deprecated; Retired | Draft | Estado de ciclo de vida da Class. |

---

## 6. Relacionamentos

| Origem | Destino | Tipo | Cardinalidade | Descrição |
|---|---|---|---|---|
| Artifact | Strategic Artifact | Specialization | 0..1 | Um Artifact pode ser especializado como Strategic Artifact. |
| Artifact | Active Artifact | Specialization | 0..1 | Um Artifact pode ser especializado como Active Artifact. |
| Artifact | Context Artifact | Specialization | 0..1 | Um Artifact pode ser especializado como Context Artifact. |
| Artifact | Passive Artifact | Specialization | 0..1 | Um Artifact pode ser especializado como Passive Artifact. |
| Artifact | Class | Classification | 1..1 | Todo Artifact possui exatamente uma Class primária. |
| Class | Artifact | Classification Target | 0..* | Uma Class pode classificar zero ou muitos Artifacts. |
| Artifact | Capability | Provides | 0..* | Um Artifact pode prover zero ou muitas Capabilities como contratos funcionais. |
| Artifact | Capability | Requires | 0..* | Um Artifact pode requerer zero ou muitas Capabilities para compatibilidade. |
| Capability | Artifact | Provided By | 0..* | Uma Capability pode ser provida por zero ou muitos Artifacts. |
| Capability | Artifact | Required By | 0..* | Uma Capability pode ser requerida por zero ou muitos Artifacts. |
| Class | Capability | Requires | 0..* | Uma Class pode exigir Capabilities obrigatórias. |
| Class | Capability | Allows | 0..* | Uma Class pode permitir Capabilities opcionais. |
| Capability | Class | Compatible With | 0..* | Uma Capability pode declarar compatibilidade com Classes. |
| Class | Class | Specializes | 0..1 parent; 0..* children | Uma Class pode especializar uma Class pai e possuir subclasses. |
| Context Artifact | Artifact | Contextualizes | 0..* | Um Context Artifact pode contextualizar artefatos por domínio institucional reutilizável. |
| Strategic Artifact | Artifact | Governs | 0..* | Um Strategic Artifact pode governar artefatos sem criar dependência estrutural inversa. |
| Active Artifact | Artifact | Consumes | 0..* | Um Active Artifact pode consumir artefatos por contrato funcional. |
| Active Artifact | Artifact | Produces | 0..* | Um Active Artifact pode produzir artefatos por contrato funcional. |
| Passive Artifact | Artifact | References | 0..* | Um Passive Artifact pode referenciar artefatos sem dependência operacional. |

---

## 7. Cardinalidades

| Cardinalidade | Nome | Significado |
|---|---|---|
| 0..1 | Optional Single | O relacionamento pode estar ausente ou ocorrer uma vez. |
| 1..1 | Required Single | O relacionamento deve ocorrer exatamente uma vez. |
| 0..* | Optional Many | O relacionamento pode estar ausente ou ocorrer múltiplas vezes. |
| 1..* | Required Many | O relacionamento deve ocorrer uma ou mais vezes. |
| 0..1 parent; 0..* children | Hierarchical Optional Parent | Uma entidade pode ter no máximo um pai direto e múltiplos filhos. |

| Entidade / Relação | Cardinalidade Aplicável | Regra |
|---|---|---|
| Artifact -> Class | 1..1 | Todo Artifact deve possuir exatamente uma Class primária. |
| Artifact -> provided Capability | 0..* | Um Artifact pode prover múltiplos contratos funcionais. |
| Artifact -> required Capability | 0..* | Um Artifact pode requerer múltiplos contratos funcionais. |
| Class -> required Capability | 0..* | Uma Class pode exigir contratos funcionais obrigatórios. |
| Class -> optional Capability | 0..* | Uma Class pode permitir contratos funcionais opcionais. |
| Capability -> compatible Class | 0..* | Uma Capability pode declarar Classes compatíveis. |
| Class -> parent Class | 0..1 | Uma Class pode possuir no máximo uma Class pai direta. |
| Class -> child Class | 0..* | Uma Class pode possuir múltiplas subclasses. |
| Artifact -> Artifact specialization | 1..1 category | Cada Artifact concreto deve pertencer a exatamente uma categoria arquitetural. |
| Context Artifact -> contextualized Artifact | 0..* | Um domínio institucional pode contextualizar múltiplos artefatos. |
| Strategic Artifact -> governed Artifact | 0..* | Um artefato estratégico pode governar múltiplos artefatos. |
| Active Artifact -> consumed Artifact | 0..* | Um artefato ativo pode consumir múltiplos artefatos por contrato. |
| Active Artifact -> produced Artifact | 0..* | Um artefato ativo pode produzir múltiplos artefatos por contrato. |
| Passive Artifact -> referenced Artifact | 0..* | Um artefato passivo pode referenciar múltiplos artefatos. |

---

## 8. Regras Estruturais

| ID | Regra Formal |
|---|---|
| RS-001 | O metamodelo define tipos, nunca instâncias concretas. |
| RS-002 | Toda entidade Artifact deve possuir exatamente uma categoria arquitetural: Strategic Artifact, Active Artifact, Context Artifact ou Passive Artifact. |
| RS-003 | Toda especialização de Artifact deve preservar os atributos obrigatórios definidos em Artifact. |
| RS-004 | Todo Artifact deve possuir exatamente uma Class primária. |
| RS-005 | Class representa classificação semântica do Artifact. |
| RS-006 | Capability representa contrato funcional provido ou requerido por Artifact ou Class. |
| RS-007 | Compatibilidade estrutural entre artefatos deve ser determinada por Class e Capability. |
| RS-008 | Identificadores específicos não podem substituir validação por Class e Capability. |
| RS-009 | Context Artifact representa um domínio institucional reutilizável, como uma família abstrata de contextos governados; este metamodelo não instancia códigos concretos de domínio, incluindo exemplos como GOV, AVB ou OWL. |
| RS-010 | Um Context Artifact deve declarar fronteiras semânticas por meio de `boundary_definition`. |
| RS-011 | Um Active Artifact deve declarar tipo abstrato de ação por meio de `action_type`. |
| RS-012 | Um Strategic Artifact deve declarar escopo e função estratégica. |
| RS-013 | Um Passive Artifact deve declarar tipo de conhecimento e nível normativo. |
| RS-014 | Uma Class não pode exigir Capability incompatível com outra Capability obrigatória da mesma Class. |
| RS-015 | Uma Capability incompatível não pode ser simultaneamente provida e requerida pelo mesmo Artifact sem regra explícita de reconciliação. |
| RS-016 | Relacionamentos circulares estruturais obrigatórios entre artefatos são proibidos. |
| RS-017 | Relacionamentos de referência não implicam dependência operacional. |
| RS-018 | Alterações em Class ou Capability que modifiquem compatibilidade devem ser tratadas como evolução governada do metamodelo. |
| RS-019 | Defaults não eliminam a obrigatoriedade de atributos requeridos. |
| RS-020 | Nenhuma regra do metamodelo pode depender de nome de arquivo, identificador concreto ou instância específica. |

---

## 9. Regras de Baixo Acoplamento

| ID | Regra Formal |
|---|---|
| RBA-001 | Nenhum artefato poderá depender estruturalmente de artefato de camada superior. |
| RBA-002 | Compatibilidade entre artefatos deverá ocorrer exclusivamente por Classes e Capabilities. |
| RBA-003 | Identificadores específicos nunca poderão ser utilizados como mecanismo de compatibilidade. |
| RBA-004 | Capability representa contrato funcional, não instância, arquivo, comando específico ou nome operacional concreto. |
| RBA-005 | Class representa classificação semântica, não implementação, execução ou identificador concreto. |
| RBA-006 | O metamodelo define tipos, nunca instâncias. |
| RBA-007 | Um Artifact deve consumir ou produzir outros artefatos por contrato funcional sempre que a relação envolver execução. |
| RBA-008 | Um Passive Artifact pode referenciar outro Artifact sem criar dependência operacional. |
| RBA-009 | Um Context Artifact deve contextualizar por domínio institucional reutilizável, não por acoplamento a artefatos concretos. |
| RBA-010 | Um Strategic Artifact deve governar por intenção, princípio, restrição ou critério, sem acoplamento estrutural a artefatos de camada inferior. |
| RBA-011 | Um Active Artifact deve declarar contratos de entrada e saída em nível abstrato quando interagir com outros artefatos. |
| RBA-012 | Classes e Capabilities devem ser reutilizáveis por múltiplos artefatos e não especializadas para uma única instância concreta. |
| RBA-013 | Relações bidirecionais devem ser evitadas; quando necessárias, devem ser semânticas e explicitamente documentadas. |
| RBA-014 | Mudanças em identificadores não devem alterar compatibilidade se Class e Capability permanecerem equivalentes. |
| RBA-015 | Artefatos de escopo local ou projetual não podem redefinir semântica institucional de Class ou Capability. |

---

## 10. Exemplos

Esta seção contém somente exemplos abstratos de forma, sem criação de artefatos concretos.

### 10.1 Forma abstrata de Artifact

| Campo Abstrato | Valor Abstrato Permitido |
|---|---|
| artifact_category | Uma categoria definida pelo metamodelo. |
| class_id | Uma Class existente no namespace de classes. |
| provided_capability_ids | Zero ou mais Capabilities existentes. |
| required_capability_ids | Zero ou mais Capabilities existentes. |
| lifecycle_status | Um estado de ciclo de vida permitido. |
| abstraction_level | Um nível de abstração permitido. |

### 10.2 Validação abstrata por Class

| Etapa | Critério Formal |
|---|---|
| Existência | A Class referenciada deve existir no namespace de classes. |
| Compatibilidade de categoria | A categoria do Artifact deve estar em `allowed_artifact_categories`. |
| Capabilities obrigatórias | O Artifact deve satisfazer as `required_capability_ids` da Class. |
| Restrições semânticas | O Artifact deve cumprir `semantic_constraints` aplicáveis. |

### 10.3 Validação abstrata por Capability

| Etapa | Critério Formal |
|---|---|
| Existência | A Capability referenciada deve existir no namespace de capabilities. |
| Contrato | O uso da Capability deve respeitar `contract_description`. |
| Compatibilidade | A Class do Artifact deve ser compatível com a Capability quando houver restrição declarada. |
| Incompatibilidade | Capabilities listadas como incompatíveis não devem coexistir sem reconciliação formal. |

---

## 11. Evolução do Modelo

| ID | Regra de Evolução |
|---|---|
| EV-001 | A evolução do metamodelo deve preservar compatibilidade retroativa sempre que possível. |
| EV-002 | Novos atributos obrigatórios devem incluir regra de migração para artefatos existentes. |
| EV-003 | Novas categorias de Artifact devem especializar Artifact sem alterar o contrato base. |
| EV-004 | Novas Classes devem preservar a distinção entre classificação semântica e contrato funcional. |
| EV-005 | Novas Capabilities devem preservar a definição de contrato funcional reutilizável. |
| EV-006 | Alterações em cardinalidades devem ser consideradas mudanças estruturais maiores. |
| EV-007 | Valores enumerados podem ser adicionados quando não invalidarem valores existentes. |
| EV-008 | Valores enumerados não devem ser removidos sem ciclo prévio de depreciação. |
| EV-009 | Identificadores devem permanecer estáveis ao longo da evolução do modelo. |
| EV-010 | Compatibilidade entre versões deve ser avaliada por Class, Capability e regras estruturais. |
| EV-011 | Instâncias concretas devem permanecer fora do metamodelo e ser definidas apenas em artefatos próprios. |
| EV-012 | Mudanças editoriais sem impacto em tipos, cardinalidades ou regras podem ser tratadas como revisão menor. |
| EV-013 | Mudanças que alterem o significado de Artifact, Class, Capability ou Context Artifact exigem revisão governada. |
