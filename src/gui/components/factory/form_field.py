from dataclasses import dataclass
from typing import Optional, Tuple
from customtkinter import CTkEntry

@dataclass
class FormField:
    name_field: Optional[str]
    field: CTkEntry

    def get(self) -> str:
        return self.field.get()

    def clear(self) -> None:
        self.field.delete(0, "end")
        self.field.configure(placeholder_text=self.field.cget("placeholder_text"))

    def wrap_field(self) -> Tuple[Optional[str], str]:
        """
        Método para encapsular o nome do campo e o valor do campo.
        Args:
            None
        Returns:
            Tuple(str, str): Tuple com o nome do campo e o valor do campo.

        Exemplo de uso:
        >>> form_field = FormField(name_field="Nome", field=CTkEntry(master=master, placeholder="Digite seu nome"))
        >>> name, value = form_field.wrap_field()
        >>> print(name, value)
        >>> ("Nome", "John Doe")
        """
        return (self.name_field, self.field.get())