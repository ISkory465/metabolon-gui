
from asyncio.windows_events import NULL
from multiprocessing.sharedctypes import Value
import OpenOPC
import time

import pywintypes
from OPC_Connection import OPC_Client

pywintypes.datetime = pywintypes.TimeType

# OPC connection
client1=OPC_Client()
list1=client1.servernames()

print(list1)
#print(type(list1[5]))
client1.start_connection(list1[5])
list2=client1.listValues()

print(list2)
list3=client1.listValues2(list2[0])
print(list3)
list4=client1.listValues2(list2[0]+'.'+list3[1])
print(list4)

val=client1.R(list4[5])
print(val)
client1.close_connection()




