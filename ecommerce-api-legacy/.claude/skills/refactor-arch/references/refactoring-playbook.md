Use este arquivo somente durante a PHASE 3, após confirmação explícita do usuário.

Os exemplos abaixo são ilustrativos em Python. Adapte a sintaxe, as convenções e o naming com base na linguagem e no framework detectados na Phase 1 do projeto sendo auditado.

Por exemplo:
- Python `class Repository:` com `raise NotImplementedError` → interface ou classe abstrata com o equivalente idiomático da linguagem detectada (interface em TypeScript/Java/Go/C#, módulo em Ruby etc.)
- Python `@app.route(...)` → equivalente de routing idiomático da stack detectada (`router.get`, `@GetMapping`, `[HttpGet]`, `http.HandleFunc` etc.)
- Python `def get_db():` em `infrastructure/database.py` → módulo de conexão na camada de infraestrutura com a extensão e convenção corretas da stack detectada
- Python `raise NotImplementedError` → exceção ou erro idiomático da linguagem (`throw new Error()`, `throw new UnsupportedOperationException()`, `return fmt.Errorf(...)` etc.)

## Rules

- Preserve external behavior.
- Make the smallest safe change.
- Preserve routes/endpoints.
- Preserve HTTP methods.
- Preserve status codes.
- Preserve request contracts.
- Preserve response contracts.
- Do not introduce unnecessary dependencies.
- Prefer stack-native conventions.
- Validate boot and endpoints after changes.

## Pattern 1 — Extract Application Service from Fat Controller

Before:

```python
def create_order(request):
    data = request.json
    if data["quantity"] <= 0:
        return {"error": "invalid quantity"}, 400
    total = data["quantity"] * data["price"]
    db.execute("insert into orders values (?, ?)", data["user_id"], total)
    return {"total": total}, 201
```

After:

```python
def create_order(request):
    command = CreateOrderCommand.from_request(request)
    result = order_service.create(command)
    return order_presenter.created(result)
```

## Pattern 2 — Move SQL from Controller to Repository

Before:

```python
def get_user(user_id):
    row = db.execute("select * from users where id = ?", user_id).fetchone()
    return {"id": row["id"], "name": row["name"]}

```

After:

```python
def get_user(user_id):
    user = user_repository.find_by_id(user_id)
    return user_presenter.ok(user)
```

## Pattern 3 — Introduce Repository Port

Before:

```python
class InvoiceService:
    def __init__(self, database):
        self.database = database
```

After:

```python
class InvoiceRepository:
    def find_open_by_customer(self, customer_id):
        raise NotImplementedError


class InvoiceService:
    def __init__(self, invoice_repository):
        self.invoice_repository = invoice_repository
```

## Pattern 4 — Move Business Rule from Serializer/View to Domain

Before:

```python
def serialize_subscription(subscription):
    status = "expired" if subscription.end_date < today() else "active"
    return {"status": status}
```

After:

```python
class Subscription:
    def status(self, current_date):
        if self.end_date < current_date:
            return "expired"
        return "active"


def serialize_subscription(subscription):
    return {"status": subscription.status(today())}
```

## Pattern 5 — Replace Central Conditional with Strategy

Before:

```python
def calculate_fee(payment_type, amount):
    if payment_type == "card":
        return amount * 0.03
    if payment_type == "pix":
        return amount * 0.01
    return 0
```

After:

```python
class PaymentFeePolicy:
    def calculate(self, amount):
        raise NotImplementedError


class CardFeePolicy(PaymentFeePolicy):
    def calculate(self, amount):
        return amount * 0.03


class PixFeePolicy(PaymentFeePolicy):
    def calculate(self, amount):
        return amount * 0.01
```

## Pattern 6 — Extract Validation Boundary

Before:

```python
def register_user(request):
    user = User(request.json["email"], request.json["age"])
    return user_service.register(user)
```

After:

```python
def register_user(request):
    command = RegisterUserCommand.validate(request.json)
    result = user_service.register(command)
    return user_presenter.created(result)
```

## Pattern 7 — Centralize Error Handling

Before:

```python
def get_product(product_id):
    try:
        product = product_service.get(product_id)
        return {"id": product.id}
    except Exception as error:
        return {"error": str(error)}, 500
```

After:

```python
# Route handler — delegates to service and presenter; no local try/except
def get_product(product_id):
    product = product_service.get(product_id)
    return product_presenter.ok(product)

# Centralized error handler — registered once with the framework for all routes
def handle_error(error):
    if isinstance(error, NotFoundError):
        return {"error": "not found"}, 404
    return {"error": "internal server error"}, 500
```

## Pattern 8 — Replace Hardcoded Secret with Configuration

Before:

```python
payment_client = PaymentClient(api_key="secret-key")
```

After:

```python
payment_client = PaymentClient(api_key=settings.payment_api_key)
```

Ao aplicar este padrão:
- Crie ou atualize `.env.example` na raiz com as variáveis necessárias usando placeholders (ex: `SECRET_KEY=your-secret-key-here`).
- Nunca grave valores reais em `.env.example`.
- Verifique se `.env` está listado no `.gitignore`; se não estiver, adicione.
- Não crie nem modifique `.env` com valores reais — isso é responsabilidade do operador.

## Pattern 9 — Isolate Deprecated API Usage

Before:

```python
result = legacy_client.old_search(query)
```

After:

```python
result = search_gateway.search(query)


class SearchGateway:
    def search(self, query):
        return modern_client.search(query)
```

## Pattern 10 — Remove Framework Dependency from Domain

Before:

```python
class Order:
    def from_request(request):
        return Order(request.json["total"])
```

After:

```python
class Order:
    def __init__(self, total):
        self.total = total

class OrderMapper:
    def from_request(self, request):
        return Order(request.json["total"])
```

## Pattern 11 — Split Flat Module into Domain Files

Aplique quando um módulo monolítico (controllers, models, views) acumula múltiplos domínios em um único arquivo, e quando código de infraestrutura (conexão com banco, schema, seeds) está fora de src/infrastructure/. Todo o código da aplicação deve residir dentro de `src/`. Cada domínio recebe seu próprio arquivo dentro do diretório de camada correspondente. A estrutura de diretórios deve ser coerente com a stack detectada na Phase 1 — adapte nomes, extensões e convenções ao framework real.

Before:

```python
# controllers.py (monolítico, no root)
def listar_produtos(): ...
def criar_produto(): ...
def listar_usuarios(): ...
def criar_usuario(): ...
def criar_pedido(): ...

# database.py (no root — infraestrutura exposta fora de src/)
db_connection = None  # global mutable
def get_db(): ...
```

After:

```
requirements.txt     ← root: apenas manifesto

src/
├── app.py           ← entry point
├── infrastructure/
│   └── database.py  ← conexão, tabelas e carga inicial de dados
├── controllers/
│   ├── __init__.py
│   ├── produto_controller.py
│   ├── usuario_controller.py
│   └── pedido_controller.py
├── models/
│   ├── __init__.py
│   ├── produto_model.py
│   ├── usuario_model.py
│   └── pedido_model.py
├── views/
│   ├── __init__.py
│   └── routes.py
├── repositories/
│   └── produto_repository.py
└── services/
    └── produto_service.py
```

```python
# src/infrastructure/database.py
# Adapte: use o mecanismo de conexão per-request do framework detectado
# (ex: Flask → flask.g + teardown_appcontext; Django → django.db.connection;
#  Express → middleware de pool; Spring → DataSource bean)

def get_db():
    # retorna conexão ativa para o contexto atual; cria se não existir
    ...

def init_db(app):
    # registra teardown no ciclo de vida do framework e executa criação de schema e seed no startup
    ...

# src/repositories/produto_repository.py — importa de infrastructure
from infrastructure.database import get_db

# src/controllers/produto_controller.py
def listar(): ...
def criar(): ...

# src/models/produto_model.py
class Produto:
    def __init__(self, id, nome, preco):
        self.id = id
        self.nome = nome
        self.preco = preco

    def to_dict(self):
        return {"id": self.id, "nome": self.nome, "preco": self.preco}

# src/views/routes.py
def register_routes(app):
    app.add_url_rule("/produtos", "listar_produtos", produto_controller.listar, methods=["GET"])
    app.add_url_rule("/usuarios", "listar_usuarios", usuario_controller.listar, methods=["GET"])
```

Atualização de imports nos arquivos que referenciam o módulo movido:

```python
# Antes da movimentação — import nos módulos que dependem do banco
from database import get_db

# Após a movimentação — import atualizado para o novo caminho
from infrastructure.database import get_db
```

Se o entry point externo não puder ser alterado imediatamente, preserve o arquivo original como wrapper fino e remova assim que todos os imports forem atualizados:

```python
# database.py (root — wrapper de compatibilidade temporário)
# Wrapper mantido apenas enquanto imports externos não forem migrados — remover após migração completa
from infrastructure.database import get_db, init_db
```

## Pattern 12 — Eliminate N+1 Query

Aplique quando código carrega uma coleção e acessa relacionamentos dentro de um loop, disparando uma query adicional por item. Substitua por eager loading via ORM ou por JOIN explícito no repositório. Adapte a estratégia à stack detectada — o princípio é o mesmo independente do ORM ou driver.

Before:

```python
# repository — carrega apenas a entidade principal, sem relacionamentos
def find_all():
    return Task.query.all()

# controller/route — acessa relacionamentos em loop → 1 + N*R queries
# (N = número de tasks, R = número de relacionamentos acessados por item)
def get_tasks():
    tasks = task_repository.find_all()
    return [
        {"title": t.title, "user": t.user.name, "category": t.category.name}
        for t in tasks
    ]
```

After (opção 1 — eager loading declarado no model, preferível quando o ORM suporta):

```python
# model — relacionamentos carregados com JOIN automaticamente
class Task(db.Model):
    user     = db.relationship("User",     lazy="joined")
    category = db.relationship("Category", lazy="joined")

# repository — inalterado; ORM emite JOIN na query principal
def find_all():
    return Task.query.all()
```

After (opção 2 — JOIN explícito no repositório, preferível quando lazy loading não está disponível ou quando o controle da query é necessário):

```python
# repository — carrega dados relacionados em query única
def find_all():
    return (
        db.session.query(Task)
        .join(User,     Task.user_id     == User.id,     isouter=True)
        .join(Category, Task.category_id == Category.id, isouter=True)
        .options(db.contains_eager(Task.user), db.contains_eager(Task.category))
        .all()
    )
```

## Pattern 13 — Remove Sensitive Field from Serializer

Aplique quando um serializer, `to_dict()`, presenter ou DTO expõe campos sensíveis (password hash, token, secret, PII) em responses de API. Use allowlist explícita de campos em vez de serializar o objeto inteiro. Adapte à convenção de serialização da stack detectada.

Before:

```python
class User(db.Model):
    def to_dict(self):
        return {
            "id":         self.id,
            "name":       self.name,
            "email":      self.email,
            "password":   self.password,   # hash exposto em toda response de usuário
            "role":       self.role,
            "created_at": str(self.created_at),
        }
```

After:

```python
class User(db.Model):
    def to_dict(self):
        return {
            "id":         self.id,
            "name":       self.name,
            "email":      self.email,
            "role":       self.role,
            "created_at": str(self.created_at),
            # password excluído — nunca deve ser serializado em responses de API
        }
```

Campos que nunca devem aparecer em responses: `password`, `password_hash`, `token`, `secret`, `api_key`, `salt`, campos de PII regulado (CPF, número de cartão, dados médicos). Prefira allowlist (liste explicitamente o que expor) a blocklist (tente lembrar o que omitir).
