VINTERSIM
=========

Vehicular intersection simulator Project.

This Repo is part of the project "Intelligent system for vehicle localization, incident detection and accident prevention at vehicular intersections using mobile robots in a pilot stage" developed by PSI group (Perception and Intelligent Systems) at Universidad del Valle (Cali, Colombia).

This repo contains 4 packages used for intersection managment:
	vinter_control: Intersection control
	vinter_msgs: Messages for V2V and V2I communication
	vinter_sim: Simulator based on stage
	vinter_utils: Miscellaneous files like maps, images, .launch files and parameters.

------------------------

##Using##

1. execute in a terminal `roslaunch vinter_utils intersection1_reduced.launch`
2. In another terminal run `rosrun costmap_2d costmap_2d_node`
3. For visualization use `rosrun rviz rviz`

