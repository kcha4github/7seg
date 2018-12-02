import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

# pin definition
CATHODE = [25, 24, 23, 22]
for c in CATHODE:
    GPIO.setup(c, GPIO.OUT)
    GPIO.output(c, GPIO.HIGH)

ANODE = [5,6,7,8,9,10,11,12]
for a in ANODE:
    GPIO.setup(a, GPIO.OUT)
    GPIO.output(a, GPIO.LOW)

DIGIT = [[GPIO.HIGH,GPIO.HIGH,GPIO.HIGH,GPIO.HIGH,GPIO.HIGH,GPIO.HIGH,GPIO.LOW ],#0
         [GPIO.LOW ,GPIO.HIGH,GPIO.HIGH,GPIO.LOW ,GPIO.LOW ,GPIO.LOW ,GPIO.LOW ],#1
         [GPIO.HIGH,GPIO.HIGH,GPIO.LOW ,GPIO.HIGH,GPIO.HIGH,GPIO.LOW ,GPIO.HIGH],#2
         [GPIO.HIGH,GPIO.HIGH,GPIO.HIGH,GPIO.HIGH,GPIO.LOW ,GPIO.LOW ,GPIO.HIGH],#3
         [GPIO.LOW ,GPIO.HIGH,GPIO.HIGH,GPIO.LOW ,GPIO.LOW ,GPIO.HIGH,GPIO.HIGH],#4
         [GPIO.HIGH,GPIO.LOW ,GPIO.HIGH,GPIO.HIGH,GPIO.LOW ,GPIO.HIGH,GPIO.HIGH],#5
         [GPIO.HIGH,GPIO.LOW ,GPIO.HIGH,GPIO.HIGH,GPIO.HIGH,GPIO.HIGH,GPIO.HIGH],#6
         [GPIO.HIGH,GPIO.HIGH,GPIO.HIGH,GPIO.LOW ,GPIO.LOW ,GPIO.LOW ,GPIO.LOW ],#7
         [GPIO.HIGH,GPIO.HIGH,GPIO.HIGH,GPIO.HIGH,GPIO.HIGH,GPIO.HIGH,GPIO.HIGH],#8
         [GPIO.HIGH,GPIO.HIGH,GPIO.HIGH,GPIO.HIGH,GPIO.LOW ,GPIO.HIGH,GPIO.HIGH]]#9
DISPLAY = 0
TIME_SPEND = 0
SLEEP_LEN = 0.0005

try:
    while True:
        if TIME_SPEND >= 0.5:
            DISPLAY = ((DISPLAY * 10) + ((DISPLAY + 1) % 10)) % 10000
            TIME_SPEND = 0
        
        v = DISPLAY // 1000
        GPIO.output(CATHODE[3], GPIO.LOW)
        GPIO.output(CATHODE[2], GPIO.HIGH)
        GPIO.output(CATHODE[1], GPIO.HIGH)
        GPIO.output(CATHODE[0], GPIO.HIGH)
        for i in range(0,7):
            GPIO.output(ANODE[i], DIGIT[v][i])
        sleep(SLEEP_LEN)
        TIME_SPEND += SLEEP_LEN
        
        v = (DISPLAY % 1000) // 100
        GPIO.output(CATHODE[3], GPIO.HIGH)
        GPIO.output(CATHODE[2], GPIO.LOW)
        GPIO.output(CATHODE[1], GPIO.HIGH)
        GPIO.output(CATHODE[0], GPIO.HIGH)
        for i in range(0,7):
            GPIO.output(ANODE[i], DIGIT[v][i])
        sleep(SLEEP_LEN)
        TIME_SPEND += SLEEP_LEN
        
        v = (DISPLAY % 100) // 10
        GPIO.output(CATHODE[3], GPIO.HIGH)
        GPIO.output(CATHODE[2], GPIO.HIGH)
        GPIO.output(CATHODE[1], GPIO.LOW)
        GPIO.output(CATHODE[0], GPIO.HIGH)
        for i in range(0,7):
            GPIO.output(ANODE[i], DIGIT[v][i])
        sleep(SLEEP_LEN)
        TIME_SPEND += SLEEP_LEN
        
        v = DISPLAY % 10
        GPIO.output(CATHODE[3], GPIO.HIGH)
        GPIO.output(CATHODE[2], GPIO.HIGH)
        GPIO.output(CATHODE[1], GPIO.HIGH)
        GPIO.output(CATHODE[0], GPIO.LOW)
        for i in range(0,7):
            GPIO.output(ANODE[i], DIGIT[v][i])
        sleep(SLEEP_LEN)
        TIME_SPEND += SLEEP_LEN
        
except KeyboardInterrupt:
    pass

GPIO.cleanup()
