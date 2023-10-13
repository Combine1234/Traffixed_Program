import RelayRasp
import time

def call1():
    RelayRasp.Len_1_Status_2()
    RelayRasp.Len_2_Status_1()
    time.sleep(1)
def call2():
    RelayRasp.Len_1_Status_1()
    RelayRasp.Len_2_Status_2()
    time.sleep(1)
def call3():
    RelayRasp.Len_2_Status_1()
    RelayRasp.Len_1_Status_2()
    time.sleep(1)