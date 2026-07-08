from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SRC_DIR = PROJECT_ROOT / "src"
ICONS_DIR = SRC_DIR / "icons"
DATA_DIR = PROJECT_ROOT / "data"

def icon_path(icon_file_name: str) -> Path:
    """
    Retorna o caminho para uma imagem de ícone.
    Args:
        icon_file_name: Nome do arquivo da imagem de ícone.

    Returns:
        Path: Caminho para a imagem de ícone.
    """
    return ICONS_DIR / icon_file_name

def data_path(data_file_name: str) -> Path:
    """
    Retorna o caminho para um arquivo de dados.
    Args:
        data_file_name: Nome do arquivo de dados.

    Returns:
        Path: Caminho para o arquivo de dados.
    """
    return DATA_DIR / data_file_name