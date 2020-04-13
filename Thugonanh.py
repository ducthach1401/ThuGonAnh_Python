import cv2
import os

path=os.getcwd()
path=path+'/BackGround/'
print (path)
for i in os.walk(path):
	print (i)
	for j in i[2]:
		name=j
		temp=path+name
		img=cv2.imread(temp)
		thaydoi=cv2.resize(src=img,dsize=(1920,1080))
		cv2.imwrite(temp,thaydoi)
		print('Done',name)
