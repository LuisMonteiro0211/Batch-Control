from PIL import Image
from customtkinter import CTkImage 
from pathlib import Path

def image_processing(file_name: Path, gap: int, size: tuple[int, int]) -> Image.Image:
    """
    Processa uma imagem para adicionar um gap entre a imagem e a borda.

    Args:
        file_name: Nome do arquivo da imagem.
        gap: Tamanho do gap em pixels.
        size: Tamanho da imagem em pixels.
    Returns:
        Image: Imagem processada com o gap.
    """
    image: Image.Image = Image.open(file_name).convert("RGBA")
    image = image.resize(size, Image.Resampling.LANCZOS)
    width, height = image.size
    new_width = width + gap

    new_image: Image.Image = Image.new("RGBA", (new_width, height), (0,0,0,0))

    new_image.paste(image,(0,0))

    return new_image

def icon_button(file_name: str, size: tuple[int, int], gap: int = 6) -> CTkImage:
    """
    Retorna um ícone para o botão já tratado com o tamanho informado.

    Args:
        file_name: Nome do arquivo da imagem.
        size: Tamanho da imagem em pixels (largura, altura).
        gap: Espaço transparente à direita do ícone, em pixels.

    Returns:
        CTkImage: Ícone pronto para uso em botões ou labels.
    """

    path_icon = Path(__file__).parent.parent / "icons" / file_name
    pil_icon = image_processing(path_icon, gap, size)
    display_size = (size[0] + gap, size[1])

    return CTkImage(light_image=pil_icon, dark_image=pil_icon, size=display_size)