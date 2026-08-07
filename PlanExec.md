# MIT AI Program Office
## Plano de Execução - Próximos Passos

| Seq. | Origem | Etapa | Prompt para o Codex | Saída Esperada | Status |
|------:|--------|--------|---------------------|----------------|:------:|
| 1 | T8 | Criar `KNOWLEDGE_MODEL.md` | Utilize o documento anexo contendo a proposta de governança aprovada no Teste T8 como referência arquitetural. Com base nesse documento, crie o arquivo `KNOWLEDGE_MODEL.md`. Preserve a estrutura atual do repositório. Não altere outros arquivos. Abra um Draft Pull Request e aguarde revisão humana. | Draft PR contendo apenas `KNOWLEDGE_MODEL.md`. | ⬜ |
| 2 | — | Revisar `KNOWLEDGE_MODEL.md` | — | Documento aprovado. | ⬜ |
| 3 | — | Merge do PR | — | `KNOWLEDGE_MODEL.md` incorporado ao repositório. | ⬜ |
| 4 | T8 + `KNOWLEDGE_MODEL.md` | Criar `glossary.md` | Analise o `KNOWLEDGE_MODEL.md` e a proposta de governança do Teste T8. Proponha o `glossary.md` do MIT AI Program Office contendo exclusivamente conceitos de Programa/Portfólio. Não inclua termos específicos dos projetos. Abra um Draft Pull Request e aguarde revisão humana. | Draft PR contendo apenas `glossary.md`. | ⬜ |
| 5 | — | Revisar `glossary.md` | — | Glossário aprovado. | ⬜ |
| 6 | — | Merge do PR | — | `glossary.md` incorporado ao repositório. | ⬜ |
| 7 | T8 + `KNOWLEDGE_MODEL.md` + `glossary.md` | Criar `protocols.md` | Analise o `KNOWLEDGE_MODEL.md`, o `glossary.md` e a proposta de governança do Teste T8. Proponha um `protocols.md` mínimo para orientar agentes de IA, Codex e colaboradores humanos. Inclua apenas protocolos gerais do MIT AI Program Office. Abra um Draft Pull Request e aguarde revisão humana. | Draft PR contendo apenas `protocols.md`. | ⬜ |
| 8 | — | Revisar `protocols.md` | — | Protocolos aprovados. | ⬜ |
| 9 | — | Merge do PR | — | `protocols.md` incorporado ao repositório. | ⬜ |
| 10 | T8 + Artefatos criados | Validar Governança v1.0 | Analise o estado atual do repositório e confirme se `README.md`, `KNOWLEDGE_MODEL.md`, `glossary.md` e `protocols.md` estão consistentes entre si. Não proponha alterações. Apenas apresente um parecer sobre a prontidão da Governança v1.0. | Parecer de prontidão da Governança v1.0. | ⬜ |
| 11 | Governança v1.0 | Retomar AvalBot R2V1 | Assimile o estado atual do MIT AI Program Office e do projeto AvalBot. Considere a Governança v1.0 estabelecida. A partir deste ponto, priorize exclusivamente a implementação da Release R2V1 do AvalBot. Antes de alterar qualquer arquivo, apresente o plano de execução da R2V1 para aprovação humana. | Plano de execução da Release R2V1. | ⬜ |

## Critério de Encerramento da PoC

A PoC será considerada concluída após a conclusão do passo **10**, quando a Governança v1.0 estiver validada.

A partir do passo **11**, o foco passa a ser exclusivamente a evolução funcional do projeto **AvalBot R2V1**, utilizando a governança estabelecida apenas como suporte ao desenvolvimento.
