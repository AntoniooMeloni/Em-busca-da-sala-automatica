# --- src/control.py ---

from . import config

# --- Importação Condicional do Módulo GPIO ---
# Tenta importar a biblioteca do Raspberry Pi apenas se estiver no ambiente correto.
if config.IS_RASPBERRY_PI:
    try:
        import RPi.GPIO as GPIO
        GPIO_AVAILABLE = True
        print("Ambiente Raspberry Pi detectado. Controle de GPIO ativado.")
    except (ImportError, RuntimeError) as e:
        print(f"AVISO: Erro ao importar RPi.GPIO ({e}). O controle de hardware será simulado.")
        GPIO_AVAILABLE = False
else:
    GPIO_AVAILABLE = False
    print("Ambiente não-Raspberry Pi. O controle de hardware será simulado.")

def setup_hardware():
    """Configura os pinos GPIO como saídas e os inicializa em estado baixo (desligado)."""
    if GPIO_AVAILABLE:
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        for pin in config.RELAY_PINS:
            GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
        print(f"GPIO pinos {config.RELAY_PINS} configurados como saída.")
    else:
        print("[SIMULAÇÃO] Hardware configurado.")

def send_command(command: str):
    """
    Envia um comando para o hardware.
    Args:
        command (str): "on" para ligar, "off" para desligar.
    """
    action_msg = "Ligando" if command.lower() == "on" else "Desligando"
    
    if GPIO_AVAILABLE:
        state = GPIO.HIGH if command.lower() == "on" else GPIO.LOW
        print(f"--- [GPIO] --- {action_msg} relés (pinos {config.RELAY_PINS})")
        for pin in config.RELAY_PINS:
            GPIO.output(pin, state)
    else:
        print(f"--- [SIMULAÇÃO] --- Comando '{command}' enviado para o hardware.")

def cleanup_hardware():
    """Limpa as configurações do GPIO, garantindo que os pinos sejam liberados."""
    if GPIO_AVAILABLE:
        print("Limpando configurações do GPIO...")
        send_command("off")  # Garante que tudo seja desligado antes de limpar
        GPIO.cleanup()
    else:
        print("[SIMULAÇÃO] Limpeza de hardware concluída.")