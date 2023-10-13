#call the data to used 
import time

import pyodbc
import database
import RelayRasp
import Function_Call_Relay

x = 1
car_count_len_1 = 0
car_count_len_2 = 0
timesave1 = 0
timesave2 = 0
Len1 = 0
Len2 = 0
shit1 = 0
shit2 = 0

start_time = time.time()

GetConn = database.GetConn()
conn = pyodbc.connect(GetConn)
print(conn)

cursor =  conn.cursor()

for row in cursor.execute("select ID_Len, Car_Count, Relay_Status from Taffixed_1 WHERE ID_Len = 1"):
    car_count_len_1 = row.Car_Count
    #print(car_count_len_1)
    #print(row.ID_Len, "|" , row.Car_Count , "|" , row.Relay_Status)
for row in cursor.execute("select ID_Len, Car_Count, Relay_Status from Taffixed_1 WHERE ID_Len = 2 "):
    car_count_len_2 = row.Car_Count
    #print(car_count_len_2)

if car_count_len_2 > car_count_len_1:
    Len2 = 1
    timesave1 = 1
    RelayRasp.Len_1_Status_LED()
    RelayRasp.Len_2_Status_GREEN()
    time.sleep(3)

    while x < 5:
        time.sleep(1)
        for row in cursor.execute("select ID_Len, Car_Count, Relay_Status from Taffixed_1 WHERE ID_Len = 1"):
            car_count_len_1 = row.Car_Count
            #print(car_count_len_1)
            #print(row.ID_Len, "|" , row.Car_Count , "|" , row.Relay_Status)
        for row in cursor.execute("select ID_Len, Car_Count, Relay_Status from Taffixed_1 WHERE ID_Len = 2 "):
            car_count_len_2 = row.Car_Count
            #print(car_count_len_2)
    
        if car_count_len_2 > car_count_len_1:
            #print("Fuck")
            timesave2 = 0
            if timesave1 == 0:
                Function_Call_Relay.call_1()
                timesave1 = 1
        else:
            timesave1 = 0
            if timesave2 == 0:
                Function_Call_Relay.call_2()
                timesave1 = 1
else:
    timesave1 = 0
    Len1 = 1
    RelayRasp.Len_1_Status_GREEN()
    RelayRasp.Len_2_Status_LED()
    time.sleep(3)
    
    while x < 5:
        time.sleep(1)
        for row in cursor.execute("select ID_Len, Car_Count, Relay_Status from Taffixed_1 WHERE ID_Len = 1"):
            car_count_len_1 = row.Car_Count
            #print(car_count_len_1)
            #print(row.ID_Len, "|" , row.Car_Count , "|" , row.Relay_Status)
        for row in cursor.execute("select ID_Len, Car_Count, Relay_Status from Taffixed_1 WHERE ID_Len = 2 "):
            car_count_len_2 = row.Car_Count
            #print(car_count_len_2)
    
        if car_count_len_2 > car_count_len_1:
            #print("Fuck")
            timesave2 = 0
            if timesave1 == 0:
                Function_Call_Relay.call_1()
                timesave1 = 1
        else:
            timesave1 = 0
            if timesave2 == 0:
                Function_Call_Relay.call_2()
                timesave1 = 1


