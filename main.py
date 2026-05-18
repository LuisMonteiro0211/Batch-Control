"""
Ponto de entrada da GUI. Execute na raiz do repositório:

    python main.py

O diretório do script fica na frente do sys.path, por isso `import src.*`
funciona quando este arquivo está na raiz do projeto.
"""

from src.gui.app import BatchControlApp


def main() -> None:
    app = BatchControlApp()
    app.run()


if __name__ == "__main__":
    main()
