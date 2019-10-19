import _thread as thread
import cv2
import urllib.request
import numpy as np
import time

list_of_ips = ['192.168.1.102:8080', '192.168.1.100:8080']

def ip_cam(name, ip):
    camera_port = "http://"+ip+"/shot.jpg"
    print("Accessing\t",camera_port)
    while ip:
        img_resp = urllib.request.urlopen(camera_port)
        img_np = np.array(bytearray(img_resp.read()), dtype=np.uint8)
        img = cv2.imdecode(img_np, -1)
        img = cv2.resize(img, (600, 600))
        cv2.imshow(ip, img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
length = len(list_of_ips)

try:
    for i in list_of_ips:
        t1 = thread.start_new_thread(ip_cam, ("Thread1", i, ))
        #t2 = thread.start_new_thread(ip_cam, ("Thread2", i, ))
except:
    print("[ERROR]")
