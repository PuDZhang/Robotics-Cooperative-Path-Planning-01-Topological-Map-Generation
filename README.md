# Robotics-Path-Planning-Topological-Map-Generation
Python codes for robotics Topological-Map-Generation algorithm.
## What is this?
This is a Python code of Topological-Map-Generation algorithm. This method can generate topological maps in clutter free space. The topological map can be used in multi-vehicle path(movement sequence) planning. It is divided into three steps. 
1. Extract the centerline of the free space.
2. Do the collision checking & width detecting.
3. Generate a topology map.<br>
![multi-vehicle-scenario](https://github.com/ChenBohan/Robotics-Path-Planning-Topological-Map-Generation/blob/master/pic/multi-vehicle%20scenario.png)  
## Extract the centerline
There are two different methods that are applied in this step, Skeletonize Method & Voronoi Method.
### Skeletonize
Skeletonization reduces binary objects to 1 pixel wide representations. This can be useful for feature extraction, and/or representing an object’s topology.<br>
In shape analysis, skeleton (or topological skeleton) of a shape is a thin version of that shape that is equidistant to its boundaries. The skeleton usually emphasizes geometrical and topological properties of the shape, such as its connectivity, topology, length, direction, and width. Together with the distance of its points to the shape boundary, the skeleton can also serve as a representation of the shape (they contain all the information necessary to reconstruct the shape).
### Voronoi


