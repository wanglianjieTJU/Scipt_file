import cv2
#The larger the kerner size and standard deviation, the more blurred the processed image
kernel_size=(5,5)
kernel_size1=(3,3)
kernel_size2=(7,7)
sigma=1.5
sigma1=3
sigma2=5
img=cv2.imread('G://vot//votseg_dataset//bag//00000000.png')
img1=cv2.GaussianBlur(img,kernel_size,sigma)
img2=cv2.GaussianBlur(img,kernel_size1,sigma1)
img3=cv2.GaussianBlur(img,kernel_size2,sigma2)

cv2.imwrite('G://gausstest1.png',img1)
cv2.imwrite('G://gausstest2.png',img2)
cv2.imwrite('G://gausstest3.png',img3)
cv2.waitKey (0)
cv2.destroyAllWindows()