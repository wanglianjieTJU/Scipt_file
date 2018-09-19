import cv2
import numpy as np
image = cv2.imread('G://vot//vot2016//bag//00000001.jpg', 0)
mask = cv2.imread('G://vot//votseg_dataset//bag//00000000.png', 0)
print('.......................')
mask = np.where(mask > 150, 255, np.where(mask < 100, 0, mask))
coef = 255 if np.max(image) < 3 else 1
image = (image * coef).astype(np.float32)
image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
image[..., 2] = np.where(mask == 255, 255, image[..., 2])
cv2.imwrite('G://test1.png', image)
