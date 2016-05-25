# Raspberry real-time video (In the Internet monitoring)

---

Environment of software and hardware as follow:
> * Ubuntu Linux
> * Python2.7
> * Raspberry Pi 2B
> * Microsoft  LifeCam HD-5000 Camera (other camera is ok)

The softwares or api needed as follow：

> * SimpleCV
> * UV4L
> * Paho-Mqtt Client

## [SimpleCV](http://tutorial.simplecv.org/en/latest/)

A simple example can be found from [http://softwarerecs.stackexchange.com/questions/18134/python-library-for-taking-camera-images](http://softwarerecs.stackexchange.com/questions/18134/python-library-for-taking-camera-images) . Meanwhile, a tutorial can be found from [http://tutorial.simplecv.org/en/latest/](http://tutorial.simplecv.org/en/latest/)

Type this command in terminal:
```shell
$ sudo apt-get install python-opencv
```
Python test code:
```python
from SimpleCV import Camera

cam=Camera() #This statement maybe encounter a warning,but don't worry
img=cam.getImage()
img.save("implecv.png")
```
## [UV4L](http://www.linux-projects.org/modules/sections/index.php?op=viewarticle&artid=14)

If you can run the python code as above successfully, you can ignore this chapter.
If you encounter an **WARNING**: SimpleCV can't seem to find a camera on your system, or the drivers do not work with SimpleCV. You can read this page : [https://www.raspberrypi.org/forums/viewtopic.php?t=57788](https://www.raspberrypi.org/forums/viewtopic.php?t=57788). It will tell you to install the UV4L. 
The steps of installing the UV4L as follow:
>1. Type this command in terminal:
    ```$ curl http://www.linux-projects.org/listing/uv4l_repo/lrkey.asc | sudo apt-key add -```
>2. Add the following line to the file /etc/apt/sources.list
    ```deb http://www.linux-projects.org/listing/uv4l_repo/raspbian/ wheezy main```
>3. Type those command in terminal:
    ```$ sudo apt-get update```
    ```$ sudo apt-get install uv4l uv4l-raspicam```
    ```$ sudo apt-get install uv4l-raspicam-extras```
    ```$ sudo service uv4l_raspicam restart```
    ```$ uv4l --driver raspicam --auto-video_nr --width 640 --height 480 --encoding jpeg```

The UV4L official website is : [http://www.linux-projects.org/modules/sections/index.php?op=viewarticle&artid=14](http://www.linux-projects.org/modules/sections/index.php?op=viewarticle&artid=14) . You can get a tutorial in more detail.

##[Paho-Mqtt Client](https://eclipse.org/paho/clients/python/docs/#installation)
The Paho-Mqtt official is : [https://eclipse.org/paho/clients/python/docs/#installation](https://eclipse.org/paho/clients/python/docs/#installation). If you want to get more information, you should read this to be patient.

Install paho-mqtt by pip :
```$pip install paho-mqtt```
Detailed code can see the file named **send.py**

Author [@Ganze][1]     
05-25-2016    

[1]: https://github.com/Pterosaur
