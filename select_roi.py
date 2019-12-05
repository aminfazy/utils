
import cv2
import numpy as np
'''if __name__=='__main__':
	im=cv2.imread("ghat.jpg")
	r=cv2.selectROI("image",im)
	imCrop=im[int(r[1]):int(r[1]+r[3]),int(r[0]):int(r[0]+r[2])]
	cv2.startWindowThread()
	cv2.imshow("image",imCrop)
	cv2.waitKey(0)
	print(r)
'''

def ret_bbox(image):
	im=cv2.imread(image)
	r=cv2.selectROI("image",im)
	imCrop=im[int(r[1]):int(r[1]+r[3]),int(r[0]):int(r[0]+r[2])]
	cv2.startWindowThread()
	cv2.imshow("image",imCrop)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	#print(r)
	return r

def ret(image):
	x=ret_bbox(image)
	y=np.array(x)
	#print("this is changed module")
	return y

#ret_bbox("ghat.jpg")

