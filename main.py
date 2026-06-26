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
from src.gui.error_window import ErrorWindow


def main() -> None:
    splash = SplashScreen()
    splash.mainloop()

    splash_error = splash.get_error()

    if splash_error  is not None:
        error_window = ErrorWindow(message=str(splash_error))
        error_window.run()

    else:
        app_context = splash.get_context()
        app = BatchControlApp(context=app_context)
        app.run()

if __name__ == "__main__":
    main()
