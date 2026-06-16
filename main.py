"""
Ponto de entrada da GUI. Execute na raiz do repositório:

    python main.py

O diretório do script fica na frente do sys.path, por isso `import src.*`
funciona quando este arquivo está na raiz do projeto.
"""

import sys

sys.dont_write_bytecode = True

from src.gui.app import BatchControlApp
from src.gui.splash_screen import SplashScreen


def main() -> None:
    splash = SplashScreen()
    splash.mainloop()

    app = BatchControlApp(context=splash.get_context())
    app.run()


if __name__ == "__main__":
    main()
