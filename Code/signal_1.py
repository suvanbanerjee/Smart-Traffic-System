import cv2,os
import pandas as pd
from ultralytics import YOLO
from tracker import*
from ftplib import FTP
import time


# FTP server details
ftp_host = '192.168.214.74'
ftp_port = 2221
ftp_user = 'admin'
ftp_password = 'admin'

#Connect to FTP server
ftp = FTP()
ftp.connect(ftp_host, ftp_port)
ftp.login(ftp_user, ftp_password)

model=YOLO('yolov8s.pt')
def RGB(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE :  
        colorsBGR = [x, y]
cv2.namedWindow('RGB')
cv2.setMouseCallback('RGB', RGB)
cap=cv2.VideoCapture("veh2_.mp4")
my_file = open("coco.txt", "r")
data = my_file.read()
class_list = data.split("\n") 
count=0
tracker=Tracker()
cy1=0
cy2=0

offset=6


while True:   
    ret,frame = cap.read()
    if not ret:
        break
    count += 1
    if count % 3 != 0:
        continue
    frame=cv2.resize(frame,(360,480))
    results=model.predict(frame)
    a=results[0].boxes.data
    px=pd.DataFrame(a).astype("float")
    list=[]   
    for index,row in px.iterrows():
        x1=int(row[0])
        y1=int(row[1])
        x2=int(row[2])
        y2=int(row[3])
        d=int(row[5])
        c=class_list[d]
        if 'car' or 'bus' or 'motorcycle' or 'truck' in c:
            list.append([x1,y1,x2,y2])
        os.system('cls')
    bbox_id=tracker.update(list)
    for bbox in bbox_id:
        x3,y3,x4,y4,id=bbox
        cx=int((x3+x4)//2)+2
        cy=int((y3+y4)//2)+2
        cv2.circle(frame,(cx,cy),4,(0,0,255),-1)
        cv2.putText(frame,str("Vehicle"),(cx,cy),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,255),2)
    density=len(list)

    file_content = str(density)
    file_log = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + " " + str(density) + "\n"
    with open('signal_1.txt', 'wb') as local_file:
        local_file.write(file_content.encode('utf-8'))
    with open('signal_1.txt', 'rb') as local_file:
        ftp.storbinary('STOR signal_1.txt', local_file)
    with open('signal_1_log.txt', 'ab') as local_file2:
        local_file2.write(file_log.encode('utf-8'))
    with open('signal_1_log.txt', 'rb') as local_file2:
        ftp.storbinary('STOR signal_1_log.txt', local_file2)

    cv2.imshow("RGB", frame)
    if cv2.waitKey(1)&0xFF==27:
        break
ftp.quit()
cap.release()
cv2.destroyAllWindows()