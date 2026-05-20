# Skill de Auditoria e Refatora��o Arquitetural

## Desafio MBA Engenharia de Software com IA - Full Cycle

# Refactor Projects Skill

## Analise Manual
 lista dos problemas identificados, classificação por severidade e justificativa 
 de por que cada problema é relevante.

### Projeto [code-smells-project](./code-smells-project)
| Linguagem | Framework | Domínio           | Número de arquivos |
| --------- |-----------|-------------------|--------------------|
| Python    | Flask     | API de E-commerce | 4                  |

#### Problemas identificados:
| Severidade | Falha                        | Justificativa                                                                                                             |
|------------|------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| CRITICAL   | Credenciais Hardcoded        | Senha `minha-chave-super-secreta-123` exposta em `app.py`                                                                 |
| CRITICAL   | Credenciais Hardcoded        | Senha `admin123` exposta em `database.py`                                                                                 |
| CRITICAL   | Credenciais Hardcoded        | Senha `123456` exposta em `database.py`                                                                                   |
| CRITICAL   | Credenciais Hardcoded        | Senha `senha123` exposta em `database.py`                                                                                 |
| CRITICAL   | SQL Injection                | Metodo `get_produto_por_id` exposto em `models.py`                                                                        |
| CRITICAL   | SQL Injection                | Metodo `criar_produto` exposto em `models.py`                                                                             |
| CRITICAL   | SQL Injection                | Metodo `atualizar_produto` exposto em `models.py`                                                                         |
| CRITICAL   | SQL Injection                | Metodo `deletar_produto` exposto em `models.py`                                                                           |
| CRITICAL   | SQL Injection                | Metodo `get_usuario_por_id` exposto em `models.py`                                                                        |
| CRITICAL   | SQL Injection                | Metodo `login_usuario` exposto em `models.py`                                                                             |
| CRITICAL   | SQL Injection                | Metodo `criar_usuario` exposto em `models.py`                                                                             |
| CRITICAL   | SQL Injection                | Metodo `criar_pedido` exposto em `models.py`                                                                              |
| CRITICAL   | SQL Injection                | Metodo `get_pedidos_usuario` exposto em `models.py`                                                                       |
| CRITICAL   | SQL Injection                | Metodo `atualizar_status_pedido` exposto em `models.py`                                                                   |
| CRITICAL   | SQL Injection                | Metodo `buscar_produtos` exposto em `models.py`                                                                           |
| CRITICAL   | SQL Injection                | Metodo `executar_query` exposto em `app.py`                                                                               |
| CRITICAL   | God Class                    | Arquivo `models.py` faz CRUD de produto, usuario, pedido, relatorio                                                       |
| CRITICAL   | God Class                    | Arquivo `database.py` cria conexao, banco de dados                                                                        |
| CRITICAL   | God Class                    | Arquivo `controllers.py` faz CRUD de produto, usuario, pedido, relatorio, faz login, aplica regras de negocios, acessa bd |
| CRITICAL   | God Class                    | Arquivo `app.py` faz configuracao da aplicacao, das rotas, acesso ao banco de dados                                       |
| HIGH       | Business Logic in Controller | Metodo `criar_produto` expoe regra em `controllers.py`                                                                    |
| HIGH       | Business Logic in Controller | Metodo `atualizar_produto` expoe regra em `contollers.py`                                                                 |
| HIGH       | Business Logic in Controller | Metodo `criar_usuario` expoe regra em `contollers.py`                                                                     |
| HIGH       | Business Logic in Controller | Metodo `login` expoe regra em `contollers.py`                                                                             |
| HIGH       | Business Logic in Controller | Metodo `criar_pedido` expoe regra em `contollers.py`                                                                      |
| HIGH       | Business Logic in Controller | Metodo `atualizar_status_pedido` expoe regra em `contollers.py`                                                           |
| HIGH       | Tight Coupling Without DI    | Arquivo `models.py` cria conexao com banco                                                                                |
| HIGH       | Tight Coupling Without DI    | Arquivo `controllers.py` cria conexao com banco, usa `models.py` diretamente                                              |
| HIGH       | Tight Coupling Without DI    | Arquivo `app.py` cria conexao com banco, usa `controllers.py` diretamente                                                 |
| HIGH       | Global Mutable State         | Arquivo `database.py` define `db_connection` e `db_path` globalmente                                                      |
| MEDIUM     | Feature Envy                 | Metodo `get_todos_produtos` no arquivo `models.py` monta a entidade produto                                               |
| MEDIUM     | Feature Envy                 | Metodo `buscar_produtos` no arquivo `models.py` monta a entidade produto                                                  |
| MEDIUM     | Feature Envy                 | Metodo `get_todos_usuarios` no arquivo `models.py` monta a entidade usuario                                               |
| MEDIUM     | Feature Envy                 | Metodo `get_usuario_por_id` no arquivo `models.py` monta a entidade usuario                                               |
| MEDIUM     | Feature Envy                 | Metodo `login_usuario` no arquivo `models.py` monta a entidade usuario                                                    |
| MEDIUM     | Feature Envy                 | Metodo `get_pedidos_usuario` no arquivo `models.py` monta a entidade pedido                                               |
| MEDIUM     | Feature Envy                 | Metodo `get_todos_pedidos` no arquivo `models.py` monta a entidade pedido                                                 |
| MEDIUM     | Feature Envy                 | Metodo `relatorio_vendas` no arquivo `models.py` monta a entidade relatorio                                               |
| MEDIUM     | Feature Envy                 | Metodo `get_db` no arquivo `database.py` monta todas as entidades                                                         |
| MEDIUM     | Feature Envy                 | Metodo `criar_produto` no arquivo `controllers.py` monta a entidade produto e categorias_validas                          |
| MEDIUM     | Feature Envy                 | Metodo `atualizar_produto` no arquivo `controllers.py` monta a entidade produto                                           |
| MEDIUM     | Long Method                  | Metodo `criar_pedido` no arquivo `models.py` excede 15 linhas                                                             |
| MEDIUM     | Long Method                  | Metodo `get_pedidos_usuario` no arquivo `models.py` excede 15 linhas                                                      |
| MEDIUM     | Long Method                  | Metodo `get_todos_pedidos` no arquivo `models.py` excede 15 linhas                                                        |
| MEDIUM     | Long Method                  | Metodo `relatorio_vendas` no arquivo `models.py` excede 15 linhas                                                         |
| MEDIUM     | Long Method                  | Metodo `buscar_produtos` no arquivo `models.py` excede 15 linhas                                                          |
| MEDIUM     | Long Method                  | Metodo `get_db` no arquivo `database.py` excede 15 linhas                                                                 |
| MEDIUM     | Long Method                  | Metodo `criar_produto` no arquivo `controllers.py` excede 15 linhas                                                       |
| MEDIUM     | Long Method                  | Metodo `atualizar_produto` no arquivo `controllers.py` excede 15 linhas                                                   |
| MEDIUM     | Long Method                  | Metodo `criar_pedido` no arquivo `controllers.py` excede 15 linhas                                                        |
| MEDIUM     | Long Method                  | Metodo `health_check` no arquivo `controllers.py` excede 15 linhas                                                        |
| MEDIUM     | Long Method                  | Metodo `executar_query` no arquivo `app.py` excede 15 linhas                                                              |
| LOW        | Magic Numbers                | Metodo `relatorio_vendas` no arquivo `models.py`                                                                          |
| LOW        | Magic Numbers                | Metodo `listar_produtos` no arquivo `controllers.py`                                                                      |
| LOW        | Magic Numbers                | Metodo `buscar_produto` no arquivo `controllers.py`                                                                       |
| LOW        | Magic Numbers                | Metodo `criar_produto` no arquivo `controllers.py`                                                                        |
| LOW        | Magic Numbers                | Metodo `atualizar_produto` no arquivo `controllers.py`                                                                    |
| LOW        | Magic Numbers                | Metodo `deletar_produto` no arquivo `controllers.py`                                                                      |
| LOW        | Magic Numbers                | Metodo `buscar_produtos` no arquivo `controllers.py`                                                                      |
| LOW        | Magic Numbers                | Metodo `listar_usuarios` no arquivo `controllers.py`                                                                      |
| LOW        | Magic Numbers                | Metodo `buscar_usuario` no arquivo `controllers.py`                                                                       |
| LOW        | Magic Numbers                | Metodo `criar_usuario` no arquivo `controllers.py`                                                                        |
| LOW        | Magic Numbers                | Metodo `login` no arquivo `controllers.py`                                                                                |
| LOW        | Magic Numbers                | Metodo `criar_pedido` no arquivo `controllers.py`                                                                         |
| LOW        | Magic Numbers                | Metodo `listar_pedidos_usuario` no arquivo `controllers.py`                                                               |
| LOW        | Magic Numbers                | Metodo `listar_todos_pedidos` no arquivo `controllers.py`                                                                 |
| LOW        | Magic Numbers                | Metodo `atualizar_status_pedido` no arquivo `controllers.py`                                                              |
| LOW        | Magic Numbers                | Metodo `relatorio_vendas` no arquivo `controllers.py`                                                                     |
| LOW        | Magic Numbers                | Metodo `health_check` no arquivo `controllers.py`                                                                         |
| LOW        | Magic Numbers                | Metodo `reset_database` no arquivo `app.py`                                                                               |
| LOW        | Magic Numbers                | Metodo `executar_query` no arquivo `app.py`                                                                               |

### Projeto [ecommerce-api-legacy](./ecommerce-api-legacy)
| Linguagem | Framework    | Domínio           | Número de arquivos |
| --------- |--------------|-------------------|--------------------|
| Javascript| Node/Express | API de E-commerce | 3                  |

#### Problemas identificados:
| Severidade | Falha                        | Justificativa                                                                                                         |
|------------|------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| CRITICAL   | Credenciais Hardcoded        | Senha `senha_super_secreta_prod_123` exposta em `utils.js`                                                            |
| CRITICAL   | Credenciais Hardcoded        | Senha `pk_live_1234567890abcdef` exposta em `utils.js`                                                                |
| CRITICAL   | Weak Crypto                  | Metodo `badCrypto` exposto em `utils.js`                                                                              |
| CRITICAL   | SQL Injection                | Metodo `setupRoutes` exposto em `AppManager.js`                                                                       |
| CRITICAL   | God Class                    | Arquivo `AppManager.js` faz criacao de tabelas, manipulacao de usuario, curso, matricula, pagamento, log de auditoria |
| CRITICAL   | Logging Sensitive Data       | Metodo  `setupRoutes` exposto em `AppManager.js`                                                                      |
| HIGH       | Business Logic in Controller | Metodo `setupRoutes` expoe regra em `AppManager.js`                                                                   |
| HIGH       | Tight Coupling Without DI    | Arquivo `AppManager.js` cria conexao com banco                                                                        |
| HIGH       | Global Mutable State         | Arquivo `utils.js` define `config`, `globalCache` e `totalRevenue` globalmente                                        |
| MEDIUM     | Feature Envy                 | Metodo `setupRoutes` no arquivo `AppManager.js` faz tudo com todas as entidades                                       |
| MEDIUM     | Long Method                  | Metodo `setupRoutes` no arquivo `AppManager.js` excede 15 linhas                                                      |
| LOW        | Magic Numbers                | Metodo `relatorio_vendas` no arquivo `AppManager.js`                                                                  |

### Projeto [task-manager-api](./task-manager-api)
| Linguagem | Framework | Domínio        | Número de arquivos |
|-----------|-----------|----------------|--------------------|
| Python    | Flask     | API de Tarefas | 15                 |

#### Problemas identificados:
| Severidade | Falha                        | Justificativa                                                                                                                                                                  |
|------------|------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CRITICAL   | Credenciais Hardcoded        | Senha  `12341234` exposta em `seed.py`                                                                                                                                         |
| CRITICAL   | Credenciais Hardcoded        | Senha  `abcd` exposta em `seed.py`                                                                                                                                             |
| CRITICAL   | Credenciais Hardcoded        | Senha  `pass` exposta em `seed.py`                                                                                                                                             |
| CRITICAL   | Weak Crypto                  | Metodo `set_password` exposto em `user.py`                                                                                                                                     |
| CRITICAL   | God Class                    | Arquivo `task.py` faz manipulacao de tabelas, validacao de dados, validacao de status, prioridade, atraso                                                                      |
| CRITICAL   | God Class                    | Arquivo `user.py` faz manipulacao de tabelas, criptografia e validacao de admin                                                                                                |
| CRITICAL   | God Class                    | Arquivo `report_route.py` faz definicao de rotas, geracao de relatorios, CRUD de categorias                                                                                    |
| CRITICAL   | God Class                    | Arquivo `task_route.py` faz definicao de rotas, CRUD de tarefas                                                                                                                |
| CRITICAL   | God Class                    | Arquivo `user_route.py` faz definicao de rotas, CRUD de usuarios, lista tarefas de usuario, faz login                                                                          |
| CRITICAL   | God Class                    | Arquivo `notification_service.py` envia email,gera notificacoes                                                                                                                |
| CRITICAL   | God Class                    | Arquivo `helpers.py` define constantes, gera id, realiza calculos e validacoes                                                                                                 |
| CRITICAL   | God Class                    | Arquivo `seed.py` cria todas as entidades, acessa banco de dados                                                                                                               |
| HIGH       | Business Logic in Controller | Metodo `summary_report` expoe regra em `report_routes.py`                                                                                                                      |
| HIGH       | Business Logic in Controller | Metodo `user_recreate_categoryport` expoe regra em `report_routes.py`                                                                                                          |
| HIGH       | Business Logic in Controller | Metodo `update_category` expoe regra em `report_routes.py`                                                                                                                     |
| HIGH       | Business Logic in Controller | Metodo `get_tasks` expoe regra em `task_routes.py`                                                                                                                             |
| HIGH       | Business Logic in Controller | Metodo `get_task` expoe regra em `task_routes.py`                                                                                                                              |
| HIGH       | Business Logic in Controller | Metodo `create_task` expoe regra em `task_routes.py`                                                                                                                           |
| HIGH       | Business Logic in Controller | Metodo `update_task` expoe regra em `task_routes.py`                                                                                                                           |
| HIGH       | Business Logic in Controller | Metodo `task_stats` expoe regra em `task_routes.py`                                                                                                                            |
| HIGH       | Business Logic in Controller | Metodo `create_user` expoe regra em `user_routes.py`                                                                                                                           |
| HIGH       | Business Logic in Controller | Metodo `update_user` expoe regra em `user_routes.py`                                                                                                                           |
| HIGH       | Business Logic in Controller | Metodo `get_user_tasks` expoe regra em `user_routes.py`                                                                                                                        |
| HIGH       | Business Logic in Controller | Metodo `login` expoe regra em `user_routes.py`                                                                                                                                 |
| HIGH       | Tight Coupling Without DI    | Arquivo `report_routes.py` manipula sessao com banco                                                                                                                           |
| HIGH       | Tight Coupling Without DI    | Arquivo `task_routes.py` manipula sessao com banco                                                                                                                             |
| HIGH       | Tight Coupling Without DI    | Arquivo `user_routes.py` manipula sessao com banco                                                                                                                             |
| HIGH       | Global Mutable State         | Arquivo `helpers.py` define `VALID_STATUSES`, `VALID_ROLES`, `MAX_TITLE_LENGTH` , `MIN_TITLE_LENGTH`, `MIN_PASSWORD_LENGTH`, `DEFAULT_PRIORITY`, e `DEFAULT_COLOR` globalmente |
| MEDIUM     | Feature Envy                 | Metodo `summary_report` no arquivo `report_routes.py` manipula todas as entidades                                                                                              |
| MEDIUM     | Feature Envy                 | Metodo `get_tasks` no arquivo `tasks_routes.py` manipula todas as entidades                                                                                                    |
| MEDIUM     | Long Method                  | Metodo `create_user` no arquivo `users_routes.py` excede 15 linhas                                                                                                             |
| MEDIUM     | Long Method                  | Metodo `update_user` no arquivo `users_routes.py` excede 15 linhas                                                                                                             |
| LOW        | Magic Numbers                | Metodo `delete_user` no arquivo `users_routes.py`                                                                                                                              |

## Construção da Skill

A Skill `refactor-arch` foi construída para automatizar uma auditoria arquitetural 
baseada em evidências e, após confirmação humana, refatorar projetos legados para 
uma estrutura MVC. A ferramenta escolhida foi o **Claude Code**, usando a 
estrutura de Custom Skills em `.claude/skills/refactor-arch/`.

A Skill foi dividida em três fases sequenciais:

1. **PHASE 1 - Project Analysis**  
   Responsável por detectar a stack do projeto, linguagem, framework, dependências, 
   banco de dados, entry point, domínio da aplicação e arquitetura atual.

2. **PHASE 2 - MVC + SOLID Architecture Audit**  
   Responsável por auditar o código de forma read-only, identificar anti-patterns, 
   classificar severidade, apontar arquivo e linha, explicar impacto e recomendar 
   uma transformação.

3. **PHASE 3 - Refactoring**  
   Executada somente após confirmação explícita do operador. Essa fase reorganiza 
   o projeto para MVC, corrige os problemas priorizados, preserva os endpoints 
   originais quando possível e valida o funcionamento da aplicação.

A separação em fases foi uma decisão importante para reduzir risco. As Fases 1 e 
2 são exclusivamente de leitura, evitando modificações antes da revisão humana. 
A Fase 3 só pode ser executada depois da pergunta obrigatória:

```text
Phase 2 complete. Proceed with refactoring (Phase 3)? [y/n]
```

Essa pausa garante que a auditoria seja revisada antes de qualquer alteração no 
código.

### Decisões de design

A Skill foi projetada com foco em cinco decisões principais.

#### 1. Auditoria baseada em evidências

A Skill não deve declarar problemas de forma genérica. Todo finding precisa estar 
conectado a uma evidência concreta, como arquivo, linha, função, dependência, 
configuração ou warning presente no projeto. Isso evita falsos positivos e 
torna o relatório verificável.

Cada finding segue o formato:

```text
[SEVERITY] Nome do anti-pattern
File: caminho:linha-inicial-linha-final
Description: descrição do problema
Impact: impacto técnico
Recommendation: correção recomendada
```

#### 2. Separação entre prompt principal e conhecimento de referência

O `SKILL.md` define o comportamento da Skill, o fluxo das fases, os guardrails e 
o formato obrigatório de saída. Os arquivos em `references/` concentram o 
conhecimento especializado:

```text
references/
├── project-analysis-heuristics.md
├── anti-pattern-catalog.md
├── phase-2-report-template.md
├── mvc-architecture-guidelines.md
└── refactoring-playbook.md
```

Essa separação facilita manutenção: o comportamento geral fica no `SKILL.md`, 
enquanto regras de arquitetura, anti-patterns e padrões de refatoração ficam em 
arquivos próprios.

#### 3. Refatoração orientada pelos achados da auditoria

A Fase 3 não refatora de forma livre. Ela deve usar os findings da Fase 2 como 
plano de ação. Cada mudança aplicada precisa estar ligada a um problema 
identificado anteriormente.

Isso evita refatorações cosméticas ou alterações sem justificativa técnica.

#### 4. Preservação de comportamento externo

A Skill prioriza manter rotas, métodos HTTP, status codes e contratos de 
request/response. Exceções são permitidas apenas quando o próprio contrato 
representa uma vulnerabilidade crítica, como um endpoint que executa SQL 
arbitrário enviado pelo usuário.

Nesse caso, a segurança tem precedência sobre a preservação da rota.

#### 5. Validação obrigatória após a refatoração

A Skill exige validação real depois da Fase 3:

- instalação de dependências;
- boot da aplicação;
- testes de endpoints com `curl`, `Invoke-WebRequest` ou equivalente;
- verificação dos anti-patterns críticos e altos corrigidos;
- execução de testes existentes quando disponíveis.

A Skill só pode marcar validações com `✓` quando os comandos forem realmente 
executados com sucesso.

### Anti-patterns incluídos e justificativa

O catálogo de anti-patterns foi criado para cobrir problemas de arquitetura, 
segurança, manutenibilidade, testabilidade e performance. Ele não é uma lista 
fechada, mas funciona como baseline mínimo para os três projetos.

| Anti-pattern                              | Severidade padrão | Motivo da inclusão                                                                                        |
|-------------------------------------------|------------------:|-----------------------------------------------------------------------------------------------------------|
| Hardcoded Credentials or Secrets          |          CRITICAL | Segredos no código expõem credenciais e dificultam rotação segura.                                        |
| SQL Injection                             |          CRITICAL | Permite leitura, alteração ou destruição de dados por input malicioso.                                    |
| Arbitrary SQL Execution                   |          CRITICAL | Endpoints que executam SQL enviado pelo usuário são vulneráveis por design.                               |
| Weak Password Hashing                     |          CRITICAL | Senhas em plaintext ou hash fraco comprometem contas em caso de vazamento.                                |
| Broken Access Control                     |     HIGH/CRITICAL | Endpoints administrativos sem autorização permitem ações destrutivas.                                     |
| Sensitive Data Exposure                   |              HIGH | Responses não devem expor senhas, tokens, secrets ou dados internos.                                      |
| Direct Database Access in Controller/View |              HIGH | Viola MVC e acopla apresentação diretamente à persistência.                                               |
| Fat Controller                            |              HIGH | Controllers com validação, regra de negócio, persistência e formatação ficam difíceis de testar e manter. |
| God Class / God Method                    |              HIGH | Arquivos ou funções com muitas responsabilidades aumentam risco de mudança.                               |
| Framework Leakage into Domain             |              HIGH | Domínio dependente de framework reduz portabilidade e testabilidade.                                      |
| Circular Dependencies                     |              HIGH | Dependências circulares indicam boundaries mal definidos.                                                 |
| N+1 Query                                 |              HIGH | Causa degradação de performance proporcional ao volume de dados.                                          |
| Dependency Hygiene Violation              |              HIGH | Dependências ausentes ou desnecessárias afetam deploy, segurança e manutenção.                            |
| Missing Validation Boundaries             |            MEDIUM | Input não validado aumenta risco de erro, inconsistência e exploração.                                    |
| Poor Error Handling                       |            MEDIUM | Expor `str(e)` ou stack traces revela detalhes internos.                                                  |
| Anemic Domain Model                       |            MEDIUM | Regras espalhadas fora do domínio enfraquecem encapsulamento.                                             |
| Business Logic in View/Serializer         |            MEDIUM | Serialização não deve conter regra de negócio.                                                            |
| Hidden Global State                       |            MEDIUM | Estado global dificulta testes, concorrência e previsibilidade.                                           |
| Deprecated API Usage                      |            MEDIUM | APIs deprecated podem bloquear upgrades e gerar riscos futuros.                                           |
| Naming or Organization Drift              |               LOW | Nomes ruins e organização inconsistente prejudicam leitura e onboarding.                                  |
| Excessive Static Helpers                  |               LOW | Helpers genéricos demais reduzem coesão e testabilidade.                                                  |

A escolha desses anti-patterns foi guiada pelos problemas encontrados nos três 
projetos e por referências técnicas em sites especializados: mistura de 
responsabilidades, SQL inseguro, endpoints administrativos sem proteção, 
exposição de dados sensíveis, ausência de separação MVC, validação espalhada, 
error handling inconsistente e uso de estrutura plana.

### Como a Skill foi construída para ser agnóstica de tecnologia

Para garantir que a Skill funcione em projetos diferentes, ela não assume 
previamente linguagem, framework, banco de dados ou estrutura de pastas.

A Fase 1 usa heurísticas baseadas em evidências, como:

- manifestos de dependência: `requirements.txt`, `package.json`, `pyproject.toml`, 
  `pom.xml`, `build.gradle`, `composer.json`;
- extensões de arquivos: `.py`, `.js`, `.ts`, `.java`, `.php`, `.rb`;
- imports e decorators de framework: `from flask import Flask`, `app.route`, 
  `express()`, `router.get`;
- scripts de execução: `python app.py`, `npm start`, `node src/app.js`;
- sinais de banco de dados: queries SQL, ORMs, connection strings, migrations e 
  arquivos `.db`;
- rotas e handlers HTTP.

A Skill também evita julgar arquitetura apenas pelo nome dos diretórios. Um 
arquivo chamado `models.py`, por exemplo, não é considerado automaticamente uma 
camada Model válida. A avaliação observa a responsabilidade real do código. Se 
`models.py` contém SQL, validação, regra de negócio e serialização, ele é tratado 
como uma violação de separação de responsabilidades.

Durante a refatoração, a Skill adapta os padrões ao framework detectado:

- em Flask, usa `src/app.py`, controllers, services, repositories e `flask.g` 
  para conexão por request;
- em Express, usa `src/app.js`, routers/controllers, services, repositories e 
  middleware de erro;
- em outros frameworks, o mesmo princípio deve ser aplicado com sintaxe e 
  convenções nativas da stack.

Os exemplos do playbook são escritos principalmente em Python, mas são tratados 
como exemplos conceituais. O agente deve adaptar a implementação para a linguagem 
detectada.

### Como a Skill aplica MVC

A arquitetura alvo é MVC-aligned, com separação clara entre camadas:

```text
src/
├── app.*
├── config/
├── infrastructure/
├── models/
├── repositories/
├── services/
├── controllers/
├── views/
└── middlewares/
```

A responsabilidade esperada de cada camada é:

- **Models:** representam entidades e regras básicas de domínio.
- **Repositories:** isolam persistência, SQL, ORM ou acesso a dados.
- **Services:** concentram regras de negócio e orquestração de casos de uso.
- **Controllers:** recebem input HTTP, delegam para services e retornam response.
- **Views/Routes:** registram rotas e fazem mapeamento de apresentação.
- **Infrastructure:** contém banco de dados, schema, seed e integrações técnicas.
- **Config:** centraliza variáveis de ambiente e configuração.
- **Middlewares:** centralizam tratamento de erro e comportamento transversal.

Essa estrutura foi usada nos três projetos, respeitando a stack de cada um.

### Desafios encontrados

O primeiro desafio foi equilibrar uma Skill genérica com refatorações concretas. 
Uma Skill muito genérica encontra problemas, mas não consegue corrigir com precisão. 
Uma Skill muito específica funciona em apenas um projeto. Para resolver isso, a 
Skill foi dividida entre heurísticas agnósticas e padrões de refatoração 
adaptáveis por stack.

O segundo desafio foi preservar comportamento externo sem preservar 
vulnerabilidades. Alguns endpoints podiam ser mantidos com autenticação ou 
validação, mas outros eram vulneráveis por design, como endpoints que executavam 
SQL arbitrário recebido no body. Nesses casos, a Skill foi instruída a remover 
ou substituir a rota por operação controlada.

O terceiro desafio foi validar a refatoração de forma objetiva. Por isso, a Skill 
exige evidências de boot, chamadas HTTP e verificações por busca textual dos 
padrões removidos. Isso reduz o risco de declarar sucesso sem comprovação.

O quarto desafio foi lidar com diferenças entre os projetos. Dois projetos usam 
Python/Flask, mas com níveis diferentes de organização, enquanto o terceiro usa 
Node.js/Express. Para manter a Skill agnóstica, a análise passou a depender de 
evidências no código e nos manifestos, e não de nomes de pastas ou suposições.

O quinto desafio foi evitar falsos positivos. A Skill foi instruída a diferenciar 
violação comprovada de risco provável. Por exemplo, uma API só deve ser marcada 
como deprecated se houver evidência concreta no código, dependências, comentários, 
warnings ou documentação do projeto.

### Resultado da construção

A Skill final entrega:

- análise inicial da stack e arquitetura;
- relatório de auditoria com findings classificados por severidade;
- pausa obrigatória para confirmação humana;
- refatoração para estrutura MVC;
- extração de configuração e remoção de secrets hardcoded;
- separação de controllers, services, models, repositories, views e infrastructure;
- centralização de error handling;
- validação de boot e endpoints;
- relatório final salvo em `reports/`.

Essa abordagem tornou a Skill reutilizável nos três projetos fornecidos e reduziu 
o acoplamento a uma tecnologia específica.

## Resultados

Esta seção apresenta o resultado da execução da Skill `refactor-arch` nos três 
projetos legados fornecidos no desafio. A execução seguiu o fluxo definido na Skill:

1. **PHASE 1 - Project Analysis**
2. **PHASE 2 - MVC + SOLID Architecture Audit**
3. **PHASE 3 - Refactoring**

A Fase 1 detectou a stack e a arquitetura de cada projeto. A Fase 2 gerou os 
relatórios de auditoria com os problemas classificados por severidade. A Fase 3 
foi executada após confirmação e aplicou a refatoração para uma estrutura MVC, 
seguida de validação de boot, endpoints e checagens contra os anti-patterns 
corrigidos.

Os relatórios completos foram salvos em:

```text
reports/audit-project-1.md
reports/audit-project-2.md
reports/audit-project-3.md
```

### Resumo dos relatórios de auditoria
| Projeto                | Stack detectada   |                    Relatório | CRITICAL | HIGH | MEDIUM | LOW | Total |
|------------------------|-------------------|-----------------------------:|---------:|-----:|-------:|----:|------:|
| `code-smells-project`  | Python + Flask    | `reports/audit-project-1.md` |        4 |    5 |      6 |   2 |    17 |
| `ecommerce-api-legacy` | Node.js + Express | `reports/audit-project-2.md` |        2 |    6 |      4 |   2 |    14 |
| `task-manager-api`     | Python + Flask    | `reports/audit-project-3.md` |        3 |    6 |      6 |   2 |    17 |

Todos os projetos atingiram os critérios mínimos exigidos:

- Fase 1 detectou a stack corretamente.
- Fase 2 encontrou pelo menos 5 findings por projeto.
- Fase 2 encontrou pelo menos 1 finding CRITICAL ou HIGH por projeto.
- Fase 3 aplicou refatoração para uma estrutura MVC.
- As aplicações foram validadas após a refatoração.

### Resultado por projeto

#### Projeto 1 - `code-smells-project`

O projeto inicial era uma API Flask de e-commerce organizada em arquivos planos 
na raiz do projeto. A auditoria identificou problemas graves de segurança, 
arquitetura e manutenção.

Principais problemas encontrados:

- SQL Injection em múltiplas queries.
- Endpoint `/admin/query` executando SQL arbitrário enviado pelo usuário.
- Senhas armazenadas e comparadas em plaintext.
- `SECRET_KEY` hardcoded e exposto no endpoint `/health`.
- Endpoints administrativos sem controle de acesso.
- Exposição de dados sensíveis em responses.
- N+1 queries em listagem de pedidos.
- Controllers e arquivos de acesso a dados com múltiplas responsabilidades.

Principais mudanças aplicadas:

- Queries migradas para repositories com parameterized queries.
- Endpoint `/admin/query` removido.
- `/admin/reset-db` protegido por token administrativo.
- Senhas migradas para `werkzeug.security.generate_password_hash` e `check_password_hash`.
- Configurações sensíveis extraídas para variáveis de ambiente.
- Dados sensíveis removidos das responses.
- Código reorganizado em `src/` com camadas MVC.
- Error handling centralizado.
- Services criados para regras de negócio.

Resumo da auditoria:

```text
CRITICAL: 4 | HIGH: 5 | MEDIUM: 6 | LOW: 2
Total: 17 findings
```

##### Comparação Antes/Depois

**Antes**
```
code-smells-project/
├── app.py          ← rotas, lógica de negócio, configuração
├── controllers.py  ← handlers HTTP + SQL direto + validação
├── models.py       ← queries SQL concatenadas (sem classes)
├── database.py     ← conexão + schema + seed + estado global
└── requirements.txt
```

**Depois**
```
code-smells-project/
├── app.py                     ← wrapper de compatibilidade
├── requirements.txt
├── .env.example
├── .gitignore
└── src/
    ├── app.py                 ← entry point real
    ├── config/
    │   └── settings.py        ← SECRET_KEY, DATABASE_PATH via env
    ├── infrastructure/
    │   ├── database.py        ← conexão por request via flask.g + schema
    │   └── seed.py            ← seed com senhas hasheadas
    ├── models/
    │   ├── produto_model.py   ← classe Produto com CATEGORIAS_VALIDAS
    │   ├── usuario_model.py   ← classe Usuario; to_dict() sem senha
    │   └── pedido_model.py    ← classe Pedido com STATUS_VALIDOS
    ├── repositories/
    │   ├── produto_repository.py   ← queries parametrizadas
    │   ├── usuario_repository.py   ← queries parametrizadas
    │   └── pedido_repository.py    ← JOIN elimina N+1
    ├── services/
    │   ├── pedido_service.py       ← orquestração de pedido
    │   └── relatorio_service.py    ← lógica de desconto
    ├── controllers/
    │   ├── produto_controller.py   ← handlers de produto com ValidationError
    │   ├── usuario_controller.py   ← handlers de usuário com AuthenticationError
    │   └── pedido_controller.py    ← handlers de pedido e relatório; reset-db com auth
    ├── views/
    │   └── routes.py               ← registro de rotas + /health + /admin/reset-db
    └── middlewares/
        └── error_handler.py        ← handlers centralizados por tipo de exceção
```


#### Projeto 2 - `ecommerce-api-legacy`

O projeto inicial era uma API Node.js/Express com fluxo de checkout, mas 
concentrava responsabilidades em módulos grandes e pouco coesos. A auditoria 
encontrou problemas de segurança, acoplamento e organização arquitetural.

Principais problemas encontrados:

- Lógica de checkout concentrada em módulos com responsabilidades misturadas.
- Acesso direto a dados fora de camada apropriada.
- Regras de negócio duplicadas ou espalhadas.
- Ausência de separação clara entre controllers, services e repositories.
- Fragilidades em validação de entrada.
- Tratamento de erro inconsistente.
- Problemas de organização e naming.
- Riscos de segurança relacionados a fluxo de autenticação e dados sensíveis.

Principais mudanças aplicadas:

- Separação em `controllers/`, `services/`, `repositories/`, `models/`, `views/`,
  `middlewares/`, `config/` e `infrastructure/`.
- Fluxo de checkout movido para service dedicado.
- Persistência isolada em repositories.
- Rotas centralizadas em camada de views/routes.
- Error handling centralizado via middleware.
- Configurações movidas para camada de config.
- Validações e regras de negócio extraídas dos handlers HTTP.
- Estrutura final alinhada ao padrão MVC.

Resumo da auditoria:

```text
CRITICAL: 2 | HIGH: 6 | MEDIUM: 4 | LOW: 2
Total: 14 findings
```

##### Comparação Antes/Depois

**Antes**
```
ecommerce-api-legacy/src/
├── app.js          ← instancia AppManager e inicia servidor
├── AppManager.js   ← DB + schema + seed + todas as rotas + toda lógica
└── utils.js        ← config hardcoded + badCrypto + globalCache
```

**Depois**
```
ecommerce-api-legacy/
├── .env.example
├── .gitignore
├── api.http
├── package.json
├── package-lock.json
└── src/
    ├── app.js                      ← entry point com async initDb
    ├── config/
    │   └── settings.js             ← configuração via process.env
    ├── infrastructure/
    │   └── database.js             ← DB init, schema, seed com scrypt
    ├── models/
    │   ├── user.js                 ← toDict() sem campo pass
    │   ├── course.js               ← isActive()
    │   ├── enrollment.js
    │   └── payment.js              ← isApproved() e approve()
    ├── repositories/
    │   ├── userRepository.js       ← findByEmail, create, deleteById
    │   ├── courseRepository.js     ← findActiveById
    │   ├── enrollmentRepository.js
    │   ├── paymentRepository.js
    │   ├── auditRepository.js
    │   └── financialRepository.js  ← JOIN único elimina N+1
    ├── services/
    │   ├── checkoutService.js      ← orquestração + scryptSync
    │   └── financialService.js     ← agregação do relatório
    ├── controllers/
    │   ├── checkoutController.js
    │   ├── financialController.js
    │   └── userController.js
    ├── views/
    │   └── routes.js               ← rotas com middleware de auth
    └── middlewares/
        ├── auth.js                 ← Bearer token via ADMIN_TOKEN
        └── errorHandler.js         ← tratamento centralizado
```

#### Projeto 3 - `task-manager-api`

O projeto inicial era uma API Flask de gerenciamento de tarefas parcialmente 
organizada, mas ainda possuía problemas de separação de responsabilidades, 
segurança, validação e acoplamento.

Principais problemas encontrados:

- Configurações sensíveis ou frágeis.
- Regras de negócio espalhadas entre rotas, services e utilitários.
- Boundaries inconsistentes entre camadas.
- Validações ausentes ou incompletas.
- Error handling não centralizado de forma suficiente.
- Problemas de organização e naming.
- Riscos de acoplamento entre infraestrutura e lógica de aplicação.
- Necessidade de melhorar a estrutura MVC já existente.

Principais mudanças aplicadas:

- Estrutura reorganizada e padronizada dentro de `src/`.
- Configurações movidas para `src/config/`.
- Persistência e setup técnico isolados em `src/infrastructure/`.
- Controllers reduzidos para receber input HTTP e delegar.
- Services concentrando regras de negócio.
- Models representando entidades do domínio.
- Repositories isolando acesso a dados.
- Error handling centralizado.
- Validação funcional executada após a refatoração.

Resumo da auditoria:

```text
CRITICAL: 3 | HIGH: 6 | MEDIUM: 6 | LOW: 2
Total: 17 findings
```

##### Comparação Antes/Depois

**Antes**
```
task-manager-api/
├── app.py                   ← SECRET_KEY hardcoded; sem load_dotenv
├── database.py
├── seed.py
├── requirements.txt         ← marshmallow e requests não utilizados
├── models/
│   ├── user.py              ← MD5 sem salt; password em to_dict()
│   ├── task.py              ← lazy default (causa N+1)
│   └── category.py
├── routes/
│   ├── user_routes.py       ← Fat controller; fake-jwt; sem auth
│   ├── task_routes.py       ← N+1 em loop; bare except
│   └── report_routes.py     ← categorias misturadas; lógica inline
├── services/
│   └── notification_service.py  ← credenciais SMTP hardcoded
└── utils/helpers.py         ← 9 funções, maioria sem uso
```

**Depois**
```
task-manager-api/
├── app.py                   ← wrapper de compatibilidade
├── requirements.txt         ← apenas 3 pacotes utilizados
├── .env.example
├── .gitignore
└── src/
    ├── app.py               ← create_app() com application factory
    ├── config/settings.py   ← SECRET_KEY, DATABASE_URL, EMAIL_* via env
    ├── infrastructure/
    │   ├── database.py      ← SQLAlchemy instance + init_db()
    │   └── seed.py          ← carga inicial
    ├── models/
    │   ├── user.py          ← werkzeug hashing; to_dict() sem password
    │   ├── task.py          ← lazy='joined'; is_overdue() canônico
    │   └── category.py
    ├── repositories/
    │   ├── user_repository.py      ← db.session.get() + selectinload()
    │   ├── task_repository.py      ← db.session.get(); count_by_status
    │   └── category_repository.py
    ├── services/
    │   ├── user_service.py         ← auth + token HMAC-SHA256
    │   ├── task_service.py         ← CRUD + validação
    │   ├── report_service.py       ← métricas de produtividade
    │   ├── notification_service.py ← credenciais via settings
    │   └── category_service.py     ← CRUD de categorias
    ├── middlewares/
    │   ├── auth.py                 ← HMAC-SHA256 verify + decorator
    │   └── error_handler.py        ← 404/405/500 centralizado
    ├── utils/
    │   ├── validators.py           ← validate_email(), is_valid_color()
    │   └── date_utils.py           ← parse_date()
    └── views/
        ├── task_routes.py          ← require_auth em POST/PUT/DELETE
        ├── user_routes.py          ← require_auth em PUT/DELETE
        ├── category_routes.py      ← require_auth em POST/PUT/DELETE
        └── report_routes.py
```

### Checklist de Validação

#### Projeto 1 - code-smells-project

**Fase 1 - Análise**
- [x] Linguagem detectada corretamente - Python
- [x] Framework detectado corretamente - Flask 3.1.1
- [x] Domínio da aplicação descrito corretamente - E-commerce (produtos, usuários, pedidos)
- [x] Número de arquivos analisados condiz com a realidade - 5 files analyzed

**Fase 2 - Auditoria**
- [x] Relatório segue o template definido nos arquivos de referência
- [x] Cada finding tem arquivo e linhas exatos
- [x] Findings ordenados por severidade (CRITICAL → LOW)
- [x] Mínimo de 5 findings identificados - 17 encontrados
- [x] Detecção de APIs deprecated incluída (não aplicável - sqlite3 nativo sem versão legada)
- [x] Skill pausou e pediu confirmação antes da Fase 3

**Fase 3 - Refatoração**
- [x] Estrutura de diretórios segue padrão MVC
- [x] Configuração extraída para módulo de config - `src/config/settings.py` via env
- [x] Models criados para abstrair dados - `Produto`, `Usuario`, `Pedido` com `to_dict()`
- [x] Views/Routes separadas - `src/views/routes.py`
- [x] Controllers concentram o fluxo da aplicação - 5 controllers thin
- [x] Error handling centralizado - `src/middlewares/error_handler.py`
- [x] Entry point claro - `app.py` (wrapper) → `src/app.py`
- [x] Aplicação inicia sem erros
- [x] Endpoints originais respondem corretamente

#### Projeto 2 - ecommerce-api-legacy (Node.js/Express)

**Fase 1 - Análise**
- [x] Linguagem detectada corretamente - JavaScript (Node.js)
- [x] Framework detectado corretamente - Express 4.18.2
- [x] Domínio da aplicação descrito corretamente - LMS com checkout, matrículas, cursos e pagamentos
- [x] Número de arquivos analisados condiz com a realidade - 6 files analyzed

**Fase 2 - Auditoria**
- [x] Relatório segue o template definido nos arquivos de referência
- [x] Cada finding tem arquivo e linhas exatos
- [x] Findings ordenados por severidade (CRITICAL → LOW)
- [x] Mínimo de 5 findings identificados - 14 encontrados
- [x] Detecção de APIs deprecated incluída (não aplicável - Express 4 sem uso de APIs legadas)
- [x] Skill pausou e pediu confirmação antes da Fase 3

**Fase 3 - Refatoração**
- [x] Estrutura de diretórios segue padrão MVC
- [x] Configuração extraída para módulo de config - `src/config/settings.js` via `process.env`
- [x] Models criados para abstrair dados - `User`, `Course`, `Enrollment`, `Payment`
- [x] Views/Routes separadas - `src/views/routes.js`
- [x] Controllers concentram o fluxo da aplicação - 3 controllers thin
- [x] Error handling centralizado - `src/middlewares/error_handler.js`
- [x] Entry point claro - `src/app.js`
- [x] Aplicação inicia sem erros
- [x] Endpoints originais respondem corretamente

#### Projeto 3 - task-manager-api (Python/Flask)

**Fase 1 - Análise**
- [x] Linguagem detectada corretamente - Python
- [x] Framework detectado corretamente - Flask 3.0.0
- [x] Domínio da aplicação descrito corretamente - Gerenciamento de tarefas com usuários, categorias e relatórios
- [x] Número de arquivos analisados condiz com a realidade - 17 files analyzed

**Fase 2 - Auditoria**
- [x] Relatório segue o template definido nos arquivos de referência
- [x] Cada finding tem arquivo e linhas exatos
- [x] Findings ordenados por severidade (CRITICAL → LOW)
- [x] Mínimo de 5 findings identificados - 16 encontrados
- [x] Detecção de APIs deprecated incluída - `Model.query.get()` (SQLAlchemy legado) detectado em 12+ locais
- [x] Skill pausou e pediu confirmação antes da Fase 3

**Fase 3 - Refatoração**
- [x] Estrutura de diretórios segue padrão MVC
- [x] Configuração extraída para módulo de config - `src/config/settings.py` via env
- [x] Models criados para abstrair dados - `User`, `Task`, `Category` com werkzeug e `lazy='joined'`
- [x] Views/Routes separadas - `src/views/routes.py`
- [x] Controllers concentram o fluxo da aplicação - 4 controllers thin com `require_auth`
- [x] Error handling centralizado - `src/middlewares/error_handler.py`
- [x] Entry point claro - `app.py` (wrapper) → `src/app.py`
- [x] Aplicação inicia sem erros
- [x] Endpoints originais respondem corretamente

### Logs das Aplicações Rodando Após Refatoração

#### Projeto 1 - code-smells-project

**Boot**
```
$ python app.py
INFO:infrastructure.database:Database initialized at C:\...\code-smells-project\loja.db
 * Serving Flask app 'app'
 * Running on http://127.0.0.1:5000
```

**Endpoints**
```
$ curl -s http://localhost:5000/produtos
HTTP 200
{
  "dados": [
    {"ativo":1,"categoria":"informatica","criado_em":"2026-05-14 23:35:27",
     "descricao":"Notebook potente para jogos","estoque":10,
     "id":1,"nome":"Notebook Gamer","preco":5999.99},
    ...
  ],
  "sucesso": true
}

$ curl -s -X POST http://localhost:5000/login \
  -H "Content-Type: application/json" \
  -d '{"email":"admin@loja.com","senha":"admin123"}'
HTTP 200
{
  "dados": {"criado_em":"2026-05-14 23:35:28","email":"admin@loja.com",
            "id":1,"nome":"Admin","tipo":"admin"},
  "mensagem": "Login OK",
  "sucesso": true
}

$ curl -s -X POST http://localhost:5000/admin/reset-db
HTTP 401
{"erro":"Acesso não autorizado"}

$ curl -s -X PUT http://localhost:5000/produtos/1 \
  -H "Content-Type: application/json" \
  -d '{"nome":"Notebook Gamer Pro","preco":6499.99,"estoque":8}'
HTTP 200
{"mensagem":"Produto atualizado","sucesso":true}

$ curl -s -X POST http://localhost:5000/pedidos \
  -H "Content-Type: application/json" \
  -d '{"usuario_id":1,"itens":[{"produto_id":2,"quantidade":2}]}'
HTTP 201
{"dados":{"pedido_id":1,"total":179.8},"mensagem":"Pedido criado com sucesso","sucesso":true}

$ curl -s http://localhost:5000/health
HTTP 200
{"counts":{"pedidos":1,"produtos":10,"usuarios":3},"database":"connected","status":"ok","versao":"1.0.0"}
```

**Anti-pattern checks - 0 ocorrências em todos os padrões críticos**
```
$ grep -RnsE "execute\(f\"SELECT.*\+" src/          → 0 matches
$ grep -RnsE "(md5|sha1|hashlib\.)" src/             → 0 matches
$ grep -RnsE "SECRET_KEY\s*=\s*['\"]" src/           → 0 matches
$ grep -RnsE "^db_connection" src/                   → 0 matches
$ grep -RnsE "cursor\.execute\(query\)" src/          → 0 matches
$ grep -RnsE "jsonify.*str\(e\)" src/ | grep -v error_handler → 0 matches
```

#### Projeto 2 - ecommerce-api-legacy

**Boot**
```
$ ADMIN_TOKEN=test-admin-token node src/app.js
Frankenstein LMS rodando na porta 3000...
```

**Endpoints**
```
$ curl -s -X POST http://localhost:3000/api/checkout \
  -H "Content-Type: application/json" \
  -d '{"usr":"Guilherme","eml":"gui@fullcycle.com.br","c_id":2,"card":"4111222233334444"}'
HTTP 200
{"msg":"Sucesso","enrollment_id":2}

$ curl -s -X POST http://localhost:3000/api/checkout \
  -H "Content-Type: application/json" \
  -d '{"usr":"João","eml":"joao@teste.com","c_id":1,"card":"5111222233334444"}'
HTTP 400
Pagamento recusado

$ curl -s http://localhost:3000/api/admin/financial-report
HTTP 401
{"error":"Unauthorized"}

$ curl -s -H "x-admin-token: test-admin-token" \
  http://localhost:3000/api/admin/financial-report
HTTP 200
[
  {"course":"Clean Architecture","revenue":997,"students":[{"student":"Leonan","paid":997}]},
  {"course":"Docker","revenue":497,"students":[{"student":"Guilherme","paid":497}]}
]

$ curl -s -X DELETE http://localhost:3000/api/users/1
HTTP 401
{"error":"Unauthorized"}

$ curl -s -X DELETE -H "x-admin-token: test-admin-token" \
  http://localhost:3000/api/users/1
HTTP 200
{"msg":"Usuário removido com sucesso"}
```

**Anti-pattern checks - 0 ocorrências em todos os padrões críticos**
```
$ grep -RnsE "(pk_live|senha_super_secreta|admin_master)" src/  → 0 matches
$ grep -RnsE "badCrypto|Buffer\.from.*base64" src/              → 0 matches
$ grep -RnsE "console\.log.*(card|cc|GatewayKey)" src/          → 0 matches
$ grep -RnsE "globalCache|logAndCache|totalRevenue" src/        → 0 matches
```

#### Projeto 3 - task-manager-api

**Boot**
```
$ python app.py
 * Serving Flask app 'app'
 * Running on http://127.0.0.1:5000
```

**Endpoints**
```
$ GET http://127.0.0.1:5000/health
HTTP 200
{"status":"ok","timestamp":"2026-05-15 12:43:56.325208+00:00"}

$ GET http://127.0.0.1:5000/tasks
HTTP 200 - 10 tasks
[
  {"id":1,"title":"Implementar autenticação JWT","user_name":"João Silva",
   "category_name":"Backend","overdue":true,"status":"pending", ...},
  ...
]
- password ausente em todas as responses de usuário

$ GET http://127.0.0.1:5000/users
HTTP 200 - 3 users
[{"id":1,"name":"João Silva","email":"joao@email.com",
  "role":"admin","task_count":4, ...}, ...]
- password ausente em todas as responses

$ POST http://127.0.0.1:5000/login  {"email":"joao@email.com","password":"1234"}
HTTP 200
{"message":"Login realizado com sucesso",
 "token":"1:2b8b2b0ba9b5ead781d8040b3bcacf4445533a...",
 "user":{"id":1,"name":"João Silva","email":"joao@email.com","role":"admin"}}
- token HMAC-SHA256 real; sem fake-jwt

$ PUT http://127.0.0.1:5000/tasks/1  (sem token)
HTTP 401
{"error":"Autenticação necessária"}

$ PUT http://127.0.0.1:5000/tasks/1  (com Bearer token válido)
HTTP 200
{"id":1,"title":"Implementar autenticacao JWT", ...}

$ GET http://127.0.0.1:5000/tasks/stats
HTTP 200
{"cancelled":1,"completion_rate":10.0,"done":1,"in_progress":2,
 "overdue":2,"pending":6,"total":10}

$ GET http://127.0.0.1:5000/reports/summary
HTTP 200
{"overview":{"total_categories":4,"total_tasks":10,"total_users":3}, ...}
```

**Anti-pattern checks - 0 ocorrências em todos os padrões críticos**
```
$ grep -RnsE "hashlib\.md5|\.md5\(" src/                            → 0 matches
$ grep -RnsE "fake-jwt" src/                                         → 0 matches
$ grep -RnsE "'password'.*self\.password" src/                       → 0 matches
$ grep -RnsE "db\.session\.(add|commit|delete|query|execute)" src/services/ → 0 matches
$ grep -RnsE "\.query\.get\(" src/                                   → 0 matches
$ grep -RnsE "^\s+except:\s*$" src/                                  → 0 matches
$ grep -RnsE "(SECRET_KEY|email_password)\s*=\s*['\"][^'\"$]" src/  → 0 matches
```

### Observações sobre Comportamento da Skill em Stacks Diferentes

**Agnoscidade de tecnologia confirmada:** A skill detectou corretamente
Python/Flask (Flask 3.1.1 e 3.0.0) e JavaScript/Express (4.18.2) via análise de 
manifesto de dependências (`requirements.txt` e `package.json`), sem configuração 
prévia ou hints de stack.

**Adaptação ao nível de organização:** No Projeto 1 (monolito em 4 arquivos) a 
Phase 3 criou a estrutura MVC do zero. No Projeto 2 (2 arquivos com classe 
monolítica) separou responsabilidades da `AppManager`. No Projeto 3 (estrutura 
parcial existente com `models/`, `routes/`, `services/`) a skill reconheceu a 
organização prévia, identificou as falhas restantes e fez a migração para `src/` 
sem descartar o trabalho existente.

**Cobertura de segurança:** Em todos os 3 projetos a skill detectou e corrigiu os 
OWASP Top 10 mais relevantes: A01 (Broken Access Control), A02 (Cryptographic 
Failures - hashing fraco), A03 (Injection - SQL Injection no Projeto 1) e A09 
(Security Logging - dados sensíveis em logs).

**Preservação de comportamento:** Todos os endpoints originais continuaram 
respondendo após a refatoração, confirmado via testes manuais com curl/Python em 
todos os projetos.

## Como Executar

Esta seção descreve os pré-requisitos, os comandos para executar a Skill 
`refactor-arch` em cada projeto e os comandos usados para validar que a 
refatoração funcionou corretamente.

### Pré-requisitos

Antes de executar a Skill ou validar os projetos, instale/configure:

| Ferramenta  | Versão mínima | Verificação        |
|-------------|---------------|--------------------|
| Claude Code | 2.x           | `claude --version` |
| Python      | 3.10+         | `python --version` |
| pip         | qualquer      | `pip --version`    |
| Node.js     | 18.x+         | `node --version`   |
| npm         | 8.x+          | `npm --version`    |

### Executar a Skill em Cada Projeto

A skill `refactor-arch` está presente em `.claude/skills/refactor-arch/` dentro 
de cada projeto. O comando de invocação é idêntico nos 3 - o Claude Code localiza 
a skill pelo diretório de trabalho atual.

#### Projeto 1 - code-smells-project

**1. Preparar o ambiente**
```bash
cd code-smells-project

# Criar e ativar virtualenv (recomendado)
python -m venv .venv
# Linux/macOS:
source .venv/bin/activate
# Windows (PowerShell):
.venv\Scripts\Activate.ps1

# Instalar dependências
pip install -r requirements.txt
```

**2. Configurar variáveis de ambiente**
```bash
cp .env.example .env
# Editar .env com valores reais:
#   SECRET_KEY=uma-chave-longa-e-aleatoria
#   DATABASE_PATH=/caminho/absoluto/para/loja.db
#   ADMIN_TOKEN=token-para-operacoes-admin
```

> Para testes locais, qualquer string serve nos campos de segredo. O 
`DATABASE_PATH` pode ser omitido - sem ele o banco cria em `loja.db` na raiz do 
projeto.

**3. Invocar a skill**
```bash
claude "/refactor-arch"
```

O Claude Code vai:
- Executar a **Fase 1** e imprimir o resumo de stack/arquitetura
- Executar a **Fase 2**, listar os findings e perguntar:
  ```
  Phase 2 complete. Proceed with refactoring (Phase 3)? [y/n]
  ```
- Após confirmar com `y`, executar a **Fase 3** e modificar os arquivos

**4. Iniciar a aplicação**
```bash
python app.py
# Saída esperada:
#  * Serving Flask app 'app'
#  * Running on http://127.0.0.1:5000
```

#### Projeto 2 - ecommerce-api-legacy

**1. Preparar o ambiente**
```bash
cd ecommerce-api-legacy
npm install
```

**2. Configurar variáveis de ambiente**
```bash
cp .env.example .env
# Editar .env com valores reais:
#   PORT=3000
#   PAYMENT_GATEWAY_KEY=sua-chave-de-gateway
#   ADMIN_TOKEN=token-para-rotas-admin
```

> `ADMIN_TOKEN` é obrigatório para acessar `GET /api/admin/financial-report` e 
`DELETE /api/users/:id`. Para testes, qualquer string serve (ex: `test-admin-token`).

**3. Invocar a skill**
```bash
claude "/refactor-arch"
```

**4. Iniciar a aplicação**
```bash
# Usando o script do package.json:
ADMIN_TOKEN=test-admin-token npm start

# Ou diretamente (Linux/macOS):
ADMIN_TOKEN=test-admin-token node src/app.js

# Windows (PowerShell):
$env:ADMIN_TOKEN="test-admin-token"; node src/app.js

# Saída esperada:
# Frankenstein LMS rodando na porta 3000...
```

#### Projeto 3 - task-manager-api

**1. Preparar o ambiente**
```bash
cd task-manager-api

python -m venv .venv
# Linux/macOS:
source .venv/bin/activate
# Windows (PowerShell):
.venv\Scripts\Activate.ps1

pip install -r requirements.txt
```

**2. Configurar variáveis de ambiente**
```bash
cp .env.example .env
# Editar .env com valores reais:
#   SECRET_KEY=uma-chave-longa-e-aleatoria
#   DATABASE_URL=sqlite:///tasks.db
#   EMAIL_USER=seu-email@exemplo.com
#   EMAIL_PASSWORD=sua-senha-de-app
```

> `DATABASE_URL` pode ser omitido - sem ele o app usa `sqlite:///tasks.db` na 
raiz do projeto. As variáveis `EMAIL_USER` e `EMAIL_PASSWORD` só são necessárias 
se a funcionalidade de notificação por email for usada.

**3. Invocar a skill**
```bash
claude "/refactor-arch"
```

**4. Popular o banco e iniciar a aplicação**
```bash
# Seed (opcional - cria 3 usuários, 4 categorias e 10 tasks de exemplo):
python src/infrastructure/seed.py

# Iniciar o servidor:
python app.py
# Saída esperada:
#  * Serving Flask app 'app'
#  * Running on http://127.0.0.1:5000
```

### Como Validar que a Refatoração Funcionou

Execute os passos abaixo após cada execução da skill, com a aplicação rodando.

#### Projeto 1 - code-smells-project

```bash
# Health check
curl -s http://localhost:5000/health
# Esperado: {"counts":{...},"database":"connected","status":"ok","versao":"1.0.0"}
# Ausente:  campos "secret_key", "debug", "db_path"

# Listagem de produtos
curl -s http://localhost:5000/produtos
# Esperado: HTTP 200 com lista de produtos

# Login (hash werkzeug, sem MD5)
curl -s -X POST http://localhost:5000/login \
  -H "Content-Type: application/json" \
  -d '{"email":"admin@loja.com","senha":"admin123"}'
# Esperado: HTTP 200 - campo "senha" ausente na response

# Proteção de rota admin
curl -s -X POST http://localhost:5000/admin/reset-db
# Esperado: HTTP 401 {"erro":"Acesso não autorizado"}

# Greps de anti-patterns (todos devem retornar 0 matches)
grep -RnsE "execute\(f\"SELECT.*\+" src/
grep -RnsE "(md5|sha1|hashlib\.)" src/
grep -RnsE "SECRET_KEY\s*=\s*['\"]" src/
grep -RnsE "jsonify.*str\(e\)" src/ | grep -v error_handler
```

#### Projeto 2 - ecommerce-api-legacy

```bash
# Checkout bem-sucedido
curl -s -X POST http://localhost:3000/api/checkout \
  -H "Content-Type: application/json" \
  -d '{"usr":"Teste","eml":"teste@email.com","c_id":2,"card":"4111222233334444"}'
# Esperado: HTTP 200 {"msg":"Sucesso","enrollment_id":...}

# Rota protegida sem token
curl -s http://localhost:3000/api/admin/financial-report
# Esperado: HTTP 401 {"error":"Unauthorized"}

# Rota protegida com token
curl -s -H "x-admin-token: $ADMIN_TOKEN" \
  http://localhost:3000/api/admin/financial-report
# Esperado: HTTP 200 com array de cursos e receita

# Greps de anti-patterns (todos devem retornar 0 matches)
grep -RnsE "(pk_live|senha_super_secreta|admin_master)" src/
grep -RnsE "badCrypto|Buffer\.from.*base64" src/
grep -RnsE "console\.log.*(card|cc|GatewayKey)" src/
grep -RnsE "globalCache|totalRevenue" src/
```

#### Projeto 3 - task-manager-api

```bash
# Health check
curl -s http://localhost:5000/health
# Esperado: {"status":"ok","timestamp":"..."}

# Listagem de tasks (sem password, com user_name e category_name)
curl -s http://localhost:5000/tasks
# Esperado: HTTP 200 - campo "password" ausente; "user_name" e "category_name" presentes

# Login com token HMAC real
curl -s -X POST http://localhost:5000/login \
  -H "Content-Type: application/json" \
  -d '{"email":"joao@email.com","password":"1234"}'
# Esperado: HTTP 200 - token no formato "1:a1b2c3..." (HMAC-SHA256, não "fake-jwt-token-1")

# Rota protegida sem token
curl -s -X PUT http://localhost:5000/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"status":"done"}'
# Esperado: HTTP 401 {"error":"Autenticação necessária"}

# Rota protegida com token (substituir TOKEN pelo retornado no login)
curl -s -X PUT http://localhost:5000/tasks/1 \
  -H "Authorization: Bearer TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"status":"done"}'
# Esperado: HTTP 200 com task atualizada

# Stats de tasks
curl -s http://localhost:5000/tasks/stats
# Esperado: {"cancelled":...,"completion_rate":...,"done":...,"total":10}

# Greps de anti-patterns (todos devem retornar 0 matches)
grep -RnsE "hashlib\.md5|\.md5\(" src/
grep -RnsE "fake-jwt" src/
grep -RnsE "'password'.*self\.password" src/
grep -RnsE "db\.session\.(add|commit|delete)" src/services/
grep -RnsE "\.query\.get\(" src/
grep -RnsE "^\s+except:\s*$" src/
grep -RnsE "(SECRET_KEY|email_password)\s*=\s*['\"][^'\"$]" src/
```

### Reexecutar a Skill (Iteração)

Se precisar executar a skill novamente em um projeto já refatorado (ex: para t
estar ajustes nos arquivos de referência), a skill vai analisar a estrutura atual 
e adaptar os findings ao estado presente - não ao estado original. Isso é o 
comportamento esperado: a skill é agnóstica de histórico.

Para restaurar o estado original de um projeto antes de reexecutar:
```bash
git checkout -- <nome-do-projeto>/
```

Para testar apenas os arquivos de referência sem modificar código:
```bash
claude "/refactor-arch"
# Responder "n" na pausa da Fase 2 - apenas o relatório é gerado
```

