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

@dataclass
class Colors:
    fundo_primario = "#1A1A1A"
    fundo_secundario = "#242424"
    elevado = "#2E2E2E"
    bordas = "#3A3A3A"
    texto_principal = "#E8E8E8"
    texto_secundario = "#A0A0A0"
    desabilitado = "#666666"
    botao_principal = "#5C8FBF"
    botao_selecionado = "#1E3A52"
    texto_houver = "#4C79A3"
    sucesso = "#4CAF82"
    alerta = "#E0A040"
    erro = "#C0504D"

@dataclass
class Fontes:
    titulo_tela = "Inter", "Bold", 18
    subtitulo_tela = "Inter", "Regular", 13
    valor = "Inter", "Regular", 13
    botao_primario = "Inter", "Bold", 13
    botao_secundario = "Inter", "Regular", 13
    subtitulo_menor = "Inter", "Regular", 11

@dataclass
class Settings:
    tema = "dark"

COLORS = Colors()
FONTS = Fontes()
SETTINGS = Settings()