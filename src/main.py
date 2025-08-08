import cv2
import time
from ultralytics import YOLO
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import platform

# --- VERIFICA SE ESTÁ RODANDO NO RASPBERRY PI ---
IS_RASPBERRY_PI = False
try:
    # platform.machine() retorna 'armv7l', 'aarch64', etc. em um Pi
    if platform.machine().startswith('arm') or platform.machine().startswith('aarch64'):
        import rasp
        IS_RASPBERRY_PI = True
        print("Ambiente Raspberry Pi detectado. Usando controle de GPIO.")
    else:
        print("Ambiente não-Raspberry Pi (Linux/Windows) detectado. Usando função de placeholder.")
except ImportError:
    print("AVISO: Erro ao importar o módulo 'rasp.py'. Funções de GPIO desativadas.")
    IS_RASPBERRY_PI = False


# --- PARÂMETROS DE CONFIGURAÇÃO ---
CAMERA_INDEX = 1  # Use 0 para webcam interna, 1, 2, etc., para externas.
OFF_DELAY_SECONDS = 20
CONFIDENCE_THRESHOLD = 0.5
FONT_PATH = "../assets/fonts/ARIAL.TTF"

try:
    ImageFont.truetype(FONT_PATH, 10)
    FONT_AVAILABLE = True
    print(f"Fonte '{FONT_PATH}' carregada com sucesso.")
except IOError:
    print(f"AVISO: Arquivo de fonte '{FONT_PATH}' não encontrado.")
    print("O texto será exibido com a fonte padrão do OpenCV (sem acentos).")
    FONT_AVAILABLE = False


# --- FUNÇÃO DE INTEGRAÇÃO (PLACEHOLDER PARA NÃO-PI) ---
def send_command_to_esp32(command):
    """Função de integração com o hardware (ESP32/Arduino)."""
    print(f"--- [AÇÃO DO SISTEMA] --- Enviando comando: '{command}'")


# --- FUNÇÃO PARA DESENHAR TEXTO COM ACENTOS ---
def putText_com_acento(frame, text, position, font_path, font_size, color_bgr):
    if not FONT_AVAILABLE:
        cv2.putText(frame, text, position, cv2.FONT_HERSHEY_SIMPLEX, font_size / 30, color_bgr, 2)
        return frame

    pil_img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    font = ImageFont.truetype(font_path, font_size)
    draw = ImageDraw.Draw(pil_img)
    color_rgb = (color_bgr[2], color_bgr[1], color_bgr[0])
    draw.text(position, text, font=font, fill=color_rgb)
    return cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)


# --- LÓGICA PRINCIPAL DE DETECÇÃO ---
def main():
    print("Iniciando o sistema de detecção de pessoas...")

    # Se for um Raspberry Pi, configura o GPIO
    if IS_RASPBERRY_PI:
        rasp.setup_gpio()

    try:
        model = YOLO('yolov5nu.pt')
    except Exception as e:
        print(f"Erro ao carregar o modelo YOLO. Verifique sua conexão com a internet. Erro: {e}")
        return

    cap = cv2.VideoCapture(CAMERA_INDEX)
    if not cap.isOpened():
        print(f"Erro: Não foi possível abrir a câmera com índice {CAMERA_INDEX}.")
        return

    light_is_on = False
    last_person_seen_time = 0

    print(f"Usando modelo YOLOv5. Sistema em execução na câmera {CAMERA_INDEX}. Pressione 'q' para sair.")

    while True:
        success, frame = cap.read()
        if not success:
            print("Falha ao capturar frame. Fim do stream?")
            break

        results = model(frame, conf=CONFIDENCE_THRESHOLD, classes=[0], verbose=False)
        
        person_detected_this_frame = False
        person_count = 0
        
        for r in results:
            for box in r.boxes:
                if int(box.cls[0]) == 0:
                    person_detected_this_frame = True
                    person_count += 1
                    
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    confidence = float(box.conf[0])
                    label = f'Pessoa {confidence:.2f}'
                    
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    frame = putText_com_acento(frame, label, (x1, y1 - 25), FONT_PATH, 20, (0, 255, 0))

        current_time = time.time()

        if person_detected_this_frame:
            last_person_seen_time = current_time
            if not light_is_on:
                print(f"Pessoa(s) detectada(s). Ativando o sistema.")
                if IS_RASPBERRY_PI:
                    rasp.send_command_to_gpio("on")
                else:
                    send_command_to_esp32("on")
                light_is_on = True
        else:
            if light_is_on and (current_time - last_person_seen_time > OFF_DELAY_SECONDS):
                print(f"Ambiente vazio por mais de {OFF_DELAY_SECONDS}s. Desativando o sistema.")
                if IS_RASPBERRY_PI:
                    rasp.send_command_to_gpio("off")
                else:
                    send_command_to_esp32("off")
                light_is_on = False

        info_text = f"Pessoas Detectadas: {person_count}"
        status_color = (0, 255, 0) if light_is_on else (0, 0, 255)
        frame = putText_com_acento(frame, info_text, (10, 30), FONT_PATH, 25, status_color)
        
        window_title = "Detecção Automática de Pessoas (YOLOv5)"
        cv2.imshow(window_title, frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    
    # Se for um Raspberry Pi, limpa o GPIO ao sair
    if IS_RASPBERRY_PI:
        rasp.cleanup_gpio()
        
    print("Sistema finalizado.")


if __name__ == "__main__":
    main()