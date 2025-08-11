# --- src/detection.py ---

import os
import urllib.request
from ultralytics import YOLO
from . import config

# URL oficial e estável para o download do modelo yolov5nu.pt
MODEL_URL = "https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov5nu.pt"

def _download_model():
    """
    Função interna para baixar o modelo se ele não existir.
    Cria o diretório de destino se necessário.
    """
    # Garante que o diretório de destino (ex: 'assets/models') exista.
    model_dir = os.path.dirname(config.MODEL_PATH)
    os.makedirs(model_dir, exist_ok=True)

    print(f"Modelo não encontrado em '{config.MODEL_PATH}'.")
    print(f"Baixando de {MODEL_URL}...")
    
    try:
        # Realiza o download do arquivo da URL para o caminho de destino
        urllib.request.urlretrieve(MODEL_URL, config.MODEL_PATH)
        print("Download do modelo concluído com sucesso!")
        return True
    except Exception as e:
        print(f"ERRO CRÍTICO: Falha ao baixar o modelo. Verifique sua conexão com a internet.")
        print(f"Detalhes do erro: {e}")
        # Remove um arquivo potencialmente corrompido/incompleto
        if os.path.exists(config.MODEL_PATH):
            os.remove(config.MODEL_PATH)
        return False

def load_model():
    """
    Carrega o modelo YOLO. Se o arquivo não existir, tenta baixá-lo primeiro.
    Retorna o objeto do modelo ou None em caso de erro.
    """
    # Passo 1: Verificar se o modelo existe. Se não, tentar baixar.
    if not os.path.exists(config.MODEL_PATH):
        if not _download_model():
            # Se o download falhar, não há como continuar.
            return None

    # Passo 2: Tentar carregar o modelo (que agora deve existir).
    try:
        print(f"Carregando modelo de '{config.MODEL_PATH}'...")
        model = YOLO(config.MODEL_PATH)
        print("Modelo YOLO carregado com sucesso.")
        return model
    except Exception as e:
        print(f"ERRO CRÍTICO: Falha ao carregar o modelo YOLO. O arquivo pode estar corrompido.")
        print(f"Detalhes do erro: {e}")
        return None

def detect_people(model, frame):
    """
    Usa o modelo carregado para detectar pessoas em um único quadro de vídeo.
    Retorna uma lista de detecções e a contagem total de pessoas.
    """
    # classes=[0] filtra a detecção apenas para a classe 'person' no dataset COCO.
    results = model(frame, conf=config.CONFIDENCE_THRESHOLD, classes=[0], verbose=False)
    
    detected_items = []
    person_count = 0
    
    if results:
        for r in results:
            for box in r.boxes:
                person_count += 1
                # Armazena a caixa delimitadora (x1, y1, x2, y2) e a confiança
                detected_items.append((box.xyxy[0], float(box.conf[0])))
                    
    return detected_items, person_count