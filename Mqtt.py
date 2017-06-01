import paho.mqtt.client as mqtt
import json
import RPi.GPIO as io
io.setmode(io.BCM)

io.setup(17, io.IN, pull_up_down=io.PUD_UP)
io.setup(18, io.IN, pull_up_down=io.PUD_UP)
io.setup(27, io.IN, pull_up_down=io.PUD_UP)

io.add_event_detect(17, io.FALLING, bouncetime=200)
io.add_event_detect(18, io.FALLING, bouncetime=200)
io.add_event_detect(27, io.FALLING, bouncetime=200)

# tuplje object met pin nummers
leds = (9,10)

# initialisatie functie voor leds met als parameter een tuple
io.setmode(io.BCM)
io.setup(9, io.OUT)
io.setup(10, io.OUT)

#Booleans
led1 = False
led2 = False
led3 = False

# set state van de leds met als parameters 2 tuples
# tuple van pin nummers en een met bools van de state
def set_leds(leds, states):
 io.output(leds, states)

# calback voor het verwerken van de berichten
def on_message(mqttc, obj, msg):
# try:
  # payload omzetten van bytestring naar string
  #

  # json wordt verwacht json string moet omgezet worden naar een python
  #  dictonary voor verwerking
 # x = json.loads(p)
   
 if msg.payload.decode() == 'led1ON':  
  io.output(9,1)
 elif msg.payload.decode() == 'led1OFF':
  io.output(9,0)

 if msg.payload.decode() == 'led2ON':
  io.output(10,1)
 elif msg.payload.decode() == 'led2OFF':
  io.output(10,0)

 if msg.payload.decode() == 'ledsOFF':
  io.output(9,0)
  io.output(10,0)
 if msg.payload.decode() == 'ledsON':
  io.output(9,1)
  io.output(10,1)

 
 print(msg.topic)
 print(msg.payload.decode())

#def manual():
# global led1
# global led2
# global led3
# try:
#  mqttc = mqtt.Client()
#  mqttc.connect("broker.hivemq.com")
#  mqttc.connect("127.0.0.1")
#  while True:
#   if io.event_detected(17):
#    if led1 == False:
#     mqttc.publish('home/groundfloor/kitchen/lights/light1', payload='led1OFF', qos=0, retain=False)
#     led1 = True
#     print(led1)
#    elif led1 == True:
#     mqttc.publish('home/groundfloor/kitchen/lights/light1', payload='led1ON', qos=0, retain=False)
#     led1 = False
 
#   if io.event_detected(18):
#    if led2 == False: 
#     mqttc.publish('home/groundfloor/kitchen/lights/light2', payload='led2OFF', qos=0, retain=False)
#     led2 = True
#    elif led2 == True:
#     mqttc.publish('home/groundfloor/kitchen/lights/light2', payload='led2ON', qos=0, retain=False)
#     led2 = False

#   if io.event_detected(27):
#    if led3 == False:
#     mqttc.publish('home/groundfloor/kitchen', payload='ledsOFF', qos=0, retain=False)
#     led3 = True
#    elif led3 == True:
#     mqttc.publish('home/groundfloor/kitchen', payload='ledsON', qos=0, retain=False)
#     led3 = False
    
# except KeyboardInterrupt:
#  pass

def main():
 global led1
 global led2
 global led3
 try:
 # initialisatie van alle elementen
 # init_leds(leds)
  mqttc = mqtt.Client()
#  mqttc.subscribe('home/groundfloor/kitchen/lights/light1')
#  mqttc.subscribe('home/groundfloor/kitchen/lights/light2')

  mqttc.on_message = on_message
#  mqttc.connect("127.0.0.1")
  mqttc.connect("broker.hivemq.com")
  mqttc.subscribe('home/groundfloor/kitchen/#')
#  mqttc.subscribe('home/groundfloor/kitchen/lights/light2')

  while True:
        
   if io.event_detected(17):
    if led1 == False:
     mqttc.publish('home/groundfloor/livingroom', payload='led1OFF', qos=0, retain=False)
     led1 = True
    elif led1 == True:
     mqttc.publish('home/groundfloor/livingroom', payload='led1ON', qos=0, retain=False)
     led1 = False
 
   if io.event_detected(18):
    if led2 == False: 
     mqttc.publish('home/groundfloor/livingroom', payload='led2OFF', qos=0, retain=False)
     led2 = True
    elif led2 == True:
     mqttc.publish('home/groundfloor/livingroom', payload='led2ON', qos=0, retain=False)
     led2 = False

   if io.event_detected(27):
    if led3 == False:
     mqttc.publish('home/groundfloor/livingroom', payload='ledsOFF', qos=0, retain=False)
     led3 = True
    elif led3 == True:
     mqttc.publish('home/groundfloor/livingroom', payload='ledsON', qos=0, retain=False)
     led3 = False
    
   mqttc.loop()

 except KeyboardInterrupt:
   pass

 finally:
   io.cleanup()

# main segment
if __name__ == "__main__":
 main()

