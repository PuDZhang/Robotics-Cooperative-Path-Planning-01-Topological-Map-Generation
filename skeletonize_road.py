from skimage import img_as_bool, io, color, morphology
import matplotlib.pyplot as plt
from skimage.morphology import medial_axis, skeletonize, skeletonize_3d
import numpy as np 
from PIL import Image
from skimage import segmentation
from scipy import ndimage as ndi
from skimage import morphology,feature

np.set_printoptions(threshold=np.inf)  

image = img_as_bool(color.rgb2gray(io.imread('road.png')))
out = skeletonize(image)

skel, distance =morphology.medial_axis(image, return_distance=True)
dist_on_skel = distance * skel


'''def find_critical_point(point):
	for i in {-1,0,1}:
		for j in {-1,0,1}:
			if(i!=0 and j!=0):
				if(occupancy_img[point[i],point[j]]==0)'''


#def Dijkstra(G,v0,INF=999):
def Dijkstra(src,goal,local_graph_dict,global_graph_dict):
	dis = 1
	path_list = []
    #path_list.append(initial)
	path_dis_dict = {}
	path_list_index = 0
	pre_dict = {}
	final_list = []
    #print goal
	for point in global_graph_dict[src]:
		#print point
		if local_graph_dict.has_key((point[0],point[1])) == True:
			path_list.append(point)
			path_dis_dict[(point[0],point[1])] = 0
			pre_dict[(point[0],point[1])] = src
	#print path_list
	while path_list_index<len(path_list):
		current_point = path_list[path_list_index]
		path_list_index = path_list_index + 1
		#print current_point
		if ((current_point[0],current_point[1]) == goal):
			print "zhaodaole"
			break
		if local_graph_dict.has_key((current_point[0],current_point[1])) == True:
			for consecutive_points_set in local_graph_dict[(current_point[0],current_point[1])]:
				for consecutive_point in consecutive_points_set:
					#print consecutive_point
					if path_dis_dict.has_key((consecutive_point[0], consecutive_point[1]))==False:
						#print consecutive_point
						dis = path_dis_dict[(current_point[0],current_point[1])]+1
						#print path_dis_dict[(current_point[0],current_point[1])]
						#print path_dis_dict(current_point[0],current_point[1]))
						#path_dis_dict.setdefault((consecutive_point[0], consecutive_point[1])).append(dis)
						path_dis_dict[(consecutive_point[0], consecutive_point[1])] = dis
						pre_dict[(consecutive_point[0], consecutive_point[1])] = (current_point[0],current_point[1])
						path_list.append(consecutive_point)
	#print dis
	#print path_dis_dict
	#dis_dict = {v:k for k,v in path_dis_dict.items()} 
	#print pre_dict
	current_point = goal
	while(current_point!=src):
		#print current_point
		if(current_point!=goal):
			final_list.append(current_point)
		current_point = pre_dict[current_point] 
	#print final_list
	return final_list
	#while path_dis > 1:


def remove_redundance(root,global_graph_dict,local_graph_dict):
	tree_second_hierarchy_dict = {}
	for first_hierarchy_point in global_graph_dict[(root[0],root[1])]:
		#print first_hierarchy_point
		#print graph_dict[(first_hierarchy_point[0],first_hierarchy_point[1])]
		#for second_hierarchy_point in graph_dict[(first_hierarchy_point[0],first_hierarchy_point[1])]:
			#print second_hierarchy_point
		tree_second_hierarchy_dict[(first_hierarchy_point[0],first_hierarchy_point[1])] = global_graph_dict[(first_hierarchy_point[0],first_hierarchy_point[1])]
	#print tree_second_hierarchy_dict
	#index = 0
	#while index < count:
	#print root,'root'
	#print tree_second_hierarchy_dict
	for i in tree_second_hierarchy_dict:
		#print i,"i"
		#print tree_second_hierarchy_dict[i]
		count = 0
		#if len(tree_second_hierarchy_dict[i])>1:
		for second_hierarchy_point in tree_second_hierarchy_dict[i]:
			#print tree_second_hierarchy_dict[i]
			for j in tree_second_hierarchy_dict:
				if i!=j:
					#if first_hierarchy_point[0]!=root[0] and first_hierarchy_point[1]!=root[1]:
					if second_hierarchy_point in tree_second_hierarchy_dict[j]: 
						count = count + 1 
						break
		if count == len(tree_second_hierarchy_dict[i]):
			print "remove",i
			#print " "
			for point in global_graph_dict[i]:
				global_graph_dict[(point[0],point[1])].remove([i[0],i[1]])
			global_graph_dict.pop(i)
			if local_graph_dict.has_key(i)==True:
				local_graph_dict.pop(i)
			if 	[i[0],i[1]] in triple_node_list:
				triple_node_list.remove([i[0],i[1]])
			tree_second_hierarchy_dict[i]=[]
			occupancy_img[i[0],i[1]]=255



points_distance_dict = {}
points_set = []

for x in range(len(dist_on_skel)):
    y=0
    for distance_value in dist_on_skel[x]:
    	if(distance_value>0):
    		points_distance_dict.setdefault(distance_value, []).append((x, y))
    		points_set.append([x,y])	
    	y = y +1
items = points_distance_dict.items()
items.sort()
#print items[0][1][0]

occupancy_img = np.array(Image.open('road.png').convert('L'))
#occupancy_img = np.array(Image.open('test2.png').convert('L'))
occ_rows,occ_cols=occupancy_img.shape
for i in range(occ_rows):
    for j in range(occ_cols):
        occupancy_img[i,j]=255
for i in points_set:
	occupancy_img[i[0],i[1]]=0

distance = ndi.distance_transform_edt(image)
local_maxi =feature.peak_local_max(distance, indices=False, footprint=np.ones((3, 3)),labels=image)
markers = ndi.label(local_maxi)[0]
labels =morphology.watershed(-distance, markers, mask=image)

node_dict = {}

for point in points_set:
	#print point
	for i in {-1,0,1}:
		for j in {-1,0,1}:
			if(point[0]+i>0 and point[0]+i<occ_rows and point[1]+j>0 and point[1]+j<occ_cols):
				if(i!=0 or j!=0):
					#print i,j
					if(occupancy_img[point[0]+i,point[1]+j]==0):
						node_dict.setdefault((point[0], point[1]), []).append([ point[0]+i, point[1]+j])

#print node_dict
triple_node_dict = {}
triple_node_list = []
for x1,y1 in node_dict:
	if (len(node_dict[x1,y1])>2):
		triple_node_dict.setdefault((x1, y1), []).append(node_dict[x1,y1])
		triple_node_list.append([x1,y1])
print triple_node_list
print len(node_dict)
print len(triple_node_list)
for triple_point in triple_node_list:
	if node_dict.has_key((triple_point[0],triple_point[1]))==True:
		remove_redundance(triple_point,node_dict,triple_node_dict)

triple_node_dict = {}
triple_node_list = []
for x1,y1 in node_dict:
	if (len(node_dict[x1,y1])>2):
		triple_node_dict.setdefault((x1, y1), []).append(node_dict[x1,y1])
		triple_node_list.append([x1,y1])
print triple_node_list
print len(node_dict)
print len(triple_node_list)

close_loop_list = []
external_path_list = []
#close_loop_list.append(triple_node_list[0])
#print close_loop_list
close_loop_list_index = 0
triple_node_list_index = 0
#print len(close_loop_list)
for triple_point in triple_node_list:
	if triple_point != [-10,-10]:
		close_loop_list_index = 0
		close_loop_list = []
		external_path_list = []
		close_loop_list.append(triple_point)
		#print close_loop_list	
		while close_loop_list_index<len(close_loop_list):
			#close_loop_list.append(triple_node_list[close_loop_list_index])
			point = close_loop_list[close_loop_list_index]
			for consecutive_points_list in triple_node_dict[(point[0],point[1])]:
				#print consecutive_points_list
				for consecutive_point in consecutive_points_list:
					#print consecutive_point
					if(consecutive_point in triple_node_list):
						#print "111"
						if(consecutive_point not in close_loop_list):
							close_loop_list.append(consecutive_point)
							#print consecutive_point
					else:
						if(consecutive_point not in external_path_list):
							external_path_list.append(consecutive_point)
						else:
							external_path_list.remove(consecutive_point)
							#print "remove"
			#print index
			#print len(close_loop_list)
			close_loop_list_index = close_loop_list_index + 1
		#print close_loop_list
		#print external_path_list
		#print ' '
		if len(close_loop_list)>2:
			#print "111111111"
			central_point = close_loop_list[0]
			occupancy_img[central_point[0],central_point[1]]=188
			for i in close_loop_list:
				if i != close_loop_list[0]:
					#print i,"i"
					for point in node_dict[(i[0],i[1])]:
						node_dict[(point[0],point[1])].remove([i[0],i[1]])
					node_dict.pop((i[0],i[1]))
					if triple_node_dict.has_key((i[0],i[1]))==True:
						triple_node_dict.pop((i[0],i[1]))
					if 	[i[0],i[1]] in triple_node_list:
						triple_node_list.remove([i[0],i[1]])
					occupancy_img[i[0],i[1]]=255
			for j in external_path_list:
				if j not in node_dict[(central_point[0],central_point[1])]:
					node_dict[(central_point[0],central_point[1])].append(j)
			print node_dict[(central_point[0],central_point[1])]		

triple_node_dict = {}
triple_node_list = []
for x1,y1 in node_dict:
	if (len(node_dict[x1,y1])>2):
		triple_node_dict.setdefault((x1, y1), []).append(node_dict[x1,y1])
		triple_node_list.append([x1,y1])
print triple_node_list
print len(node_dict)
print len(triple_node_list)


#print close_loop_list
#print " "
#print external_path_list	

#Dijkstra((external_path_list[0][0],external_path_list[0][1]),(external_path_list[1][0],external_path_list[1][1]),triple_node_dict,node_dict)




'''for x2,y2 in triple_node_dict:
			if (abs(x1-x2)==1 and abs(y1-y2)==1):
				triple_node_dict[(x1,y1)]=0
				triple_node_dict[(x2,y2)]=0

final_triple_node_dict = {}
for x1,y1 in triple_node_dict:
	if (triple_node_dict[(x1,y1)]!=0):
		final_triple_node_dict.setdefault((x1, y1), []).append(triple_node_dict[x1,y1])'''
		


#for node in triple_node_dict:
	#print node


fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(8, 8))
axes = axes.ravel()
ax0, ax1, ax2, ax3 = axes
ax0.imshow(image, cmap='gray', interpolation='nearest')
ax0.set_title('original', fontsize=20)
ax1.imshow(occupancy_img, cmap='gray', interpolation='nearest')
ax1.set_title('skeleton', fontsize=20)
ax1.contour(image, [0.5], colors='w')
ax2.imshow(dist_on_skel, interpolation='nearest')
ax2.contour(image, [0.5], colors='w')
ax3.imshow(skel, interpolation='nearest')
ax3.contour(image, [0.5], colors='w')
plt.savefig("bar.png",dpi=700)
plt.show()
