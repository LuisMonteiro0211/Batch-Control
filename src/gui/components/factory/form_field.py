from dataclasses import dataclass
from typing import Union
from customtkinter import CTkEntry
from customtkinter import CTkSegmentedButton
@dataclass
class FormField:
    name_field: str
    field: Union[CTkEntry, CTkSegmentedButton]

    def get(self) -> str:
        return self.field.get()

    def clear(self) -> None:
        if isinstance(self.field, CTkEntry):
            self.field.delete(0, "end")
            self.field.configure(placeholder_text=self.field.cget("placeholder_text"))