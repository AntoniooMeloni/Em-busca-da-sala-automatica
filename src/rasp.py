import RPi.GPIO as GPIO
import time

# --- CONFIGURAÇÃO DO PINO GPIO ---
# Use o número do pino GPIO (BCM), não o número físico do pino.
# Exemplo: Pino físico 12 é o GPIO 18.
RELAY_PIN = 18 

def setup_gpio():
    """
    Configura o modo da placa e o pino de saída.
    """
    try:
        # Usar a numeração Broadcom (BCM) para os pinos
        GPIO.setmode(GPIO.BCM)
        # Desativa avisos de "canal já em uso"
        GPIO.setwarnings(False)
        # Configura o pino do relé como saída e o inicializa como DESLIGADO (LOW)
        GPIO.setup(RELAY_PIN, GPIO.OUT, initial=GPIO.LOW)
        print(f"GPIO pino {RELAY_PIN} configurado como saída.")
    except Exception as e:
        print(f"ERRO ao configurar GPIO: {e}")
        print("Certifique-se de que o script está rodando em um Raspberry Pi com privilégios de acesso ao GPIO (use 'sudo').")


def send_command_to_gpio(command):
    """
    Envia um comando para ligar ou desligar o pino GPIO.
    'command' pode ser "on" ou "off".
    """
    if command.lower() == "on":
        print(f"--- [GPIO] --- Ligando pino {RELAY_PIN} (HIGH)")
        GPIO.output(RELAY_PIN, GPIO.HIGH)
    elif command.lower() == "off":
        print(f"--- [GPIO] --- Desligando pino {RELAY_PIN} (LOW)")
        GPIO.output(RELAY_PIN, GPIO.LOW)
    else:
        print(f"Comando GPIO desconhecido: '{command}'")

def cleanup_gpio():
    """
    Limpa as configurações do GPIO, revertendo os pinos ao estado padrão.
    """
    print("Limpando configurações do GPIO...")
    GPIO.cleanup()

# Bloco para teste direto do módulo (opcional)
if __name__ == '__main__':
    print("Testando o módulo GPIO...")
    setup_gpio()
    
    try:
        print("Ligando o relé por 5 segundos...")
        send_command_to_gpio("on")
        time.sleep(5)
        
        print("Desligando o relé.")
        send_command_to_gpio("off")
        
    finally:
        # Garante que o cleanup será chamado mesmo se ocorrer um erro
        cleanup_gpio()
        print("Teste finalizado.")