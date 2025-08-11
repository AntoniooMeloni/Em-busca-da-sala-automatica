# --- src/main.py ---

import cv2
import time

# Importa os módulos da nossa aplicação
from . import config
from . import control
from . import detection
from . import display

def run():
    """Função principal que executa o ciclo de vida da aplicação."""
    print("--- INICIANDO SISTEMA DE DETECÇÃO AUTOMÁTICA ---")

    # 1. INICIALIZAÇÃO
    control.setup_hardware()
    model = detection.load_model()
    if model is None:
        print("Finalizando aplicação devido a erro no carregamento do modelo.")
        return

    cap = cv2.VideoCapture(config.CAMERA_INDEX)
    if not cap.isOpened():
        print(f"ERRO: Não foi possível abrir a câmera com índice {config.CAMERA_INDEX}.")
        return

    # 2. ESTADO DA APLICAÇÃO
    light_is_on = False
    last_person_seen_time = 0

    print(f"\nSistema em execução. Pressione 'q' na janela de vídeo para sair.")

    # 3. LOOP PRINCIPAL
    try:
        while True:
            success, frame = cap.read()
            if not success:
                print("Falha ao capturar frame. Fim do stream de vídeo.")
                break

            # MÓDULO DE DETECÇÃO
            detected_items, person_count = detection.detect_people(model, frame)
            
            # MÓDULO DE CONTROLE
            current_time = time.time()
            person_detected = person_count > 0

            if person_detected:
                last_person_seen_time = current_time
                if not light_is_on:
                    print(f"[{time.strftime('%H:%M:%S')}] Pessoa(s) detectada(s). Ativando sistema.")
                    control.send_command("on")
                    light_is_on = True
            elif light_is_on and (current_time - last_person_seen_time > config.OFF_DELAY_SECONDS):
                print(f"[{time.strftime('%H:%M:%S')}] Ambiente vazio por {config.OFF_DELAY_SECONDS}s. Desativando sistema.")
                control.send_command("off")
                light_is_on = False

            # MÓDULO DE DISPLAY
            frame = display.draw_detection_boxes(frame, detected_items)
            frame = display.draw_status_overlay(frame, person_count, light_is_on)
            display.show_frame(frame)

            # Verificação de saída
            if cv2.waitKey(1) & 0xFF == ord('q'):
                print("Tecla 'q' pressionada. Encerrando...")
                break
    finally:
        # 4. FINALIZAÇÃO
        cap.release()
        cv2.destroyAllWindows()
        control.cleanup_hardware()
        print("--- SISTEMA FINALIZADO ---")

# Ponto de entrada para executar o script
if __name__ == '__main__':
    run()