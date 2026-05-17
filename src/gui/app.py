"""
Módulo principal para construção da interface gráfica da aplicação.
"""

from customtkinter import CTk

class BatchControlApp(CTk):
    def __init__(self):
        super().__init__()
        self.title("Batch Control")
        self.geometry("900x580")
        self.resizable(False, False)
        
    def run(self):
        self.mainloop()

if __name__ == "__main__":
    app = BatchControlApp()
    app.run()