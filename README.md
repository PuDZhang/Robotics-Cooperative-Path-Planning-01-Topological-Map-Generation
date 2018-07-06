# Robotics-Path-Planning-Topological-Map-Generation
Python codes for robotics Topological-Map-Generation algorithm.
## What is this?
This is a Python code of Topological-Map-Generation algorithm. <br>
This method can generate topological maps in clutter free space. <br>
The topological map can be used in multi-vehicle path(movement sequence) planning. <br>
<img src="https://github.com/ChenBohan/Robotics-Path-Planning-Topological-Map-Generation/blob/master/pic/multi-vehicle%20scenario.png" width = "50%" height = "50%" div align=center />

It is divided into three steps： 
1. Extract the centerline of the free space.<br>
2. Do the collision checking & width detecting.<br>
3. Generate a topology map.<br>

## Extract the centerline
There are two different methods that are applied in this step, Skeletonize Method & Voronoi Method.

Scenario:<br>
<img src="https://github.com/ChenBohan/Robotics-Path-Planning-Topological-Map-Generation/blob/master/pic/scenario.png" width = "50%" height = "50%" div align=center />

Grid-based Map:<br>
<img src="https://github.com/ChenBohan/Robotics-Path-Planning-Topological-Map-Generation/blob/master/pic/Grid-based%20map.png" width = "50%" height = "50%" div align=center />

Centerline:<br>
<img src="https://github.com/ChenBohan/Robotics-Path-Planning-Topological-Map-Generation/blob/master/pic/The%20centerline%20of%20the%20road.png" width = "50%" height = "50%" div align=center />、

### Skeletonize
Skeletonization reduces binary objects to 1 pixel wide representations.<br> 
This can be useful for feature extraction, and/or representing an object’s topology.<br>
<img src="https://github.com/ChenBohan/Robotics-Path-Planning-Topological-Map-Generation/blob/master/pic/skeletonize.png" width = "40%" height = "40%" div align=center />

### Voronoi
<img src="https://github.com/ChenBohan/Robotics-Path-Planning-Topological-Map-Generation/blob/master/pic/Learning%20metric-topological%20maps%20for%20indoor%20mobile%20robot%20navigation.png" width = "60%" height = "60%" div align=center />

Ref:
[Learning metric-topological maps for indoor mobile robot navigation](https://www.ri.cmu.edu/pub_files/pub1/thrun_sebastian_1996_1/thrun_sebastian_1996_1.pdf "Learning metric-topological maps for indoor mobile robot navigation")

## Collision checking & Width Detecting
Refine the centerline.

<img src="https://github.com/ChenBohan/Robotics-Path-Planning-Topological-Map-Generation/blob/master/pic/checking%26detecting.png" width = "40%" height = "40%" div align=center />

<img src="https://github.com/ChenBohan/Robotics-Path-Planning-Topological-Map-Generation/blob/master/pic/distance.png" width = "40%" height = "40%" div align=center />

## Generate a Topological Map
According to the rules, generate a topology map based on the centerline.

<img src="https://github.com/ChenBohan/Robotics-Path-Planning-Topological-Map-Generation/blob/master/pic/Topological%20map.png" width = "40%" height = "40%" div align=center />

