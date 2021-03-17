
import cv2 # importando o openCV
import numpy as np
from pyzbar.pyzbar import decode # importando biblioteca de decodificacao de qrCode

# capturando a imagem 
#img = cv2.imread('qrcode.png')

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

takeFoto = True

while True:
    
    success, img = cap.read()

    for barcode in decode(img):
        myData = barcode.data.decode('utf-8')
        print(myData)
        pts = np.array([barcode.polygon], np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(img, [pts], True, (0,255,0),5)
        pts2 = barcode.rect
        cv2.putText(img, myData,(pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.9,(255,0,255), 2)

        if takeFoto:
            cv2.imwrite("teste.png", img)
            takeFoto = False
    
        
    cv2.imshow('Result', img)
    cv2.waitKey(1)
    
# import qrtools

# qr = qrtools.QR()

# qr.decode('qrcode.png')

# print(qr.data)