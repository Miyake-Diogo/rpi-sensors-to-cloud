# Programa simples para testar os sensores

# Importa as bibliotecas
import time
import board
import adafruit_dht
# from board import D18

# Inicialização do dispositivo no pino:
dht_device = adafruit_dht.DHT11(board.D18)
#Para ler do  DHT22
#dht_device = adafruit_dht.DHT22(<pin>)

while True:
    try:
        # Para ler a Temperatura
        temperatura = dht_device.temperature
        # Para ler a umidade
        humidade = dht_device.humidity
        print(f"Temperatura:  {temperatura, :.1f} C    Humididate: {humidade}% ")

    except RuntimeError as error:
        # Se aparecer erros
        print(error.args[0])

    time.sleep(5.0)
