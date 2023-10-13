import RPi.GPIO as GPIO
import time

start_time = time.time()

GPIO.setmode(GPIO.BCM) # GPIO Numbers instead of board numbers
GPIO.setwarnings(False)
#set Light 1
GPIO.setup(17, GPIO.OUT) 
GPIO.setup(27, GPIO.OUT) 
GPIO.setup(22, GPIO.OUT) 
#set Light 2
GPIO.setup(23, GPIO.OUT) 
GPIO.setup(24, GPIO.OUT) 
GPIO.setup(25, GPIO.OUT) 

def Len_1_Status_LED():
    GPIO.output(17, GPIO.LOW) # on
    GPIO.output(27, GPIO.HIGH) # off
    GPIO.output(22, GPIO.HIGH) # off

def Len_2_Status_LED():
    GPIO.output(23, GPIO.LOW) # on
    GPIO.output(24, GPIO.HIGH) # off
    GPIO.output(25, GPIO.HIGH) # off

def Len_1_Status_GREEN():
    GPIO.output(17, GPIO.HIGH) # off
    GPIO.output(27, GPIO.HIGH) # off
    GPIO.output(22, GPIO.LOW) # on

def Len_2_Status_GREEN():
    GPIO.output(23, GPIO.HIGH) # off
    GPIO.output(24, GPIO.HIGH) # off
    GPIO.output(25, GPIO.LOW) # on

def Len_1_Status_1():
    GPIO.output(17, GPIO.LOW) # on
    time.sleep(1)
    GPIO.output(17, GPIO.HIGH) # off
    GPIO.output(27, GPIO.LOW) # on
    time.sleep(2)
    GPIO.output(27, GPIO.HIGH) # off
    GPIO.output(22, GPIO.LOW) # on

def Len_1_Status_2():
    GPIO.output(22, GPIO.LOW) # on
    time.sleep(1)
    GPIO.output(22, GPIO.HIGH) # off
    GPIO.output(27, GPIO.LOW) # on
    time.sleep(2)
    GPIO.output(27, GPIO.HIGH) # off
    GPIO.output(17, GPIO.LOW) # on
    
def Len_2_Status_1():
    GPIO.output(23, GPIO.LOW) # on
    time.sleep(1)
    GPIO.output(23, GPIO.HIGH) # off
    GPIO.output(24, GPIO.LOW) # on
    time.sleep(2)
    GPIO.output(24, GPIO.HIGH) # off
    GPIO.output(25, GPIO.LOW) # on

def Len_2_Status_2():
    GPIO.output(25, GPIO.LOW) # on
    time.sleep(1)
    GPIO.output(25, GPIO.HIGH) # off
    GPIO.output(24, GPIO.LOW) # on
    time.sleep(2)
    GPIO.output(24, GPIO.HIGH) # off
    GPIO.output(23, GPIO.LOW) # on