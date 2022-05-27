import cv2
import requests
import numpy as np
import unittest

url="https://i.imgur.com/hE68qlT.jpeg"

def getImage(url):
    result=requests.get(url)
    ### btye string解析
    imgstring = np.array(result.content).tobytes()
    imgstring = np.asarray(bytearray(imgstring), dtype="uint8")
    img= cv2.imdecode(imgstring, cv2.IMREAD_COLOR)
   
    img=cv2.resize(img,(600,int(img.shape[0]*600/img.shape[1]))) #調整照片比例
    img=cv2.flip(img,0) #沿x軸翻轉
    img=cv2.flip(img,1) #沿y軸翻轉
    return img


cv2.imshow("show",getImage(url))
cv2.waitKey(0)
#cv2.imwrite(".\image.jpg",getImage(url)) #使用這行可存取照片


### automated test
class test(unittest.TestCase):
    def test_getImage(self):
        self.assertIsInstance(getImage(url),np.ndarray) ###確認是否為numpy array

if __name__=="__main__":
    unittest.main()

##img link
# https://images.unsplash.com/photo-1631086459990-06bc4d7ad6cf
# https://i.imgur.com/hE68qlT.jpeg
# https://effigis.com/wp-content/uploads/2015/02/Airbus_Pleiades_50cm_8bit_RGB_Yogyakarta.jpg

