# MVC Architecture Guidelines

Use este arquivo durante a PHASE 2 e PHASE 3.

A arquitetura alvo é MVC-aligned e technology-agnostic.

Não force folder names durante a análise (PHASE 2) — avalie responsabilidades reais, não nomes de diretórios.
Durante a refatoração (PHASE 3), crie a estrutura de diretórios por camada obrigatoriamente.

## Organização de arquivos

- Todo o código da aplicação reside dentro de `src/`, incluindo o entry point (ex: src/app.py). O root do projeto contém apenas arquivos de manifesto (ex: requirements.txt, package.json) e arquivos de ambiente (ex: .env, Dockerfile).
- Exceção: um wrapper mínimo no root é permitido exclusivamente para preservar a compatibilidade com comandos externos que dependam do entry point original (ex: `python app.py`). O wrapper deve apenas reexportar o entry point real em `src/` e conter um comentário documentando a exceção. Essa exceção não se aplica a scripts auxiliares (seed, migration, etc.) — esses pertencem a `src/infrastructure/` sem exceção.
- Dentro de `src/`, crie um diretório por camada: models/, controllers/, views/, repositories/, services/, infrastructure/ ou equivalentes idiomáticos da stack detectada.
- Cada domínio ou entidade deve ter seu próprio arquivo por camada: um controller por domínio, um model por entidade, um routes file por contexto de apresentação.
- Não concentre múltiplos domínios em um único arquivo de controller, model ou view.
- Código de infraestrutura (conexão com banco, schema, seeds, clientes externos) pertence a src/infrastructure/ — nunca ao root do projeto nem a outras camadas.
- Adapte naming e extensões às convenções da linguagem e framework — o princípio de separação por camada é invariante.

## Controllers / Handlers

Controllers devem:

- receber HTTP/framework input
- coordenar request flow
- delegar business decisions
- chamar services/use cases
- retornar responses ou views

Controllers não devem:

- conter SQL direto
- conter business rules complexas
- conter persistence logic
- conter formatting complexo
- depender diretamente de secrets ou environment variables

## Models / Domain Entities

Models devem:

- representar domain state
- proteger invariants
- conter domain behavior quando apropriado
- evitar framework leakage
- evitar dependência direta de database, HTTP ou external SDKs

## Views / Routes / Presentation

Views, routes, serializers, DTO mappers e presenters devem:

- formatar output
- renderizar templates
- serializar responses
- mapear dados para response contracts

Views/serializers não devem:

- executar business workflows
- acessar database diretamente
- tomar decisões de domínio complexas

## Services / Use Cases

Services/use cases devem:

- orquestrar workflows
- coordenar domain, repositories e integrations
- manter framework details nas boundaries
- ser testáveis sem HTTP runtime quando possível

## Repositories / Gateways

Repositories/gateways devem:

- isolar persistence
- esconder SQL, ORM, SDK ou client details
- expor contracts claros
- evitar business rules que pertencem ao domain

## Infrastructure

Infrastructure contém os detalhes técnicos de baixo nível que suportam todas as outras camadas.

Infrastructure deve:

- gerenciar conexões com banco de dados (setup, teardown, per-request lifecycle)
- criar e migrar schemas quando não há ferramenta dedicada de migration
- inicializar dados de seed
- instanciar clientes externos (HTTP clients, SDKs de cloud, message brokers)

Infrastructure não deve:

- conter business rules
- conter domain logic
- ser importada por Models ou Domain entities
- expor detalhes de implementação além da sua própria camada

Exemplos: database.py (conexão SQLite/Postgres), redis_client.py, s3_client.py, smtp_client.py.

O entry point da aplicação (app.py) pode importar infrastructure para inicialização, mas demais camadas importam apenas os contratos (ex: get_db de infrastructure/database.py).

## Dependency direction

Direção preferida:

```text
Presentation -> Application -> Domain
Presentation -> Infrastructure
Application -> Ports
Infrastructure -> Ports
Infrastructure -> External Systems
Domain -> no framework or infrastructure dependencies
```

Evite:

```text
Domain -> Controller
Domain -> HTTP Framework
Domain -> ORM Session
Domain -> Cloud SDK
Controller -> SQL Query
View -> Database
Serializer -> Business Workflow
```

## Cross-domain Coupling

Domínios não devem importar implementações uns dos outros diretamente.
Se Domain A precisa de dados de Domain B, acesse através de um repository port ou contrato de serviço — nunca importando Model, Repository ou Service de B diretamente.
Imports bidirecionais entre domínios são sinal de acoplamento indevido e devem ser tratados como violação de DIP.

## Circular Dependencies

Sinal: Módulo A importa B, B importa A (direta ou transitivamente).
Resolução preferida: extrair o contrato compartilhado para um módulo neutro que ambos importam — nenhum dos dois importa o outro.
Alternativa: inverter a dependência — o módulo de nível mais alto depende de uma abstração (port/interface), não da implementação do módulo de nível mais baixo.
Circular dependencies entre camadas (ex: repository importando controller) indicam inversão de layering e devem ser corrigidas antes de qualquer outra refatoração.
