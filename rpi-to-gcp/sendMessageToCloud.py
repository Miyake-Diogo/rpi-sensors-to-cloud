from google.cloud import pubsub_v1
import datetime
import json
import sensorData
import time

project_id = "miyake-tech"  # Coloque aqui seu ID de projeto
topic_name = "my-topic"  # Entre com o nome do topico criado

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_name)

futures = dict()


def get_callback(f, data):
    def callback(f):
        try:
            # print(f.result())
            futures.pop(data)
        except:
            print("Por favor, verifique a exception: {} para : {}.".format(f.exception(), data))

    return callback


while True:
    time.sleep(3)
    # Aqui traremos os dados dos sensores
    movement = str(sensorData.FindMovement_v2())  # Dados de movimento
    temperature = round(float(sensorData.FindTemperature()), 2)  # Dados de temperatura
    humidity = round(float(sensorData.FindHumidity()), 2)  # Dados de humidade
    timenow = float(time.time())  # Dados de tempo
    data = {"timestamp": timenow,
            "movement": movement,
            "temperature": temperature,
            "humidity": humidity}
    print(data)
    # Quando a mensagem é publicada é retornada a variavel future.
    future = publisher.publish(
        topic_path, data=(json.dumps(data)).encode("utf-8"))  # Os dados devem ser um string de bytes.
    # As falhas de publicação devem ser tratadas na função de retorno de chamada.
    future.add_done_callback(get_callback(future, data))
    time.sleep(5)
# Aguarde a resolução de todos os futuros de publicação antes de sair.
while futures:
    time.sleep(5)

print("Mensagem publicada com erro.")
