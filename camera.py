from SimpleCV import Camera
import paho.mqtt.client as mqtt
import StringIO
import base64
import time
import os

def CaptureImages() :
    #load mqtt service
    #videoClient = mqtt.Client()
    #videoClient.reinitialise(client_id = "Camera", clean_session = True, userdata = None)
    #videoClient.connect("139.217.26.207", port = 1883, keepalive = 60, bind_address = "")
    #videoClient.loop_start()

    #prepare the send buffer
    output = StringIO.StringIO()
    #capture the images
    camera = Camera()
    while True:
        image = camera.getImage()
        #image.save(output)
        image.save("hello.jpg")
        #videoClient.publish("Video", base64.b64decode(output.getvalue()))
        time.sleep(5)

class Recover(object):
    def __init__(self, pid) :
        self.pid = pid
    def __del__(self) :
        os.kill(self.pid, 9)

videoProcess = os.fork()
if videoProcess == 0 :
    CaptureImages()
    exit()

videoRecover = Recover(videoProcess)
if __name__ == "__main__" :
    time.sleep(60)

