# Anti-pattern Catalog

Use este arquivo durante a PHASE 2.

Este catálogo é um baseline mínimo, não uma lista exaustiva.
Aplique conhecimento externo relevante somente quando houver evidência concreta no código, nas dependências, nos arquivos de configuração, nos warnings disponíveis ou em documentação presente no repositório. Isso inclui vulnerabilidades de segurança (OWASP Top 10, CWE), performance anti-patterns, anti-patterns específicos da linguagem ou framework detectados e problemas de design ou segurança. Não declare vulnerabilidade, depreciação ou incompatibilidade apenas por memória ou suposição.
Não limite os findings ao que está listado aqui.

Todo finding deve ter evidência concreta.

## Severity model

- CRITICAL: exposição de segurança, segredo hardcoded, colapso arquitetural, fluxo crítico intestável ou falha de produção de alto risco.
- HIGH: violação forte de MVC/SOLID com alto custo de manutenção, coupling elevado, baixa testabilidade ou amplo change impact.
- MEDIUM: design smell localizado que pode crescer se repetido.
- LOW: problema menor de organização, naming, duplicação ou clareza.

## Catalog

| Anti-pattern | Default severity | Principles | Detection signals |
|---|---:|---|---|
| Hardcoded Credentials or Secrets | CRITICAL | Security, DIP | tokens, passwords, API keys, private URLs ou credentials no source code |
| SQL Injection | CRITICAL | Security, Input Validation | concatenação de string em query SQL com input do usuário; ausência de prepared statements ou parameterized queries; f-string, %, .format() ou concatenação direta em raw SQL; ORM com execução de SQL bruto via text() ou execute() sem bind parameters |
| Weak Password Hashing | CRITICAL | Security, OWASP A02:2021 | função de hash genérica (md5, sha1, sha256, sha512) aplicada diretamente a campo de senha antes de persistir; ausência de salt ou KDF; exemplos: hashlib.sha256(pwd), crypto.createHash('sha256'), MessageDigest.getInstance('SHA-256') usados para armazenar ou comparar senhas |
| Direct Database Access in Controller/View | HIGH | MVC, SRP, DIP | SQL, ORM session, query builder ou database client em controller, handler, view ou serializer |
| Fat Controller | HIGH | MVC, SRP | HTTP handling misturado com validation, persistence, business rules e formatting |
| God Class / God Method | HIGH | SRP, OCP, Testability | classe/método grande, responsabilidades não relacionadas, muitos motivos para mudar |
| Framework Leakage into Domain | HIGH | DIP, Clean Architecture | domain importando HTTP framework, ORM session, request/response, cloud SDK ou filesystem |
| Circular Dependencies | HIGH | DIP, Layering | imports cíclicos entre layers, modules ou domains |
| Sensitive Data Exposure | HIGH | Security, SRP | campo sensível (password, token, secret, PII) serializado em response de API; to_dict() / serializer / presenter incluindo campos que não devem ser expostos |
| N+1 Query | HIGH | Performance, SRP, DIP | loop sobre coleção com acesso a relacionamento não carregado; múltiplos SELECT por item em vez de JOIN ou eager load |
| Dependency Hygiene Violation | HIGH | Security, Reliability, Maintainability | dependência usada no código mas ausente no manifest (quebra em deploy); dependência declarada no manifest mas nunca importada (surface de ataque desnecessária) |
| Duplicated Business Rules | MEDIUM | SRP, OCP | mesma regra repetida em controllers, serializers, services, views ou models |
| Missing Validation Boundaries | MEDIUM | MVC, Security, SRP | input não confiável passado diretamente para domain, DB ou external service |
| Business Logic in View/Serializer | MEDIUM | MVC, SRP | cálculos, authorization, state changes ou decisões em template/serializer |
| Deprecated API Usage | MEDIUM | Maintainability, Security | APIs, methods, annotations, config keys ou dependencies marcadas como deprecated |
| Poor Error Handling | MEDIUM | Reliability, Testability | broad catch, swallowed errors, leaked stack traces ou responses inconsistentes |
| Anemic Domain Model | MEDIUM | MVC, SRP, OOP | domain objects somente com dados enquanto regras ficam espalhadas |
| Hidden Global State | MEDIUM | Testability, Reliability | mutable globals, singleton state ou environment reads em domain logic |
| Excessive Static Helpers | LOW | SRP, Testability | helpers estáticos genéricos substituindo services coesos |
| Naming or Organization Drift | LOW | Maintainability | nomes ambíguos, organização inconsistente, boundaries confusos ou magic numbers soltos no código |

## Deprecated API Usage

Detecte Deprecated API Usage quando houver evidência como:

- símbolo marcado como deprecated
- comentário indicando deprecated, legacy, old API ou TODO migrate
- warning de build/runtime
- annotation/decorator deprecated
- configuration key deprecated
- API substituída por alternativa oficial
- dependency API com risco de remoção em upgrade

Severity guidance:

- CRITICAL: cria exposição de segurança ou risco direto de produção.
- HIGH: bloqueia upgrade ou afeta fluxo core.
- MEDIUM: uso localizado que deve ser migrado.
- LOW: aparece somente em tooling, samples ou código não crítico.

Não declare deprecation sem evidência.

## Weak Password Hashing

Detecte Weak Password Hashing quando houver evidência como:

- hash genérico (md5, sha1, sha256, sha512) aplicado diretamente a uma senha
- ausência de salt embutido ou custo configurável (work factor / iterations)
- comparação de senhas feita via igualdade de strings em vez de função de verificação segura

Use o KDF já incluído no framework detectado — sem nova dependência:

| Stack detectada na Phase 1 | KDF recomendado (sem nova dependência) |
|---|---|
| Python + Flask | werkzeug.security.generate_password_hash / check_password_hash |
| Python + Django | django.contrib.auth.hashers.make_password / check_password |
| Python (stdlib) | hashlib.pbkdf2_hmac |
| Node.js (stdlib) | crypto.scrypt ou crypto.pbkdf2 |
| Java + Spring | BCryptPasswordEncoder (Spring Security) |
| Ruby + Rails | has_secure_password (bcrypt) |
| PHP | password_hash() com PASSWORD_BCRYPT ou PASSWORD_ARGON2ID |
| Go | golang.org/x/crypto/bcrypt |

Se o framework não incluir KDF embutido: adicionar bcrypt, argon2 ou passlib como dependência explícita.

Nunca usar SHA-256 ou qualquer hash rápido para senha — mesmo com salt manual, o custo computacional é insuficiente contra ataques de força bruta com GPU.

Severity guidance:

- CRITICAL: senhas em plaintext ou com hash genérico no banco — qualquer dump expõe todas as credenciais.
- HIGH: KDF sem salt adequado ou custo configurável muito baixo.

Não declare Weak Password Hashing sem evidência de uso de hash genérico sobre campo de senha.