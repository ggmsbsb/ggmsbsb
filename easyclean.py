from PIL import Image, ImageDraw

def create_erase_and_fade_gif(logo_path, output_gif, frames=120, frame_duration=50):
    """Cria um GIF com o texto apagando da esquerda para a direita e depois voltando com um fade in."""
    logo = Image.open(logo_path).convert("RGBA")
    width, height = logo.size
    
    images = []
    
    # Fase 1: Apagar o texto da esquerda para a direita
    for i in range(frames // 2):
        frame = Image.new("RGBA", logo.size, (255, 255, 255, 255))
        erase_width = int((i / (frames // 2)) * width)
        draw = ImageDraw.Draw(frame)
        draw.rectangle([erase_width, 0, width, height], fill=(255, 255, 255, 0))
        erased_logo = Image.alpha_composite(frame, logo)
        images.append(erased_logo)
    
    # Fase 2: Fade in do texto
    for i in range(frames // 2):
        frame = Image.new("RGBA", logo.size, (255, 255, 255, 255))
        opacity = int((i / (frames // 2)) * 255)
        faded_logo = logo.copy()
        faded_logo.putalpha(opacity)
        frame.paste(faded_logo, (0, 0), faded_logo)
        images.append(frame)
    
    # Salvar os frames como um GIF animado
    images[0].save(output_gif, save_all=True, append_images=images[1:], duration=frame_duration, loop=0)
    print(f"GIF salvo como {output_gif}")

# Exemplo de uso:
create_erase_and_fade_gif("easy-noborder.png", "easy-noborder_erase_fade.gif")