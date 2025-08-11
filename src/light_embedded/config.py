# --- src/config.py ---

import os
import platform

# --- PARÂMETROS DE DETECÇÃO E CÂMERA ---
CAMERA_INDEX = 1          # 0 para webcam interna, 1, 2, etc., para externas.
CONFIDENCE_THRESHOLD = 0.5 # Limiar de confiança para detecção (0.0 a 1.0)
OFF_DELAY_SECONDS = 20    # Segundos sem detecção para desligar o sistema

# --- CAMINHOS PARA ASSETS ---
# Constrói caminhos a partir da localização deste arquivo para garantir que funcione em qualquer lugar.
# BASE_ASSETS_PATH aponta para a pasta 'assets' que está no mesmo nível da pasta 'src'.
BASE_ASSETS_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "assets"))
FONT_PATH = os.path.join(BASE_ASSETS_PATH, "fonts/ARIAL.TTF")
MODEL_PATH = os.path.join(BASE_ASSETS_PATH, "models/yolov5nu.pt")

# --- CONFIGURAÇÃO DE HARDWARE (Raspberry Pi) ---
# Lista de pinos GPIO (no modo BCM) que controlam os relés.
# Adicione mais pinos a esta lista para controlar mais seções de luzes.
RELAY_PINS = [18, 23]

# --- VERIFICAÇÃO DE AMBIENTE DE EXECUÇÃO ---
# Determina se o código está rodando em um Raspberry Pi para ativar o controle GPIO.
IS_RASPBERRY_PI = platform.machine().startswith(('arm', 'aarch64'))