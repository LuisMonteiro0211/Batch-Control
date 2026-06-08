"""
Exceções customizadas do Batch-Control.

Hierarquia:
    BatchControlError          → base de tudo no projeto
    └── RepositoryError        → camada de dados (repositórios)
        ├── ProductNotFoundError
        ├── DuplicateSkuError
        └── DatabaseOperationError

Uso típico no repositório (traduz erro do SQLite → exceção do domínio):
    try:
        cursor.execute(...)
    except IntegrityError:
        raise DuplicateSkuError(entity.cod_sku) from e

Uso típico no service/GUI (trata de forma amigável):
    try:
        repo.create(produto)
    except DuplicateSkuError as e:
        mostrar_alerta(f"SKU {e.cod_sku} já existe")
    except RepositoryError:
        mostrar_alerta("Erro ao salvar no banco")
"""


class BatchControlError(Exception):
    """Exceção base do projeto. Use para capturar qualquer erro da aplicação."""

    pass


class ValidationError(BatchControlError):
    """Dados inválidos antes de chegar ao banco (camada service/GUI)."""

    pass


class RepositoryError(BatchControlError):
    """Erros da camada de acesso a dados (repositórios)."""

    pass


class ProductNotFoundError(RepositoryError):
    """Produto não encontrado em uma busca."""

    pass


class DuplicateSkuError(RepositoryError):
    """Tentativa de cadastrar um cod_sku que já existe."""

    def __init__(self, cod_sku: int) -> None:
        self.cod_sku = cod_sku
        super().__init__(f"O código SKU {cod_sku} já está cadastrado.")


class DatabaseOperationError(RepositoryError):
    """Falha inesperada ao executar uma operação no banco."""

    pass


class InvalidDateError(ValidationError):
    """Data inválida."""

    pass

class InvalidStringError(ValidationError):
    """String inválida."""

    pass

class InvalidNumberError(ValidationError):
    """Número inválido."""

    pass

class ProductHasBalanceError(BatchControlError):
    """Produto com saldo não pode ser deletado."""

    pass