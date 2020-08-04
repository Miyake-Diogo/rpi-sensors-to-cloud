# Funções para usar e retornar os dados necessários
from gpiozero import MotionSensor
import Adafruit_DHT
# from datetime import datetime
import time
import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)
gpio.setup(4, gpio.IN)

pir = MotionSensor(4)
sensor = Adafruit_DHT.DHT11
DHT_DATA_PIN = 27



def FindMovement_v2():
    time.sleep(2)
    if (gpio.input(4) == gpio.HIGH):
        movimento = "Movimento Detectado"
    else:
        movimento = "Nenhum Movimento Detectado"

    return movimento


def FindMovement():
    time.sleep(2)
    if (pir.wait_for_motion() == True):
        movimento = "Movimento Detectado"
    else:
        movimento = "Nenhum Movimento Detectado"

    return movimento


def FindTemperature():
    umidade, temperatura = Adafruit_DHT.read_retry(sensor, DHT_DATA_PIN)
    return temperatura


def FindHumidity():
    umidade, temperatura = Adafruit_DHT.read_retry(sensor, DHT_DATA_PIN)
    return umidade


