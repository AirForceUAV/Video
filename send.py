from SimpleCV import Camera
cam=Camera()

import paho.mqtt.client as mqtt
mqttc=mqtt.Client()
mqttc.reinitialise(client_id="Camera",clean_session=True,userdata=None)
mqttc.connect("139.217.26.207",port=1883,keepalive=60,bind_address="")
#mqttc.connect("192.168.31.209",port=1883,keepalive=60,bind_address="")
mqttc.loop_start()

import StringIO

output=StringIO.StringIO()

import base64
import time,threading

def loop(sender):
	while True:
		mqttc.publish("Video","hello")
		time.sleep(1)

t1 = threading.Thread(target=loop,args=(mqttc,))
t1.start()

while True:
	print "world"
	time.sleep(5)
raw_input()

i = 0
#while True:
#img=cam.getImage()
#img.save(output)
#img.show()
#str=output.getvalue()
#mqttc.publish("Video",base64.b64encode(str))
#time.sleep(.05)
#print (i+len(str))


