
from asyncio.windows_events import NULL
from multiprocessing.sharedctypes import Value
# import OpenOPC.OpenOPC as opc1
import OpenOPC 
# import OpenOPC.OpenOPC as opc1

import pywintypes
from OPC_Connection import OPC_Client
import json
pywintypes.datetime = pywintypes.TimeType
client=OpenOPC.client()
client.connect("OPC.SimaticNET")

client.write(('SIMATIC 300-Station.CPU 315-2 DP.DB5.HE12.BF2',False))
print('Done')

