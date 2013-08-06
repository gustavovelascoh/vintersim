#include "ros/ros.h"
#include "std_msgs/String.h"
#include "nav_msgs/Odometry.h"

#include <sstream>
#include <string>

void update_odom(const nav_msgs::Odometry::ConstPtr &msg)
{
	void* tracked = tracked_object;
	ROS_INFO("HEY ");

}

int main(int argc, char** argv)
{

	ros::init(argc, argv, "laser_station");

	ros::NodeHandle n;
	ros::Subscriber sub[4];
	//const ros::Subscriber& sub_a[4] = {sub[0],sub[1],sub[2],sub[3]};
	int subs[] = {0,1,2,3};

	for (int i=0; i < 4; ++i)
	{
		const ros::Subscriber& sub_a = sub[i];
		std::stringstream ss;
		ss << "base_" << i << "/base_pose_ground_truth";
		std::string s = ss.str();

		sub[i] = n.subscribe(s, 1000, update_odom);//,sub_a);
		ROS_INFO("Subscribing to topic: ");
		std::cout << s << std::endl;
	}

	ros::spin();

	return 0;
}
