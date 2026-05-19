"""
Módulo de tema visual do projeto.

Centraliza cores, fontes e configurações de aparência. Toda a UI deve importar desse módulo
ao invés de usar código hardcoded.

Uso recomendado:
from theme import COLORS, FONTS, SETTINGS

frame.configure(
    fg_color=COLORS.fundo_primario,
    border_width=1,
    border_color=COLORS.bordas
)

ctk.CtkButton(
    master=frame,
    text="Botão",
    font=FONTS.botao_primario,
    fg_color=COLORS.botao_principal,
    hover_color=COLORS.botao_selecionado,
    text_color=COLORS.texto_principal,
    command=lambda: print("Botão clicado")
)
"""

from dataclasses import dataclass
from customtkinter import CTkFont

@dataclass(frozen=True)
class Colors:
    fundo_primario: str = "#1A1A1A"
    fundo_secundario: str = "#242424"
    elevado: str = "#2E2E2E"
    bordas: str = "#3A3A3A"
    texto_principal: str = "#E8E8E8"
    texto_secundario: str = "#A0A0A0"
    desabilitado: str = "#666666"
    botao_principal: str = "#5C8FBF"
    botao_selecionado: str = "#1E3A52"
    texto_houver: str = "#4C79A3"
    sucesso: str = "#4CAF82"
    alerta: str = "#E0A040"
    erro: str = "#C0504D"
    texto_selecionado: str = "#4C79A3"
    transparente: str = "transparent"
    texto_botao_principal: str = "#FFFFFF"

@dataclass(frozen=True)
class _FontSpec:
    family: str
    size: int
    weight: str = "normal"

class Fontes:
    """Fontes do tema. CTkFont só é criado no primeiro acesso (após a janela raiz existir)."""

    _FONT_SPECS: dict[str, _FontSpec] = {
        "titulo_tela": _FontSpec("Inter", 18, "bold"),
        "subtitulo_tela": _FontSpec("Inter", 11),
        "valor": _FontSpec("Inter", 13),
        "botao_primario": _FontSpec("Inter", 13),
        "botao_secundario": _FontSpec("Inter", 13),
        "subtitulo_menor": _FontSpec("Inter", 11),
        "texto_tabela": _FontSpec("Inter", 12),
    }

    def __init__(self) -> None:
        self._cache: dict[str, CTkFont] = {}

    def __getattr__(self, name: str) -> CTkFont:
        if name not in self._FONT_SPECS:
            raise AttributeError(f"Fonte '{name}' não definida no tema.")
        if name not in self._cache:
            spec = self._FONT_SPECS[name]
            self._cache[name] = CTkFont(
                family=spec.family,
                size=spec.size,
                weight=spec.weight,
            )
        return self._cache[name]

@dataclass(frozen=True)
class Settings:
    tema: str = "dark"

COLORS = Colors()
FONTS = Fontes()
SETTINGS = Settings()