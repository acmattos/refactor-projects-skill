# Phase 2 Report Template

Use este arquivo durante a PHASE 2.

O template obrigatório de campos e labels continua sendo o definido no `SKILL.md`.

## O que conta como evidence concreta

Evidence concreta é qualquer um dos itens abaixo observado diretamente no repositório:
- Linha de código específica (cite file path e line range)
- Entrada no arquivo de dependências (requirements.txt, package.json, pom.xml etc.)
- Chave de configuração em arquivo de settings ou .env
- Warning de build, lint ou runtime presente no repositório
- Comentário no próprio código (TODO, FIXME, deprecated, legacy)

Não declare um anti-pattern sem ao menos uma dessas evidências.

## Exemplo de finding completo

[HIGH] Fat Controller
File: src/controllers/task_controller.py:45-112
Description: A função `create_task` (linha 45) executa validação de input, acessa o banco via SQLAlchemy diretamente e formata a resposta — três responsabilidades distintas em um único handler HTTP.
Impact: Qualquer mudança em validação, persistência ou formato de resposta exige editar o mesmo método; testabilidade reduzida pois o controller não pode ser testado sem banco real.
Recommendation: Extrair validação para um command/schema, persistência para um repository e formatação para um presenter. Ver Pattern 1 e Pattern 2 em `references/refactoring-playbook.md`.

## Checklist de qualidade antes de finalizar a PHASE 2

- Cada finding cita file path e line range concretos
- Cada finding conecta o problema a MVC/SOLID/security/maintainability
- Findings com mesma root cause estão agrupados
- Nenhum finding é advice genérico sem evidência no código
- A frase de pausa obrigatória aparece no chat (não no arquivo gravado)
