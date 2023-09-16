from opcua import Server
import random
import uuid
import time

server = Server()

url = "opc.tcp://localhost:4840" 
server.set_endpoint(url)

name = "OPCUA_SERVER"
namespace = server.register_namespace(name)

node = server.get_objects_node()

Param = node.add_object('ns=2;s="Parameter"', "Parameters")

pressure = Param.add_variable('ns=2;s="Pressure_01"', "Pressure_01",0)
power = Param.add_variable('ns=2;s="Power_01"', "Power_01",0)
speed = Param.add_variable('ns=2;s="Speed_01"', "Speed_01",0)
gas_flow = Param.add_variable('ns=2;s="Gas_Flow_01"', "Gas_Flow_01",0)
vibration = Param.add_variable('ns=2;s="Vibration_01"', "Vibration_01",0)
pressure2 = Param.add_variable('ns=2;s="Pressure_02"', "Pressure_02",0)
vibration2 = Param.add_variable('ns=2;s="Vibration_02"', "Vibration_02",0)

cycleid = Param.add_variable('ns=2;s="cycleid"', "cycleid",0)
date = Param.add_variable('ns=2;s="date"', "date",0)
_time = Param.add_variable('ns=2;s="time"', "time",0)
combined = Param.add_variable('ns=2;s="combined"', "combined",0)
tstamp = Param.add_variable('ns=2;s="tstamp"', "tstamp",0)
key = Param.add_variable('ns=2;s="key"', "key",0)
ps1 = Param.add_variable('ns=2;s="ps1"', "ps1",0)
ps2 = Param.add_variable('ns=2;s="ps2"', "ps2",0)
ps3 = Param.add_variable('ns=2;s="ps3"', "ps3",0)
ps4 = Param.add_variable('ns=2;s="ps4"', "ps4",0)
ps5 = Param.add_variable('ns=2;s="ps5"', "ps5",0)
ps6 = Param.add_variable('ns=2;s="ps6"', "ps6",0)
eps1 = Param.add_variable('ns=2;s="eps1"', "eps1",0)
fs1 = Param.add_variable('ns=2;s="fs1"', "fs1",0)
fs2 = Param.add_variable('ns=2;s="fs2"', "fs2",0)
ts1 = Param.add_variable('ns=2;s="ts1"', "ts1",0)
ts2 = Param.add_variable('ns=2;s="ts2"', "ts2",0)
ts3 = Param.add_variable('ns=2;s="ts3"', "ts3",0)
ts4 = Param.add_variable('ns=2;s="ts4"', "ts4",0)
v1 = Param.add_variable('ns=2;s="v1"', "v1",0)
ce = Param.add_variable('ns=2;s="ce"', "ce",0)
cp = Param.add_variable('ns=2;s="cp"', "cp",0)
se = Param.add_variable('ns=2;s="se"', "se",0)
cooler_cond = Param.add_variable('ns=2;s="cooler_cond"', "cooler_cond",0)
valve_cond = Param.add_variable('ns=2;s="valve_cond"', "valve_cond",0)
pump_leak = Param.add_variable('ns=2;s="pump_leak"', "pump_leak",0)
hydrau_bar = Param.add_variable('ns=2;s="hydrau_bar"', "hydrau_bar",0)
stable = Param.add_variable('ns=2;s="stable"', "stable",0)

pressure.set_writable()
power.set_writable()
speed.set_writable()
gas_flow.set_writable()
vibration.set_writable()
pressure2.set_writable()
vibration2.set_writable()

cycleid.set_writable()
date.set_writable()
_time.set_writable()
combined.set_writable()
tstamp.set_writable()
key.set_writable()
ps1.set_writable()
ps2.set_writable()
ps3.set_writable()
ps4.set_writable()
ps5.set_writable()
ps6.set_writable()
eps1.set_writable()
fs1.set_writable()
fs2.set_writable()
ts1.set_writable()
ts2.set_writable()
ts3.set_writable()
ts4.set_writable()
v1.set_writable()
ce.set_writable()
cp.set_writable()
se.set_writable()
cooler_cond.set_writable()
valve_cond.set_writable()
pump_leak.set_writable()
hydrau_bar.set_writable()
stable.set_writable()

server.start()
print("OPC UA Server Started at ",format(url))

i = 0
j = 1

while  True:   
    
    parameter_1 = round(random.uniform(1010,1030), 6)
    parameter_2 = round(random.uniform(1730,1811), 6)
    parameter_3 = round(random.uniform(1010,1030), 7)
    parameter_4 = round(random.uniform(1951,2278), 6)
    parameter_5 = round(random.uniform(1.8,1.9), 9)
    parameter_6 = round(random.uniform(1600,1800), 6)
    parameter_7 = round(random.uniform(1.0,1.1), 9)
    
    pressure.set_value(parameter_1)
    power.set_value(parameter_2)
    speed.set_value(parameter_3)
    gas_flow.set_value(parameter_4)
    vibration.set_value(parameter_5)
    pressure2.set_value(parameter_6)
    vibration2.set_value(parameter_7)   
    
    i = i + 1        
    
    k = 0
    
    if(i == k + 60) :
        k = i
        j = j + 1
        
    parameter_01 = j   
    parameter_02 = '4/'+str(random.randint(1,30))+'/20'
    parameter_03 = str(random.randint(0,24)) +':'+str(random.randint(0,60)) +':'+ str(random.randint(0,60))
    parameter_04 = str(parameter_02) +' '+ str(parameter_03)
    parameter_05 = parameter_03
    parameter_06 = i
    parameter_07 = uuid.uuid4().hex
    parameter_08 = round(random.uniform(140,190),1)
    parameter_09 = round(random.uniform(2,140),1)
    parameter_10 = round(random.uniform(0,3),2)
    parameter_11 = round(random.uniform(0,11),2)
    parameter_12 = round(random.uniform(0,10),2)
    parameter_13 = round(random.uniform(8,9),2)
    parameter_14 = round(random.uniform(8,9),2)
    parameter_15 = round(random.uniform(2200,2400),2)
    parameter_16 = round(random.uniform(0,9),2)
    parameter_17 = round(random.uniform(35,55),3)
    parameter_18 = round(random.uniform(40,60),3)
    parameter_19 = round(random.uniform(0,10),2)
    parameter_20 = round(random.uniform(0,10),2)    
    parameter_21 = round(random.uniform(0,1),3)
    parameter_22 = round(random.uniform(19,47),3)
    parameter_23 = round(random.uniform(1.1,2.1),3)
    parameter_24 = round(random.uniform(1.1,2.11),3)    
    parameter_25 = random.randint(3,100)
    parameter_26 = random.randint(80,100)
    parameter_27 = random.randint(0,1)
    parameter_28 = random.randint(90,130)
    
    cycleid.set_value(parameter_01)
    date.set_value(parameter_02)
    _time.set_value(parameter_03)
    combined.set_value(parameter_04)
    tstamp.set_value(parameter_05)
    key.set_value(parameter_06)
    ps1.set_value(parameter_07)
    ps2.set_value(parameter_08)
    ps3.set_value(parameter_09)
    ps4.set_value(parameter_10)
    ps5.set_value(parameter_11)
    ps6.set_value(parameter_12)
    eps1.set_value(parameter_13)
    fs1.set_value(parameter_14)
    fs2.set_value(parameter_15)
    ts1.set_value(parameter_16)
    ts2.set_value(parameter_17)
    ts3.set_value(parameter_18)
    ts4.set_value(parameter_19)
    v1.set_value(parameter_20)
    ce.set_value(parameter_21)
    cp.set_value(parameter_22)
    se.set_value(parameter_23)
    cooler_cond.set_value(parameter_24)
    valve_cond.set_value(parameter_25)
    pump_leak.set_value(parameter_26)
    hydrau_bar.set_value(parameter_27)
    stable.set_value(parameter_28)
       
    time.sleep(5)