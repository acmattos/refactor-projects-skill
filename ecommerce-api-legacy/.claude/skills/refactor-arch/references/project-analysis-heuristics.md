# Project Analysis Heuristics

Use este arquivo durante a PHASE 1.

## Objetivo

Inferir o contexto do projeto antes da auditoria.

A análise deve ser technology-agnostic e baseada em evidências.

## Language detection

Sinais comuns:

- JavaScript/TypeScript:
  - `package.json`
  - `package-lock.json`
  - `pnpm-lock.yaml`
  - `yarn.lock`
  - `.js`, `.jsx`, `.ts`, `.tsx`
  - `tsconfig.json`

- Python:
  - `requirements.txt`
  - `pyproject.toml`
  - `Pipfile`
  - `poetry.lock`
  - `.py`

- Java/Kotlin:
  - `pom.xml`
  - `build.gradle`
  - `settings.gradle`
  - `.java`, `.kt`

- PHP:
  - `composer.json`
  - `.php`

- Ruby:
  - `Gemfile`
  - `.rb`

- C#/.NET:
  - `.csproj`
  - `.sln`
  - `.cs`

- Go:
  - `go.mod`
  - `.go`

- Rust:
  - `Cargo.toml`
  - `.rs`

## Framework detection

Identifique o framework principal a partir de sinais observáveis — não assuma pelo nome do projeto:

- Nome da dependência no arquivo de manifest (requirements.txt, package.json, pom.xml, Gemfile etc.)
- Imports ou annotations no arquivo de bootstrap ou entry point
- Decorators/annotations de routing (`@app.route`, `@Get`, `@RestController`, `@Controller` etc.)
- Arquivos de configuração específicos de framework (`django settings`, `application.yml`, `nest-cli.json` etc.)
- Convenções de diretório impostas pelo framework (`app/controllers/`, `src/main/java/` etc.)

Não declare framework sem ao menos um desses sinais no repositório.

## Entry point detection

Identifique como a aplicação é iniciada:

- Arquivos nomeados `main.*`, `app.*`, `index.*`, `server.*`, `Application.*` na raiz ou em `src/`
- Presença de função de bootstrap (`app.run()`, `server.listen()`, `SpringApplication.run()` etc.)
- Scripts de execução em `package.json` (`scripts.start`, `scripts.dev`), `Makefile`, `Procfile`
- `CMD` ou `ENTRYPOINT` em `Dockerfile`
- `command:` em `docker-compose.yml`
- Instruções de execução em README

Use o entry point detectado na PHASE 3 para o comando de boot validation.

## Test framework detection

Identifique se existem testes e qual o framework utilizado:

- Diretórios: `test/`, `tests/`, `spec/`, `__tests__/`
- Padrões de arquivo: `*_test.*`, `test_*.*`, `*.test.*`, `*.spec.*`
- Arquivos de configuração de test runner: `pytest.ini`, `jest.config.*`, `.mocharc.*`, `karma.conf.*`, `phpunit.xml`, `rspec` etc.
- Entrada `test` em scripts de manifest (`package.json`, `Makefile`)
- Imports de framework de teste nos arquivos de teste

Se não houver evidência de testes, reporte "None detected" no campo correspondente da PHASE 1.

## API style detection

Identifique o estilo da API a partir de sinais observáveis:

- **REST**: rotas com métodos HTTP explícitos (GET, POST, PUT, DELETE, PATCH), paths com segmentos de recurso, arquivos de rota ou controller por domínio
- **GraphQL**: arquivos `.graphql` ou `.gql`, schema definitions, funções resolver, imports de biblioteca graphql
- **gRPC / Protobuf**: arquivos `.proto`, imports de geração de stub, serviços com métodos tipados
- **RPC genérico / outro**: arquivos de definição de protocolo, serializers binários, endpoint único com envelope de mensagem

Use o estilo detectado para montar o inventário de endpoints na PHASE 3.

## Database detection

Use evidências como:

- migrations
- schema files
- ORM models
- SQL queries
- repositories
- connection strings
- database adapters
- Docker Compose services
- environment variables relacionadas a banco
