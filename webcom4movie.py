#coding: UTF-8
import sys
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
print(sys.path)


from PIL import Image,ImageDraw,ImageFont
import cv2
import subprocess
import time
import os
import threading

def capIm():

    cap= cv2.VideoCapture(-1)
    while True:

        if cap.isOpened() is False:
            print("cant open camera")
            #sys.exit()





        ret,frame=cap.read()
        cv2.imwrite('capturedImage.jpg',frame)



def judge_and_draw():
    cmd = "sh run2.sh"
    subprocess.call(cmd.split())

    try:
        res=subprocess.check_output(cmd.split())
    except:
        print("ERROR")

    response = res.decode("utf-8")


    if "class_2_images" in response:
        judge = "unconfortable"

    elif "class_1_images" in response:
        judge = "comfortable"

    else:
        print(response)
        judge = response


    img = Image.open("capturedImage.jpg")

    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("kokoro/Kokoro.otf",27)


    draw.text((10,10),judge,fill=(255,0,0),font=font)
    img.save("judge-result.jpg")


def showIm()
    cmd = "fbi judge-result.jpg -t 1 -1"
    p = subprocess.call(cmd.split())








def getsize():
    while True:
        print(os.path.getsize('capturedImage.jpg'))
        time.sleep(3)







if __name__=="__main__":
    th1 = threading.Thread(target = capIm)
    th2 = threading.Thread(target=getsize)
    th3 = threading.Thread(target=showIm)


    th1.start()
    th2.start()
    th3.start()
