import cv2
import numpy as np
kamera = cv2.VideoCapture(0)
while True:
  ret,gambar = kamera.read()
  if not ret:
    print('kamera tidak terdeteksi')
  nama = 'objek.jpg'
  cv2.imwrite(nama,gambar)
  img = cv2.imread(nama)
  img_copy = img.copy()
  img_hsv = cv2.cvtColor(img_copy,cv2.COLOR_BGR2HSV)
  lower_merah = np.array([0,150,100])
  upper_merah = np.array([10,255,255])
  maks = cv2.inRange(img_hsv,lower_merah,upper_merah)
  img_blur = cv2.GaussianBlur(maks,(5,5),0)
  _,thresh = cv2.threshold(img_blur,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)
  contours,hirarki = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
  jumlah = 0
  for cnt in contours:
    luas = cv2.contourArea(cnt)
    if luas > 500:
      jumlah +=1
      x,y,w,h = cv2.boundingRect(cnt)
      cv2.rectangle(img_copy,(x,y),(x+w,y+h),(0,0,255),2)
      cv2.putText(img_copy,'MERAH',(x,y-30),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)
      cv2.putText(img_copy,str(jumlah),(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)
  cv2.imshow('gambar mask', img_copy)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
kamera.release()
cv2.destroyAllWindows()

  
