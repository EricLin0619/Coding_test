# Coding test
### Coding process
Package I used : requests、opencv、numpy   
1. First, use requests package to send the request to url that contains a img file.   
2. Second, use numpy to parse the byte string to numpy array that is a image data type.   
3. Finally, use opencv to flip the image and show the image.
It all the steps to complete this test.   
### How to use
If you want to try other image, just modify the url string.     
And you can save the image after comment out cv2.imwrite(".\image.jpg",getImage(url))   
### Example
'''
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
'''
