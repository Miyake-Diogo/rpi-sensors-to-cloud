# https://www.youtube.com/watch?v=Tw0mG4YtsZk
from gpiozero import LED
from gpiozero import MotionSensor
from datetime import datetime

green_led = LED(17)
pir = MotionSensor(4)
green_led.off()

dateTimeObj = datetime.now()
timestampStr = dateTimeObj.strftime("%Y-%b-%d (%H:%M:%S.%f)")
while True:
    pir.wait_for_motion()
    dateTimeObj = datetime.now()
    timestampStr = dateTimeObj.strftime("%Y-%b-%d (%H:%M:%S.%f)")
    print(f"Motion Detected at {timestampStr}")
    green_led.on()
    pir.wait_for_motion()
    green_led.off()
    dateTimeObj = datetime.now()
    timestampStr2 = dateTimeObj.strftime("%Y-%b-%d (%H:%M:%S.%f)")
    print(f"Motion Stoped at {timestampStr2}")

