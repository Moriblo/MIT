/plano Explique a estrutura deste repositório.\nListe os diretórios principais.\nMostre quais arquivos parecem ser documentos de arquitetura, requisitos ou planejamento.\nNão altere nada.
Copiar
Estrutura do repositório
O repositório /workspace/MIT é pequeno e parece reunir materiais de estudo/projeto do curso “Inteligência Artificial Agêntica Aplicada à Transformação Empresarial”. A raiz contém apenas um README.md geral e dois diretórios principais: avalbot e dbot. O README.md raiz descreve o propósito amplo do repositório como “Trabalhos e insights” do curso. 

Diretórios principais
avalbot/
Projeto documentado como uma plataforma multi-persona de IA integrada ao Discord e Groq. O README.md do diretório indica que a release atual é R2V1, em desenvolvimento, com alvo de deploy em Azure VM, runtime Python, motor Groq e canal Discord. 

Conteúdo observado:

avalbot/README.md — documento central do projeto AvalBot, com visão, escopo, status, arquitetura e fluxo de interação.

avalbot/docs/ — diretório de documentação do AvalBot.

persona.md — catálogo de personas e definições comportamentais.

r2v1-implementation-plan.md — plano/baseline de implementação da release R2V1.

avalbot/sessions.json — arquivo JSON de sessões, atualmente vazio ({}).

dbot/
Projeto de bot Discord mais simples, descrito como um bot que responde “como um pirata”. 

Conteúdo observado:

dbot/README.md — instruções de configuração e execução.

dbot/discord_only.py — bot Discord mínimo que responde ao comando $hello. 

dbot/mybot.py — bot Discord que chama a API Groq e pede respostas em estilo pirata. 

dbot/mybot_v2.py — versão mais elaborada do bot “Pirate”, com prompt de sistema, limpeza de resposta, chamada ao Groq e comandos Discord. 

dbot/requirements.txt — dependências Python, incluindo discord.py, python-dotenv, openai, azure-ai-projects e azure-identity. 

dbot/.env — arquivo de ambiente presente no diretório. Não detalhei seu conteúdo por ser potencialmente sensível.

dbot/.gitignore

dbot/LICENSE

Arquivos que parecem ser documentos de arquitetura, requisitos ou planejamento
Documentos de arquitetura
avalbot/README.md — contém uma seção explícita de arquitetura de alto nível, incluindo visão conceitual com Discord, AvalBot, serviços de persona/sessão/comando, arquivos personas.json/sessions.json, Groq Service e Groq. 

avalbot/README.md — também descreve o fluxo de interação entre usuário, mensagem Discord, identificação de usuário, sessão ativa, persona, prompt, Groq e resposta ao Discord. 

Documentos de requisitos / escopo funcional
avalbot/README.md — define o objetivo da release R2V1: múltiplas personas, configuração externa, persistência de sessão, gerenciamento de perfil ativo, integração Discord/Groq, base de autorização por papéis e preparação para Azure. 

avalbot/README.md — lista entregáveis funcionais, técnicos e de governança, incluindo seleção/troca de persona, persistência de sessão, prompts por persona, comandos Discord, integração Groq, arquitetura modular e uso de Discord Roles como autorização. 

avalbot/docs/persona.md — define requisitos/estrutura das personas: identidade, missão, responsável, expertise, estilo de comunicação, regras comportamentais, prompt template e política de acesso. 

Documentos de planejamento
avalbot/docs/r2v1-implementation-plan.md — é o documento mais claramente voltado a planejamento. Ele declara que preserva o escopo original aprovado da Release R2V1 e serve como baseline para avaliar progresso, mudanças de escopo e entregas. 

avalbot/docs/r2v1-implementation-plan.md — organiza o trabalho em fases F1 a F9, cobrindo planejamento/repositório, personas, configuração, serviços core, comandos, integração Discord, testes, release packaging e deploy Azure. 

avalbot/docs/r2v1-implementation-plan.md — lista os artefatos esperados ao fim da R2V1: documentação, configuração, código-fonte em src/, pacote de release e infraestrutura Azure. 

avalbot/docs/r2v1-implementation-plan.md — define critérios de sucesso, incluindo testes funcionais bem-sucedidos, bot operacional no Discord, personas configuráveis externamente, sessões persistidas e execução contínua no Azure. 

Documentos operacionais / setup
dbot/README.md — documenta configuração de .env, tokens do Discord/Groq e comandos para executar os bots discord_only.py e mybot.py. 

dbot/requirements.txt — funciona como arquivo de dependências do projeto Python. 

Observações importantes
Há uma diferença de nomenclatura: o plano menciona docs/personas.md, mas no repositório o arquivo encontrado é avalbot/docs/persona.md no singular. O plano cita docs/personas.md como documentação esperada.  O arquivo existente se chama persona.md e define o catálogo oficial de personas. 

O plano R2V1 prevê uma estrutura futura src/ com serviços modulares (main.py, command_service.py, discord_service.py, groq_service.py, persona_service.py, session_service.py), mas essa estrutura ainda não aparece nos arquivos observados; ela está descrita como entregável planejado. 

O diretório dbot/ parece ser uma implementação/protótipo funcional anterior ou paralela, enquanto avalbot/ parece ser o projeto mais estruturado e planejado para evolução multi-persona.

Comandos executados
Testing

✅ pwd && find .. -name AGENTS.md -print

✅ find . -maxdepth 1 -mindepth 1 -printf '%y %p\n' | sort

✅ find . -type f \( -iname '*arch*' -o -iname '*architecture*' -o -iname '*requirement*' -o -iname '*requirements*' -o -iname '*plan*' -o -iname '*planning*' -o -iname '*design*' -o -iname '*roadmap*' -o -iname '*spec*' -o -iname 'README*' -o -iname 'CONTRIBUTING*' -o -iname 'docs*' \) -printf '%p\n' | sort | head -200

✅ git status --short

✅ find . -maxdepth 3 -not -path './.git*' -printf '%y %p\n' | sort

✅ sed -n '1,220p' README.md

✅ sed -n '1,220p' avalbot/README.md

✅ sed -n '1,220p' avalbot/docs/r2v1-implementation-plan.md

✅ sed -n '1,160p' avalbot/docs/persona.md

✅ sed -n '1,220p' dbot/README.md

✅ cat dbot/requirements.txt

✅ nl -ba README.md avalbot/README.md avalbot/docs/r2v1-implementation-plan.md avalbot/docs/persona.md dbot/README.md dbot/requirements.txt

✅ for f in dbot/*.py; do nl -ba "$f" | sed -n '1,180p'; done

✅ nl -ba avalbot/sessions.json | sed -n '1,80p'

Não alterei nenhum arquivo, conforme solicitado.