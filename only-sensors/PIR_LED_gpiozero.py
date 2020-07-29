
from gpiozero import LED
from gpiozero import MotionSensor

green_led = LED(17)
pir = MotionSensor(4)
green_led.off()

while True:
    pir.wait_for_motion()
    print("Motion Detected")
    green_led.on()
    pir.wait_for_motion()
    green_led.off()
    print("Motion Stoped")