import cv2,os
import pandas as pd
from ultralytics import YOLO
from tracker import*
import time
from ftplib import FTP
import linker


# FTP server details
ftp_host = '192.168.214.74'
ftp_port = 2221
ftp_user = 'admin'
ftp_password = 'admin'

#Connect to FTP server
ftp = FTP()
ftp.connect(ftp_host, ftp_port)
ftp.login(ftp_user, ftp_password)


def case_3():
    pass

def case_2_1():
    signal_2.green(3)
def case_2_2():
    signal_1.green(3)

def case_1():
    if signal_1_density or signal_3_density > 1 or time_:


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
time_prev=time.time()

while True: 


    with open('signal_1.txt', 'r') as signal1:
         signal_1_density=str(signal1.read)
    with open('signal_2.txt', 'r') as signal2:
         signal_2_density=str(signal2.read)
    with open('signal_1.txt', 'r') as signal3:
         signal_3_density=str(signal3.read)


    ret,frame = cap.read()


    if not ret:
        break
    count += 1
    if count % 3 != 0:
        continue


    frame=cv2.resize(frame,(360,480))
    results=model.predict(frame)
    a=results[0].boxes.boxes
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
    
    time_delta = time.time() - time_prev
    print(len(list))

    if time_delta > 30:

        if (signal_1_density or signal_3_density > 20) and (signal_2_density or signal_4_density == 0 ):
            linker.All_off()
            linker.Signal_1_yellow_on()
            linker.Signal_2_yellow_on()
            linker.Signal_3_yellow_on()
            linker.Signal_4_yellow_on()
            time.sleep(3)
            linker.Signal_1_yellow_off()
            linker.Signal_2_yellow_off()
            linker.Signal_3_yellow_off()
            linker.Signal_4_yellow_off()

            linker.Signal_1_green_on()
            linker.Signal_2_red_on()
            linker.Signal_3_green_on()
            linker.Signal_4_red_on()

        elif (signal_2_density or signal_4_density > 20) and (signal_1_density or signal_3_density == 0 ):
            
            linker.All_off()
            linker.Signal_1_yellow_on()
            linker.Signal_2_yellow_on()
            linker.Signal_3_yellow_on()
            linker.Signal_4_yellow_on()
            time.sleep(3)
            linker.Signal_1_yellow_off()
            linker.Signal_2_yellow_off()
            linker.Signal_3_yellow_off()
            linker.Signal_4_yellow_off()
        
            linker.Signal_1_red_on()
            linker.Signal_2_green_on()
            linker.Signal_3_red_on()
            linker.Signal_4_green_on()


        elif (singal_2_density or signal_4_density < 2) and (signal_1_density or signal_3_density < 2 ):
            
            density based


        else:
            case_3()

    cv2.imshow("RGB", frame)
    if cv2.waitKey(1)&0xFF==27:
        break

cap.release()
cv2.destroyAllWindows()