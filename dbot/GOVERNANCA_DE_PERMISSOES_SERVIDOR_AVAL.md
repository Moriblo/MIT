# GOVERNANÇA DE PERMISSÕES — SERVIDOR AVAL

> Documento consolidado das definições acordadas para a governança, documentação, baseline, histórico, inventário e análise de consistência das permissões do servidor **Aval** no Discord.

---

## 1. Objetivo da governança

Esta estrutura tem como objetivo criar uma base documental e operacional para responder, de forma rastreável, às seguintes perguntas:

- como uma permissão estava considerada no início da governança;
- por que aquela configuração inicial foi adotada;
- qual é o status atual da permissão;
- quando ocorreu a última mudança;
- quando o parâmetro foi inventariado pela última vez;
- qual membro e qual cargo estão envolvidos;
- em qual recurso a permissão está sendo analisada;
- como a herança pode influenciar a permissão efetiva;
- quais alterações ocorreram ao longo do tempo;
- se existem inconsistências entre status, datas e inventários.

A governança não pretende reconstruir artificialmente todo o histórico anterior. O objetivo é estabelecer uma **baseline confiável** e criar **rastreabilidade real a partir dela**.

---

# 2. Princípios fundamentais

## 2.1 Baseline não significa “estado atual”

A **Baseline** representa:

> **como o parâmetro estava considerado no início da governança e por que aquela condição foi adotada.**

Portanto, a baseline é uma referência inicial controlada.

Ela não deve ser confundida com o status atual.

---

## 2.2 Status Atual representa a situação efetiva conhecida

O **Status Atual** representa a situação mais recentemente registrada para determinado parâmetro.

Ele deve ser analisado juntamente com:

- Data/Hora da Mudança;
- Data do Inventário;
- Razão da Última Atualização;
- Permissão Efetiva, quando aplicável.

---

## 2.3 Inventário e atualização são conceitos diferentes

Uma mudança pode ocorrer sem inventário posterior.

Um inventário pode ocorrer sem qualquer mudança.

Por isso, devem existir informações distintas para:

- **Data/Hora da Mudança** — quando ocorreu a última alteração conhecida;
- **Data do Inventário** — quando aquele parâmetro foi verificado pela última vez.

---

## 2.4 A permissão efetiva pode resultar de múltiplos níveis

A configuração observada em um único ponto não representa necessariamente a permissão efetiva de um membro.

A análise deve considerar, conforme aplicável:

```text
Membro
   │
   ├── Cargos
   │
   ├── Categoria
   │       └── Canal
   │
   └── Permissão efetiva resultante
```

Assim, duas linhas com o mesmo parâmetro podem apresentar status diferentes sem que isso seja necessariamente uma inconsistência.

Exemplo:

| Elemento | Parâmetro | Status |
|---|---|---|
| Cargo Aval-Gestão | Gerenciar canais | ✓ |
| Categoria APLICAÇÕES | Gerenciar canais | / |
| Canal aval-corp | Gerenciar canais | ✓ ou / |
| Membro específico | Permissão efetiva | ✓ |

A interpretação depende da combinação e da herança entre os níveis.

Para esclarecimentos adicionais sobre o funcionamento e a interpretação da herança, deve-se consultar o **Glossário**, especialmente os registros relacionados à **Permissão Efetiva**, herança e precedência.

---

# 3. Estrutura consolidada das tabelas

A estrutura principal é composta por tabelas funcionais e tabelas de metadados.

## 3.1 Tabela 1 — Baseline

### Finalidade

Registrar a condição considerada no início da governança e a justificativa daquela configuração.

### Pergunta que responde

> **Como este parâmetro estava considerado no início da governança e por quê?**

### Campos principais

| Campo | Finalidade |
|---|---|
| Membro | Identifica o membro ao qual a análise se aplica, quando aplicável |
| Cargo | Identifica o cargo relacionado |
| Tipo de Recurso | Identifica se o recurso é Cargo, Categoria, Canal ou outro tipo definido |
| Nome do Recurso | Nome utilizado no servidor para identificar o recurso |
| Categoria | Contextualiza a categoria à qual o recurso pertence, quando aplicável |
| Parâmetro | Permissão ou configuração específica analisada |
| Status Baseline | Condição considerada na baseline |
| Permissão Efetiva | Resultado efetivo esperado ou observado para o membro, quando aplicável |
| Razão da Configuração Inicial | Justificativa conhecida para a condição inicial |
| Data/Hora da Baseline | Momento de formalização da baseline |
| Responsável | Cargo responsável pela manutenção do registro |
| Observação | Informação complementar |

### Regra inicial para a razão

Quando não houver justificativa histórica específica conhecida:

> **Definição inicial da baseline de governança de permissões.**

Quando houver uma razão claramente conhecida, ela deve ser registrada explicitamente.

Exemplo:

> **Permitir que o cargo Aval-Gestão possa editar e administrar os canais de comunicação corporativa da Aval.**

---

## 3.2 Tabela 2 — Histórico de Alterações

### Finalidade

Registrar todas as alterações realizadas após a baseline.

### Pergunta que responde

> **O que mudou, quando mudou, por qual razão e quem demandou a alteração?**

### Campos principais

| Campo | Finalidade |
|---|---|
| Identificador da Alteração | Identificação única do evento |
| Membro | Membro envolvido, quando aplicável |
| Cargo | Cargo envolvido |
| Tipo de Recurso | Tipo do recurso afetado |
| Nome do Recurso | Nome do recurso no servidor |
| Categoria | Categoria relacionada, quando aplicável |
| Parâmetro | Configuração específica alterada |
| Status Anterior | Condição anterior |
| Status Atual | Condição resultante da alteração |
| Data/Hora da Mudança | Momento da alteração |
| Data do Último Inventário | Última data em que o parâmetro foi verificado |
| Razão da Última Atualização | Contexto e justificativa da atualização |
| Demandante | Quem solicitou a alteração |
| Responsável | Cargo responsável pela execução/manutenção |
| Permissão Efetiva | Resultado efetivo conhecido, quando aplicável |
| Observação | Informação complementar |

### Regra de responsabilidade

Para a estrutura atualmente definida:

- **Demandante** identifica quem solicitou ou motivou a alteração;
- **Responsável** identifica a função ou cargo responsável pela atualização.

No contexto atual, a administração é exercida por **Moacyr Blondet**, mas a estrutura deve registrar a responsabilidade de forma funcional, permitindo evolução futura.

---

## 3.3 Tabela 3 — Check de Consistência

Esta tabela deve incorporar a lógica enviada como exemplo pelo usuário.

### Finalidade

Avaliar a coerência entre:

- Status Atual;
- Data de Hoje / data de referência;
- Status Atual registrado;
- Data/Hora da Mudança;
- Data do Inventário.

A coluna **Conclusão** é resultado da análise e não deve ser tratada como variável de entrada.

### Exemplo conceitual fornecido

| Status Atual | Data de Hoje | Status Atual | Data da Mudança | Data do Inventário | Conclusão |
|---|---|---|---|---|---|
| S1 | DZ | S1 | DX | DY | Inventário Desatualizado |
| S1 | DZ | S1 | DX | DX | Sem Mudança na Data DZ |
| S1 | DZ | S1 | DZ | DZ | ERRO entre os campos status. Não está sendo descrita a mudança. |
| S1 | DZ | S2 | DZ | DZ | OK |

### Regra conceitual

Todas as variáveis da combinação são campos analisados pela regra, com exceção da **Conclusão**, que é produzida pela análise.

A nomenclatura dos resultados pode ser padronizada posteriormente conforme o conjunto de regras for ampliado.

---

## 3.4 Tabela 4 — Glossário

O Glossário passa a acumular duas funções:

1. glossário de termos e regras;
2. dicionário estruturado de objetos, artefatos, atributos e subatributos.

### Finalidade

Responder:

> **O que é cada elemento utilizado na governança, como ele se relaciona com os demais e como deve ser interpretado?**

### Estrutura conceitual

A categorização deve utilizar linguagem orientada a objeto.

Os principais níveis são:

```text
Artefato
   └── Tipo de Artefato
          └── Objeto
                 └── Atributo
                        └── Subatributo
```

A identificação da herança é necessária porque:

- um **Objeto** pode ser associado a diferentes artefatos;
- um **Atributo** pode estar associado a diferentes objetos;
- um **Subatributo** pode estar associado a diferentes atributos.

### Campos recomendados

| Campo | Finalidade |
|---|---|
| Termo / Nome | Nome do item documentado |
| Artefato | Artefato ao qual o item pertence |
| Tipo de Artefato | Classificação do artefato |
| Característica | Indica a natureza estrutural do item |
| Classificação Estrutural | Objeto, Atributo ou Subatributo |
| Item Pai / Herança | Identifica o elemento superior ao qual o item se relaciona |
| Campo | Nome do campo, quando aplicável |
| Finalidade | Para que serve |
| Significado | Como interpretar o item |
| Valores Permitidos | Valores aceitos, quando aplicável |
| Regra / Especificidade | Regra operacional ou condição especial |
| Observação Associada | Contexto adicional, alertas e exemplos |

### Exemplo de uso de “Observação Associada”

Para o campo **Razão da Última Atualização**, deve constar orientação equivalente a:

> **Tente realizar o preenchimento deste campo considerando a informação dentro de alguns destes contextos:**
>
> - alteração efetiva;
> - correção;
> - revisão;
> - sincronização;
> - inventário;
> - validação.

---

# 4. Status das permissões

## 4.1 Estados básicos

Os três estados principais são:

| Símbolo | Significado |
|---|---|
| X | Negado |
| / | Neutro / não definido explicitamente naquele nível |
| ✓ | Permitido |

## 4.2 Regra importante sobre “/”

O símbolo `/` **não significa necessariamente “sem efeito”**.

Ele representa uma condição neutra ou não explicitamente definida naquele nível.

A permissão efetiva poderá decorrer de:

- configuração do membro;
- permissões dos cargos;
- permissões da categoria;
- permissões do canal;
- regras de precedência e herança.

Portanto, a interpretação do status isolado deve ser evitada quando a análise envolver um membro específico.

---

# 5. Permissão Efetiva

A coluna **Permissão Efetiva** foi considerada fundamental.

Ela representa o resultado observado ou esperado após considerar os níveis relevantes.

Exemplo conceitual:

| Membro | Cargo | Recurso | Parâmetro | Status Local | Permissão Efetiva |
|---|---|---|---|---|---|
| Usuário A | Aval-Gestão | Canal X | Gerenciar Canal | / | ✓ |

Nesse caso, o `/` no recurso não significa que o membro não possa executar a ação. O resultado efetivo pode decorrer do cargo ou de outra regra de herança.

---

# 6. Categoria e Tipo de Recurso

Foi acordado que **Categoria** não deve competir semanticamente com **Tipo de Recurso**.

A estrutura recomendada é:

- **Tipo de Recurso**: identifica a natureza do recurso;
- **Nome do Recurso**: identifica o nome concreto utilizado no servidor;
- **Categoria**: fornece o contexto categorial do recurso, quando aplicável.

Exemplo:

| Tipo de Recurso | Nome do Recurso | Categoria |
|---|---|---|
| Categoria | APLICAÇÕES | — |
| Canal | aval-corp | APLICAÇÕES |
| Cargo | Aval-Gestão | — |

---

# 7. Cargo e Papel do Cargo

Cargo e papel são conceitos diferentes.

Portanto, não devem ser confundidos no mesmo atributo.

A estrutura adotada prioriza:

- **Cargo** como entidade de permissões;
- informações sobre papel funcional, quando necessárias, devem ser documentadas em campo próprio ou no Glossário.

O atributo **Papel do Cargo** não é obrigatório na matriz principal enquanto sua informação puder ser adequadamente mantida como metadado.

---

# 8. Razão da Última Atualização

A nomenclatura consolidada é:

> **Razão da Última Atualização**

Ela substitui formulações anteriores mais genéricas.

Seu objetivo é registrar o contexto da alteração mais recente.

A atualização pode decorrer, por exemplo, de:

- alteração efetiva;
- correção;
- revisão;
- sincronização;
- inventário;
- validação.

Essa orientação deve constar no Glossário, na coluna **Observação Associada**.

---

# 9. Demandante e Responsável

Os dois conceitos devem permanecer distintos.

## Demandante

Identifica quem solicitou ou originou a necessidade da alteração.

## Responsável

Identifica o cargo ou função responsável pela atualização e manutenção.

Essa separação permite distinguir:

```text
Quem pediu ≠ Quem executou ≠ Quem é responsável funcionalmente
```

---

# 10. Nomenclatura dos arquivos

A convenção acordada é:

```text
<Tipo de Artefato>_<Artefato>_<Atributo>_<Versão>_<Data>_<Cargo Responsável>.<extensão>
```

O componente:

```text
<Atributo>
```

deve ser utilizado somente quando necessário.

### Significado dos componentes

| Componente | Finalidade |
|---|---|
| Tipo de Artefato | Classificação geral do arquivo |
| Artefato | Nome principal do artefato |
| Atributo | Elemento específico, quando necessário |
| Versão | Controle de versão |
| Data | Referência temporal |
| Cargo Responsável | Função ou cargo responsável pela atualização |
| Extensão | Formato do arquivo |

Exemplo conceitual:

```text
Governanca_Permissoes_Baseline_v1_20260820_Administrador.xlsx
```

A composição e o objetivo de cada componente devem estar documentados no Glossário.

---

# 11. Visão de base de dados

A estrutura pode ser interpretada como um pequeno modelo relacional.

## 11.1 Entidades principais

```text
┌───────────────┐
│   BASELINE    │
└───────┬───────┘
        │
        │ identifica condição inicial
        ▼
┌───────────────┐
│   PARÂMETRO   │◄──────────────┐
└───────┬───────┘               │
        │                       │
        │                       │
        ▼                       │
┌───────────────┐        ┌───────┴───────┐
│   RECURSO     │        │    CARGO      │
└───────┬───────┘        └───────────────┘
        │
        ▼
┌───────────────┐
│    MEMBRO     │
└───────┬───────┘
        │
        ▼
┌───────────────────┐
│ PERMISSÃO EFETIVA │
└───────────────────┘

BASELINE ──► HISTÓRICO DE ALTERAÇÕES
                  │
                  ▼
          CHECK DE CONSISTÊNCIA

GLOSSÁRIO ──► define e explica todos os elementos
```

---

## 11.2 Relações principais

### Baseline ↔ Histórico

A Baseline representa o ponto inicial.

O Histórico registra as mudanças posteriores.

Uma mesma combinação lógica de:

```text
Membro
+ Cargo
+ Tipo de Recurso
+ Nome do Recurso
+ Categoria
+ Parâmetro
```

pode possuir:

- uma referência de baseline;
- zero ou vários eventos de alteração.

### Histórico ↔ Check de Consistência

O histórico fornece dados temporais e de status para análise.

O Check de Consistência avalia combinações de:

- Status;
- Datas;
- Inventário.

### Glossário ↔ Todas as tabelas

O Glossário funciona como camada de metadados.

Ele define:

- artefatos;
- tipos de artefato;
- objetos;
- atributos;
- subatributos;
- campos;
- valores;
- regras;
- heranças;
- especificidades.

---

# 12. Resumo consolidado dos itens

| Item / Tema | Descritivo e para que serve | Parâmetros / Especificidades | Proposta anterior | Atualização acordada | Status |
|---|---|---|---|---|---|
| 1. Baseline | Registrar a referência inicial da governança | Estado inicial, razão, data e contexto | Baseline como configuração atual | Baseline passou a representar a condição inicial considerada e sua razão | Fechado |
| 2. Status Atual | Representar a condição mais recente conhecida | Status, data da mudança e inventário | Status tratado de forma mais isolada | Diferenciado claramente de baseline e inventário | Fechado |
| 3. Inventário | Registrar a última verificação do parâmetro | Data do Inventário | Poderia ser confundido com atualização | Conceito separado de mudança | Fechado |
| 4. Check de Consistência | Validar coerência entre status e datas | Todas as variáveis de entrada; Conclusão como saída | Regra conceitual inicial | Incorporado como tabela de metadados com exemplo fornecido | Fechado |
| 5. Permissão Efetiva | Mostrar o impacto real da combinação de níveis | Membro, cargo, categoria, canal e parâmetro | Discussão sobre herança | Coluna explicitamente adotada | Fechado |
| 6. Membro | Permitir análise efetiva por usuário | Membro relacionado à configuração | Relação membro/cargo poderia ser tabela separada | Mantido nas tabelas principais quando aplicável | Fechado |
| 7. Cargo | Identificar papel de permissões | Cargo como entidade própria | Papel e cargo potencialmente misturados | Conceitos separados | Fechado |
| 8. Razão da Última Atualização | Registrar contexto da alteração mais recente | Alteração, correção, revisão, sincronização, inventário ou validação | Razão da alteração | Nome consolidado e orientação documentada no Glossário | Fechado |
| 9. Demandante | Identificar origem da solicitação | Pessoa, papel ou entidade demandante | Não existia inicialmente | Adicionado ao Histórico | Fechado |
| 10. Responsável | Identificar responsabilidade funcional | Cargo Responsável | Responsável como pessoa | Consolidado como responsabilidade funcional | Fechado |
| 11. Tipo de Recurso | Identificar a natureza do recurso | Cargo, Categoria, Canal etc. | Discussão sobre coluna Canal | Adotado “Tipo de Recurso” + “Nome do Recurso” | Fechado |
| 12. Categoria | Contextualizar o recurso | Categoria relacionada | Potencial conflito com Tipo de Recurso | Mantida como contexto, não como substituta do tipo | Fechado |
| 13. Glossário | Ser a camada central de metadados | Artefato, tipo, objeto, atributo, subatributo e herança | Dicionário de campos separado | Consolidado no Glossário | Fechado |
| 14. Status X / / / ✓ | Padronizar a representação de permissões | Negado, neutro e permitido | Possibilidade de interpretação simplificada | “/” explicitamente definido como não necessariamente sem efeito | Fechado |
| 15. Nomenclatura de Arquivos | Padronizar identificação documental | Tipo de Artefato, Artefato, Atributo opcional, Versão, Data, Cargo Responsável | Nomenclatura mais simples | Convenção consolidada | Fechado |
| 16. Automação futura | Possibilitar inventário automático | Discord, coleta estruturada, comparação e IA | Ideia futura | Estrutura preparada para automação | Diretriz futura |

---

# 13. Processo operacional da governança

## Etapa 1 — Inventário

Coletar as configurações reais do servidor.

A coleta inicial pode ser realizada por:

- interface do Discord;
- registros documentais;
- screenshots;
- futuramente, API e automação.

---

## Etapa 2 — Construção da Baseline

Registrar:

- recurso;
- categoria;
- membro;
- cargo;
- parâmetro;
- condição inicial;
- permissão efetiva, quando aplicável;
- razão da configuração inicial.

---

## Etapa 3 — Registro de alterações

Toda alteração posterior à baseline deve gerar registro no Histórico.

A alteração deve conter, no mínimo:

- condição anterior;
- condição resultante;
- data/hora;
- razão da última atualização;
- demandante;
- responsável;
- última data de inventário.

---

## Etapa 4 — Inventários recorrentes

Periodicamente, as configurações devem ser verificadas.

O inventário:

- não substitui a data da última mudança;
- atualiza a data do inventário;
- pode identificar divergências;
- pode alimentar o Check de Consistência.

---

## Etapa 5 — Análise de consistência

O Check de Consistência deve avaliar:

- divergência entre status;
- mudança sem registro temporal adequado;
- inventário desatualizado;
- combinações válidas;
- outras regras que venham a ser formalizadas.

---

# 14. Preparação para automação e IA

Sim. Esta estrutura é **fortemente compatível com a realização futura de inventário automático das permissões do Discord**, inclusive com apoio de IA.

A razão é que o modelo está separando adequadamente:

1. **dados observados** — permissões e recursos;
2. **dados históricos** — alterações;
3. **metadados** — Glossário;
4. **regras de consistência** — Check de Consistência;
5. **interpretação** — Permissão Efetiva e regras de herança.

Uma arquitetura futura poderia funcionar assim:

```text
Discord
   │
   ▼
Coletor automático
   │
   ├── Servidor
   ├── Cargos
   ├── Membros
   ├── Categorias
   ├── Canais
   └── Permissões
          │
          ▼
Inventário estruturado
          │
          ├── Comparação com Baseline
          ├── Comparação com último inventário
          ├── Atualização do Histórico
          └── Check de Consistência
                    │
                    ▼
              Camada de IA
                    │
                    ├── Detectar anomalias
                    ├── Explicar diferenças
                    ├── Identificar impactos
                    └── Gerar relatório
```

A IA não deveria ser a fonte primária da verdade das permissões.

O inventário deve ser baseado em dados estruturados extraídos do Discord. A IA pode atuar principalmente como camada de:

- análise;
- explicação;
- detecção de inconsistências;
- geração de documentação;
- apoio à tomada de decisão.

Essa separação reduz o risco de a IA “interpretar” uma configuração inexistente ou substituir o dado efetivamente observado.

---

# 15. Diretriz futura de snapshot automático

A criação de um **snapshot automático das permissões reais do servidor** permanece como uma proposta para release futura.

Esse mecanismo poderá:

1. coletar a estrutura real do servidor;
2. gerar um inventário datado;
3. comparar o inventário com a baseline;
4. comparar com o inventário anterior;
5. identificar mudanças;
6. alimentar o Histórico;
7. executar os checks de consistência;
8. gerar um relatório para validação humana.

O princípio recomendado é:

> **Automação coleta. Regras comparam. IA analisa. Humano valida.**

---

# 16. Situação atual da governança

## Estrutura funcional

| Componente | Situação |
|---|---|
| Baseline | Definida |
| Histórico de Alterações | Definido |
| Check de Consistência | Definido conceitualmente e com exemplo inicial |
| Glossário | Definido como camada central de metadados |
| Permissão Efetiva | Aprovada |
| Membro | Incluído no modelo |
| Cargo | Incluído no modelo |
| Herança | A ser explicitada no Glossário |
| Status X / / / ✓ | Definido |
| Inventário | Diferenciado de atualização |
| Razão da Última Atualização | Definida |
| Demandante | Incluído |
| Responsável funcional | Definido |
| Convenção de nomenclatura | Definida |
| Snapshot automático | Roadmap futuro |
| Inventário automático com IA | Viável como evolução futura |

---

# 17. Próximo passo recomendado

O próximo passo é operacional:

1. consolidar os prints das permissões;
2. extrair os recursos, cargos, membros e parâmetros observados;
3. preencher a tabela **Baseline**;
4. registrar no **Histórico de Alterações** as mudanças já conhecidas e suas razões;
5. estruturar o **Glossário**;
6. implementar o primeiro conjunto de regras do **Check de Consistência**;
7. utilizar a planilha como fonte oficial da baseline de governança.

A partir da baseline estabelecida:

> **qualquer alteração posterior deverá obrigatoriamente entrar no Histórico de Alterações, com sua justificativa e seus dados temporais.**

Assim, não se tenta criar uma falsa precisão sobre todo o passado. A governança passa a possuir **rastreabilidade real a partir do ponto em que a baseline é formalizada**.
