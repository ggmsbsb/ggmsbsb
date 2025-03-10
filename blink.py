from PIL import Image, ImageDraw

# Imagem que tu quer fazer o gif de piscar
logo = Image.open("lkd.png").convert("RGBA")

num_frames = 120
frame_duration = 50  # duração em milissegundos da animação

# Lista pra guardar os frames
frames = []

for i in range(num_frames):
    # Nova imagem de tamanho igual com fundo transparente
    frame = Image.new("RGBA", logo.size, (0, 0, 0, 0))
    
    # Animação de piscar. Feito baseado na opacidade.
    opacity = int(255 * (1 - abs((i / (num_frames / 2)) - 1)))
    logo_with_opacity = logo.copy()
    logo_with_opacity.putalpha(opacity)
    
    # Logo no frame
    frame.paste(logo_with_opacity, (0, 0), logo_with_opacity)
    
    # Frame para a lista
    frames.append(frame)

# Salvar os frames como um GIF
frames[0].save("lkd_blink.gif", save_all=True, append_images=frames[1:], duration=frame_duration, loop=0, transparency=0, disposal=2)