from gpiozero import MotionSensor
from datetime import datetime
import time as t

pir = MotionSensor(4)

while True:
    if pir.wait_for_motion() == True:
        timenow = datetime.now().time()
        movimento = "Movimento Detectado "
        print("{} - {}".format(movimento, timenow))
    pir.wait_for_motion()
    print("SEM MOVIMENTOS")

# pir.wait_for_no_motion()
# timenow = datetime.now().time()
# print("Nenhum Movimento Detectado - {}".format(timenow))
# t.sleep(5)
