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

Intersection scenarios: There are 2 intersection, one rectangular and one squared. Both can be launched with or without gui using one of these options:

`roslaunch vinter_utils intersection.launch`
`roslaunch vinter_utils intersection_no_gui.launch`
`roslaunch vinter_utils intersection_sq.launch`
`roslaunch vinter_utils intersection_sq_no_gui.launch`



