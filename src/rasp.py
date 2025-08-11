# --- START OF MODIFIED FILE rasp.py ---

import RPi.GPIO as GPIO
import time

# --- CONFIGURAÇÃO DOS PINOS GPIO ---
# Use uma lista para gerenciar todos os pinos dos relés.
# RELAY_PINS[0] -> Seção 1 de lâmpadas (GPIO 18)
# RELAY_PINS[1] -> Seção 2 de lâmpadas (GPIO 23)
RELAY_PINS = [18, 23] 

def setup_gpio():
    """
    Configura o modo da placa e todos os pinos de saída.
    """
    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        # Configura cada pino da lista como saída e o inicializa como DESLIGADO (LOW)
        for pin in RELAY_PINS:
            GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
        print(f"GPIO pinos {RELAY_PINS} configurados como saída.")
    except Exception as e:
        print(f"ERRO ao configurar GPIO: {e}")
        print("Certifique-se de que o script está rodando em um Raspberry Pi com privilégios de acesso ao GPIO (use 'sudo').")


def send_command_to_gpio(command):
    """
    Envia um comando para ligar ou desligar TODOS os pinos de relé.
    'command' pode ser "on" ou "off".
    """
    if command.lower() == "on":
        print(f"--- [GPIO] --- Ligando todos os relés (pinos {RELAY_PINS})")
        for pin in RELAY_PINS:
            GPIO.output(pin, GPIO.HIGH)
    elif command.lower() == "off":
        print(f"--- [GPIO] --- Desligando todos os relés (pinos {RELAY_PINS})")
        for pin in RELAY_PINS:
            GPIO.output(pin, GPIO.LOW)
    else:
        print(f"Comando GPIO desconhecido: '{command}'")

def cleanup_gpio():
    """
    Limpa as configurações do GPIO, revertendo os pinos ao estado padrão.
    """
    print("Limpando configurações do GPIO...")
    # Garante que os relés sejam desligados antes de limpar
    send_command_to_gpio("off")
    GPIO.cleanup()

# Bloco para teste direto do módulo (opcional)
if __name__ == '__main__':
    print("Testando o módulo GPIO...")
    setup_gpio()
    
    try:
        print("Ligando os relés por 5 segundos...")
        send_command_to_gpio("on")
        time.sleep(5)
        
        print("Desligando os relés.")
        send_command_to_gpio("off")
        
    finally:
        cleanup_gpio()
        print("Teste finalizado.")
# --- END OF MODIFIED FILE rasp.py ---
