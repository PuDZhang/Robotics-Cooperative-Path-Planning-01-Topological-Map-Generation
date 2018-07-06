# Robotics-Path-Planning-Topological-Map-Generation
Python codes for robotics Topological-Map-Generation algorithm.
## What is this?
This is a Python code of Topological-Map-Generation algorithm. <br>
This method can generate topological maps in clutter free space. <br>
The topological map can be used in multi-vehicle path(movement sequence) planning. <br>
![multi-vehicle-scenario](https://github.com/ChenBohan/Robotics-Path-Planning-Topological-Map-Generation/blob/master/pic/multi-vehicle%20scenario.png)  
It is divided into three steps： <br>
1. Extract the centerline of the free space.
![skeletonize](https://github.com/ChenBohan/Robotics-Path-Planning-Topological-Map-Generation/blob/master/pic/The%20centerline%20of%20the%20road.png)  
2. Do the collision checking & width detecting.
![checking](https://github.com/ChenBohan/Robotics-Path-Planning-Topological-Map-Generation/blob/master/pic/checking%26detecting.png)  
3. Generate a topology map.<br>
![Topological-map](https://github.com/ChenBohan/Robotics-Path-Planning-Topological-Map-Generation/blob/master/pic/Topological%20map.png)  
## Extract the centerline
There are two different methods that are applied in this step, Skeletonize Method & Voronoi Method.
### Skeletonize
Skeletonization reduces binary objects to 1 pixel wide representations.<br> 
This can be useful for feature extraction, and/or representing an object’s topology.<br>
![skeletonize](https://github.com/ChenBohan/Robotics-Path-Planning-Topological-Map-Generation/blob/master/pic/skeletonize.png)  
### Voronoi


