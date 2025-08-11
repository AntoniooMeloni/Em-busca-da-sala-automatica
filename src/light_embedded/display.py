# --- src/display.py ---

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import os
from . import config

# --- Verificação da Fonte ---
# Verifica uma vez no início se a fonte customizada está disponível.
FONT_AVAILABLE = os.path.exists(config.FONT_PATH)
if FONT_AVAILABLE:
    print(f"Fonte '{config.FONT_PATH}' encontrada. Textos terão suporte a acentos.")
else:
    print(f"AVISO: Fonte '{config.FONT_PATH}' não encontrada. Usando fonte padrão do OpenCV.")

def draw_text(frame, text, position, font_size, color_bgr):
    """Desenha texto no frame, usando Pillow para suporte a acentos se a fonte estiver disponível."""
    if FONT_AVAILABLE:
        pil_img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        font = ImageFont.truetype(config.FONT_PATH, font_size)
        draw = ImageDraw.Draw(pil_img)
        color_rgb = (color_bgr[2], color_bgr[1], color_bgr[0]) # Converte BGR para RGB
        draw.text(position, text, font=font, fill=color_rgb)
        return cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)
    else:
        # Fallback para a fonte do OpenCV (não suporta acentos bem)
        cv2.putText(frame, text, position, cv2.FONT_HERSHEY_SIMPLEX, font_size / 25.0, color_bgr, 2)
        return frame

def draw_detection_boxes(frame, detected_items):
    """Desenha as caixas delimitadoras para todos os itens detectados."""
    for box, confidence in detected_items:
        x1, y1, x2, y2 = map(int, box)
        label = f'Pessoa {confidence:.2f}'
        color = (0, 255, 0)  # Verde
        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
        frame = draw_text(frame, label, (x1, y1 - 25), 20, color)
    return frame

def draw_status_overlay(frame, person_count, light_is_on):
    """Desenha o painel de informações de status no canto da tela."""
    info_text = f"Pessoas Detectadas: {person_count}"
    status_color = (0, 255, 0) if light_is_on else (0, 0, 255) # Verde se ligado, Vermelho se desligado
    frame = draw_text(frame, info_text, (10, 30), 25, status_color)
    return frame

def show_frame(frame):
    """Exibe o frame final em uma janela do OpenCV."""
    window_title = "Sistema de Detecção Automática (YOLO)"
    cv2.imshow(window_title, frame)