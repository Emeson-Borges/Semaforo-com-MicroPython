from machine import Pin
from time import sleep

# Configuração dos pinos dos LEDs
led_vermelho = Pin(25, Pin.OUT)
led_amarelo = Pin(26, Pin.OUT)
led_verde = Pin(27, Pin.OUT)

# Função para controlar o ciclo do semáforo
def semaforo():
    while True:
        # Verde aceso
        led_verde.value(1)
        led_amarelo.value(0)
        led_vermelho.value(0)
        sleep(5)  # Tempo do sinal verde

        # Amarelo aceso
        led_verde.value(0)
        led_amarelo.value(1)
        led_vermelho.value(0)
        sleep(2)  # Tempo do sinal amarelo

        # Vermelho aceso
        led_verde.value(0)
        led_amarelo.value(0)
        led_vermelho.value(1)
        sleep(5)  # Tempo do sinal vermelho

# Executa o ciclo do semáforo
semaforo()
