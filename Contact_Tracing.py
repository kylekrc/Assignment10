# Program 10: Contact Tracing App

import cv2
import numpy as np
from pyzbar.pyzbar import decode
import datetime

def decoder(image):
    gray_img = cv2.cvtColor(image,0)
    barcode = decode(gray_img)

    for cap in barcode:
        barcodeData = cap.data.decode("utf-8")
        scan = "Scanned"
        
        points = cap.polygon
        (x,y,w,h) = cap.rect
        pts = np.array(points, np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(image, [pts], True, (0, 250, 0), 3)
        cv2.putText(frame, scan, (x,y), cv2.FONT_HERSHEY_SIMPLEX,0.9,(0,250,0), 2)
        print(f"{barcodeData}\n")

        Filetext_create = open("User_data.txt", "w")
        Filetext_create.write(f"{cap.data.decode('utf-8')}\n" )
              
        Date = datetime.datetime.now()
        Filetext_create.write(Date.strftime("\n\nDate: %Y/%m/%d \nTime: %H:%M:%S"))
        Filetext_create.close()
        print(f"Date & Time: {Date}\n\n")
        
capture = cv2.VideoCapture(0)
while True:
    ret, frame = capture.read()
    decoder(frame)
    cv2.imshow('Image Scanner', frame)
    code = cv2.waitKey(10)
    if code == ord('q'):
        break
    
    