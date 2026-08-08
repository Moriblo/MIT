/plano

Leia os seguintes arquivos:

- avalbot/docs/persona.md
- avalbot/docs/r2v1-implementation-plan.md

Resuma:

1. Objetivo da release R2V1
2. Personas existentes
3. Decisões arquiteturais registradas
4. Pendências abertas

Não altere nada.
Copiar
Observação sobre o arquivo solicitado
Você pediu avalbot/docs/persona.md, mas esse arquivo não existe no repositório. O arquivo existente e correspondente é avalbot/docs/personas.md, que foi lido junto com avalbot/docs/r2v1-implementation-plan.md.

1. Objetivo da release R2V1
A R2V1 é a baseline oficial de escopo do AvalBot. Ela define o conjunto inicial aprovado de entregas, contra o qual progresso, mudanças de escopo e funcionalidades entregues deverão ser avaliados. O acompanhamento operacional deve ocorrer exclusivamente pelo GitHub Project avalbot. 

A release será considerada completa quando todos os itens da baseline forem entregues, os critérios de aceitação forem aprovados, os testes funcionais passarem, o bot estiver operacional no Discord, as personas forem configuráveis externamente, as sessões de usuários forem persistidas e a solução estiver rodando continuamente na Azure. 

Os entregáveis previstos incluem documentação, arquivos de configuração, serviços Python, pacote de release e infraestrutura Azure. 

2. Personas existentes
O documento define três personas ativas no portfólio atual: Aval, Governança IA e Pirate. Todas têm como responsável Moacyr Ribeiro Blondet. 

Aval
Aval é a persona padrão, do tipo General Assistant. Sua missão é atender todos os usuários com respostas equilibradas, práticas e úteis em diversos temas. 

Sua política de acesso indica disponibilidade para todos os usuários, e seu status está ativo. 

Governança IA
Governança IA é uma persona especialista em governança de IA, voltada a apoiar organizações e profissionais na compreensão, desenho e implementação de práticas responsáveis de governança de IA. 

Seu acesso é controlado por roles do Discord, e seu status está ativo. 

Pirate
Pirate é uma persona de personagem, voltada a interações criativas, engajantes e divertidas, mantendo utilidade, inteligência e respeito. 

Seu comportamento deve manter uma personalidade inspirada em piratas, mas sem narrar ações, usar direções de palco ou quebrar personagem desnecessariamente. 

Seu acesso também é controlado por roles do Discord, e seu status está ativo. 

3. Decisões arquiteturais registradas
As personas são tratadas como a camada comportamental da plataforma: o código implementa a mecânica, enquanto as personas definem inteligência, estilo de comunicação, especialização e experiência do usuário. 

O ciclo de vida definido para personas é: personas.md → personas.json → Persona Service → Groq Prompt Builder → Groq API → resposta ao usuário. 

Cada persona deve definir identidade, missão, responsável, expertise, estilo de comunicação, regras comportamentais, template de prompt e política de acesso. 

As regras de governança estabelecem que todas as personas devem ser definidas no documento antes de serem adicionadas à plataforma, ter identificador único, possuir template de prompt, definir política de acesso e declarar um responsável. O documento personas.md é a fonte oficial da verdade, e personas.json deve ser gerado a partir das definições aprovadas nele. 

A arquitetura planejada inclui serviços separados para comandos, Discord, Groq, personas e sessões dentro de src/. 

Também há decisão de governança de escopo: a baseline da R2V1 não deve ser modificada retroativamente; mudanças durante o desenvolvimento devem ser gerenciadas pelo GitHub Project. 

4. Pendências abertas
As pendências abertas registradas no plano incluem:

Concluir a estrutura do repositório, marcada como em progresso. 

Criar personas.json e sessions.json. 

Criar os serviços centrais persona_service.py, session_service.py e groq_service.py. 

Criar command_service.py e implementar os comandos $perfis, $perfil, $ajuda e $whoami. 

Integrar os serviços com o Discord. 

Executar testes funcionais. 

Publicar a Release R2V1. 

Preparar o ambiente Azure e implantar o AvalBot 24x7 na Azure. 

Comandos executados
Testing / checks

✅ find .. -name AGENTS.md -print

⚠️ sed -n '1,240p' avalbot/docs/persona.md — arquivo solicitado não existe; o repositório contém avalbot/docs/personas.md.

✅ sed -n '1,260p' avalbot/docs/r2v1-implementation-plan.md

✅ find avalbot -maxdepth 3 -type f | sort

✅ nl -ba avalbot/docs/personas.md | sed -n '1,260p'

✅ nl -ba avalbot/docs/r2v1-implementation-plan.md | sed -n '1,260p'

✅ nl -ba avalbot/docs/personas.md | sed -n '260,420p'

✅ git status --short