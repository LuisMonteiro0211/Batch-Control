from PIL import Image
from customtkinter import CTkImage 
from pathlib import Path

def image_processing(file_name: str, gap: int) -> Image:
    """
    Processa uma imagem para adicionar um gap entre a imagem e a borda.

    Args:
        file_name: Nome do arquivo da imagem.
        gap: Tamanho do gap em pixels.

    Returns:
        Image: Imagem processada com o gap.
    """
    image = Image.open(file_name).convert("RGBA")
    image = image.resize((16, 16), Image.LANCZOS)
    width, height = image.size
    new_width = width + gap

    new_image = Image.new("RGBA", (new_width, height), (0,0,0,0))

    new_image.paste(image,(0,0))

    return new_image

def icon_button(file_name: str) -> CTkImage:
    """
    Retorna um ícone para o botão já tradado com o tamanho necessário de 22x16 pixels

    Args:
        file_name: Nome do arquivo da imagem.

    Returns:
        CTkImage: Ícone para o botão já tradado com o tamanho necessário de 22x16 pixels.
    """

    path_icon = Path(__file__).parent.parent / "icons" / file_name
    pil_icon = image_processing(path_icon, 6)

    return CTkImage(light_image=pil_icon, dark_image=pil_icon, size=(22, 16))