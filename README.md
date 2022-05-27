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
Put your url string to getImage( )

       cv2.imshow("show",getImage(url))
       cv2.waitKey(0)
You can see the image flipped by the getImage( )     
![圖片](https://github.com/EricLin0619/Coding_test/blob/main/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%202022-05-27%20141603.png?raw=true "")     
### Automated test
To test whether the result from getImage( ) is numpy array.

       class test(unittest.TestCase):
           def test_getImage(self):
               self.assertIsInstance(getImage(url),np.ndarray) ###確認是否為numpy array

       if __name__=="__main__":
           unittest.main()
        
test result:
![圖片](https://github.com/EricLin0619/Coding_test/blob/main/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%202022-05-27%20142147.png?raw=true "")  



