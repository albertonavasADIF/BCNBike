# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 16:58:36 2024

@author: alber
"""

import asyncio
import csv
import sys
import json
import time
import os
import paho.mqtt.client as paho


MAXLINESTOREAD = 100000
MAXSTATIONSTOPUBLISH = 500
broker="localhost"
port=1883


file ='2019_01_Gener_BICING_ESTACIONS.csv'
f = csv.reader(open(file, 'r',encoding='utf-8'),delimiter=',')
lineId = f.__next__()
data_file={}
data_file['totals']={}
numline = 0
    
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False



"""
populate dictinary of data_file from data in file 
"""

while numline < MAXLINESTOREAD:
    line= f.__next__()   
    data ={}  #dictinoary for data_line
    for index,indexId in enumerate(lineId):
        indexId = indexId.replace('\ufeff', '')
        data[indexId]=line[index]
    id = data['id']
    time_stamp = data['updateTime']
    if id not in data_file.keys():
        data_file[id]={}
    if time_stamp not in  data_file[id].keys():    
        data_file[id][time_stamp]={}
    if time_stamp not in data_file['totals'].keys():
        data_file['totals'][time_stamp]={'id':'totals','tBikes':0,'tSlots':0,'noBikes':0,'noSlots':0}
    for key,value in data.items(): 
        if is_number(value):
            if is_integer(value):
                data_file[id][time_stamp][key]=int(value)
            else:
                data_file[id][time_stamp][key]=float(value)
        else:
            data_file[id][time_stamp][key]=value

    if data_file[id][time_stamp]['bikes']==0:
        data_file['totals'][time_stamp]['noBikes']=data_file['totals'][time_stamp]['noBikes']+1
    
    if data_file[id][time_stamp]['slots']==0:
         data_file['totals'][time_stamp]['noSlots']=data_file['totals'][time_stamp]['noSlots']+1
    data_file['totals'][time_stamp]['tBikes']=data_file['totals'][time_stamp]['tBikes']+data_file[id][time_stamp]['bikes']

    data_file['totals'][time_stamp]['tSlots']=data_file['totals'][time_stamp]['tSlots']+data_file[id][time_stamp]['slots']

    numline = numline + 1

"""
function to execute the publisher for each Id in asyncronus mode
"""

def on_publish(client,userdata,result):         #create function for callback
    print("data published \n")
    pass


async def publish(station,file):
    print('station: ' + station + ' started')

    client1= paho.Client()                           #create client objec
    client1.on_publish = on_publish   
    while True:
        
        client1.connect(broker,port)              #establish connection
        fj = open(file,'r')
        d = json.load(fj)
        
        for timeStamp in d:
            ret= client1.publish("stations/"+station+"/readings",json.dumps(d[timeStamp]))
            await asyncio.sleep(10)

async def main():
    station = 1
    p_stations = 0
    publishers = []
    global MAXSTATIONSTOPUBLISH
    if (MAXSTATIONSTOPUBLISH > len(data_file.keys())-1):
        MAXSTATIONSTOPUBLISH=len(data_file.keys())-1
    while p_stations < MAXSTATIONSTOPUBLISH:
        file_name = './temp/aux' + str(station) + '.json'
        if str(station) in data_file.keys():
            r = json.dumps(data_file[str(station)])
            fj = open(file_name,'w')
            fj.write(r)
            fj.close()
        
            publishers.append(publish(str(station), file_name))
            p_stations = p_stations +1
        station = station + 1
        
    file_name = './temp/totals.json'
    r = json.dumps(data_file['totals'])
    fj = open(file_name,'w')
    fj.write(r)
    fj.close()

    publishers.append(publish('totals', file_name))    
    await asyncio.wait(publishers)


"""
Run the event loop to execute the asynchronous code
"""

if __name__ == "__main__":
    
    # Record the start time for measuring execution time
    #os.chdir('/Documentos/')
    start_time = time.time()

    # Run the main asynchronous function using asyncio.run()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    #asyncio.run(main())

    # Calculate and print the total execution time
    end_time = time.time()
    
    print(start_time)
    print(end_time)

