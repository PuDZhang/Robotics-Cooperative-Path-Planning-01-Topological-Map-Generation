import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import scipy
import math
from scipy.misc import imsave

#im=Image.open('demo.jpg')
img=np.array(Image.open('park.png').convert('L'))
#img=np.array(Image.open('test2.png').convert('L'))

def distance(freepoint,occpoint):
	result = (freepoint[0]-occpoint[0])**2 + (freepoint[1]-occpoint[1])**2
	return math.sqrt(result)

def angle(freepoint,occpoint_1,occpoint_2):
	delta_y1 = occpoint_1[1]-freepoint[1]
	delta_x1 = occpoint_1[0]-freepoint[0]
	angel_1 = (math.atan2(delta_y1,delta_x1))*180/np.pi
	delta_y2 = occpoint_2[1]-freepoint[1]
	delta_x2 = occpoint_2[0]-freepoint[0]	
	angel_2 = (math.atan2(delta_y2,delta_x2))*180/np.pi
	delta_angel = abs(angel_1 - angel_2)
	#print angel_1
	#print angel_2
	if(delta_angel>=0 and delta_angel<=180):
		return delta_angel
	else:
		return 360.0 - delta_angel


CLOSE_DISTANCE = 11
max_angle=15
#max_angle_for_too_close_pt=91
rows,cols=img.shape
print img.shape
occupancy = []
free=[]
#print occupancy
index=0
for i in range(rows):
    for j in range(cols):
        if (img[i,j]>=128):
            img[i,j]=255				#255 is white
            free.append([i,j])
            #print [i,j]
        else:
            img[i,j]=0

for i in range(1,rows-1):
	for j in range(1,cols-1):
		if img[i,j]==0:
			#if(img[i-1,j]==255 or img[i+1,j]==255 or img[i,j-1]==255 or img[i,j+1]==255 or img[i+1,j+1]==255 or img[i+1,j-1]==255 or img[i-1,j+1]==255 or img[i-1,j-1]==255):
			if(img[i-1,j]==255 or img[i+1,j]==255 or img[i,j-1]==255 or img[i,j+1]==255):
				occupancy.append([i,j])



print "occupancy"
print len(occupancy)
print "free"
print len(free)


vo = []
minset = []
dis = []
min_dis_points_set = []

#print vo
for freepoint in free:
#for freepoint in range(0,1):
	#freepoint=[104,153]
	min = 1000000
	#flag = 0
	#minx=-1000000
	#miny=-1000000
	#minset= []
	min_dis_points_set = []
	too_close = 0
	for occpoint in occupancy:
		#vo.append(freepoint)
		dis.append(occpoint)
		dis.append(distance(occpoint,freepoint))	
		'''if(distance(occpoint,freepoint)<5):
			too_close = 1
			break'''

		MIN_DIS_BUFFER = 1.1
		if((abs(distance(occpoint,freepoint)-min))<MIN_DIS_BUFFER):
		#if((abs(distance(occpoint,freepoint)-min))<0.1):
			#flag = flag + 1
			#print min
			#print distance(occpoint,freepoint)
			min_dis_points_set.append(occpoint)
			#minset.append(occpoint)
			#dis.append(distance(occpoint,freepoint))
			#dis.append(occpoint)
			#print min
			#miny = occpoint[0]
			#minx = occpoint[1]
			#print occpoint

		if(distance(occpoint,freepoint)<min-MIN_DIS_BUFFER):
			min = distance(occpoint,freepoint)
			#flag = 0
			#miny = occpoint[0]
			#minx = occpoint[1]
			#minset= []
			minset.append(occpoint)
			#dis.append("0000000000000000000")
			#dis.append(distance(occpoint,freepoint))
			#dis.append(occpoint)
			min_dis_points_set=[]
			min_dis_points_set.append(occpoint)
	#print min_dis_points_set
	if(len(min_dis_points_set)>1):
		gather_points_set = []
		gather_points_set.append(min_dis_points_set[0])
		min_dis_points_set[0] = [-10,-10]
		index_i = 0
		while(index_i<len(gather_points_set)):
			for index_j in range(0,len(min_dis_points_set)):
				if (min_dis_points_set[index_j]!=[-10,-10]):

					'''print gather_points_set
					print min_dis_points_set
					print index_i
					print gather_points_set[index_i]
					print len(gather_points_set)
					print index_j
					print min_dis_points_set[index_j]
					print len(min_dis_points_set)
					print " "'''
					angle_value = angle(freepoint,gather_points_set[index_i],min_dis_points_set[index_j])
					#print min_dis
					#print gather_points_set[index_i]
					#print min_dis_points_set[index_j]
					if(angle_value<max_angle or distance(gather_points_set[index_i],min_dis_points_set[index_j])<= CLOSE_DISTANCE):	
						#print gather_points_set[index_i]
						#print min_dis_points_set[index_j]
						gather_points_set.append(min_dis_points_set[index_j])
						min_dis_points_set[index_j]=[-10,-10]
						#print gather_points_set				
						#min_dis_points_set[index_j]=[-10,-10]
					'''if(angle_value<max_angle_for_too_close_pt ):
						gather_points_set.append(min_dis_points_set[index_j])
						min_dis_points_set[index_j]=[-10,-10]'''
			index_i = index_i + 1
		#print index_i
		if(len(gather_points_set)<len(min_dis_points_set)):
			vo.append(freepoint)
			'''
			print freepoint
			print "gather_points_set"
			print gather_points_set[0]
			print "min_dis_points_set"
			print min_dis_points_set
			print " "
			'''
			#print min_dis_points_set[index_j][0]
			#print " " 
	#if(flag>0):
		#vo.append(freepoint)
		#print minset
		#print freepoint
		#print flagi
		#dis.append(freepoint)
		#dis.append("    ")
		#print dis
	#dis=[]
#print dis
#print vo
print "minset"
print len(minset)

occupancy_img = np.array(Image.open('park.png').convert('L'))
#occupancy_img = np.array(Image.open('test2.png').convert('L'))


occ_rows,occ_cols=occupancy_img.shape
for i in range(occ_rows):
    for j in range(occ_cols):
        occupancy_img[i,j]=255

for i in vo:
	occupancy_img[i[0],i[1]]=0
for i in occupancy:
	occupancy_img[i[0],i[1]]=0
# for i in min_dis_points_set:
# 	occupancy_img[i[0],i[1]]=0
occupancy_img[53,132]=0



plt.figure("lena")
plt.imshow(occupancy_img,cmap='gray')
plt.axis('off')
plt.savefig("voronoi.png",dpi=800)
plt.show()

