from machine import Pin, time_pulse_us
import time

# --- Configuração dos Pinos ---
PINO_TRIG = 25
PINO_ECHO = 27
PINO_LED_CAIXA = 26  # LED indicador de caixa completa

trig = Pin(PINO_TRIG, Pin.OUT)
echo = Pin(PINO_ECHO, Pin.IN)
led_caixa = Pin(PINO_LED_CAIXA, Pin.OUT)

# --- Parâmetros ---
DIST_THRESH_CM = 10     # Limite de distância para detectar frasco
MIN_GAP_MS = 300        # Tempo mínimo entre detecções (ms)

# --- Variáveis de contagem ---
itens = 0
caixas = 0
ultimo_pulso_ms = 0
estado_presenca = False

# --- Função para medir distância ---
def obter_distancia():
    """
    Mede a distância em centímetros usando o sensor HC-SR04.
    Retorna None se não houver eco.
    """
    trig.value(0)
    time.sleep_us(2)
    trig.value(1)
    time.sleep_us(10)
    trig.value(0)

    duracao = time_pulse_us(echo, 1, 30000)  # timeout 30ms
    if duracao < 0:
        return None
    distancia = (duracao / 2) * 0.0343  # velocidade do som em cm/us
    return distancia

print("Sistema de contagem iniciado!")
print("Aguardando frascos...")

# --- Loop Principal ---
while True:
    dist = obter_distancia()

    if dist is not None:
        objeto_presente = dist <= DIST_THRESH_CM
    else:
        objeto_presente = False

    agora_ms = time.ticks_ms()

    # Detecta borda de subida (livre -> objeto presente)
    if (not estado_presenca) and objeto_presente:
        if time.ticks_diff(agora_ms, ultimo_pulso_ms) > MIN_GAP_MS:
            itens += 1
            ultimo_pulso_ms = agora_ms
            print(f"Item detectado! Total de itens: {itens}")

            # Verifica se completou caixa
            if itens % 10 == 0:
                caixas += 1
                print(f"Caixa completada! Total de caixas: {caixas}")
                # Pisca LED 2x para indicar
                for _ in range(2):
                    led_caixa.value(1)
                    time.sleep(0.5)
                    led_caixa.value(0)
                    time.sleep(0.3)

    estado_presenca = objeto_presente
    time.sleep_ms(50)  # taxa de leitura ~20 Hz
