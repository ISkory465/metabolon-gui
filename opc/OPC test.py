
from asyncio.windows_events import NULL
from multiprocessing.sharedctypes import Value
# import OpenOPC.OpenOPC as opc1
import OpenOPC as opc1
import time

import pywintypes
from OPC_Connection import OPC_Client
import json
pywintypes.datetime = pywintypes.TimeType
with open('opc\opcList.JSON') as json_file:
    data = json.load(json_file)
 
    # for reading nested data [0] represents
    # the index value of the list
    #print(data['TAB1'])
    print(type(data['TAB1']))
    x=data['TAB1']
    mykeys = [*x]          #list of keys    y=x.keys()
    k=mykeys[8]
    st="Temp. Fer 1 (\N{DEGREE SIGN}C)"
    print(k)
    print(st)
    if k==st:
      print('yes')
    #print(x['Temp. Fer 1 (°C)'])
    #print('\N{DEGREE SIGN} C')

# OPC connection
client1=OpenOPC.client()
list1=client1.servers()

#print(list1)
#name=list1[3]
#print(name)
#client1.connect(name)
#x=client1['Ack_All']
#tag='Ack_All'
#print(x)
#client1.write((tag,False))
#print(type(list1[5]))
# client1.start_connection(list1[5])
# d=client1.getInfo()


# print(d)
# serverName=d['OPC Server']
# print(serverName)
# list2=client1.listValues()

# print(list2)
# list3=client1.listValues2(list2[0])
# print(list3)
# list4=client1.listValues2(list2[0]+'.'+list3[1])
# print(list4)

# val=client1.R(list4[5])
# print(val)
# client1.close_connection()

'''


