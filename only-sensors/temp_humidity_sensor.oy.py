# retornar dados de temperatura e umidade
import Adafruit_DHT
import time

sensor = Adafruit_DHT.DHT11
DHT_READ_TIMEOUT = 5
DHT_DATA_PIN = 27

humidity, temperature = Adafruit_DHT.read_retry(sensor, DHT_DATA_PIN)
while True:
	if humidity is not None and temperature is not None:
		print('Temperature={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
	else:
		print('Failed to get reading from the sensor. Try again!')
	time.sleep(DHT_READ_TIMEOUT)
