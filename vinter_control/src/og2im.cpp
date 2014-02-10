#include "ros/ros.h"
#include <boost/thread/mutex.hpp>
#include "nav_msgs/OccupancyGrid.h"
#include "sensor_msgs/Image.h"

//nav_msgs::OccupancyGrid myOG;
//sensor_msgs::Image myImage;
//bool OG_rcvd;

/*void ogCallback(const nav_msgs::OccupancyGrid::ConstPtr &msg)
{
	myOG = *msg;
	OG_rcvd = true;

}*/

class OG2Im_node
{
	nav_msgs::OccupancyGrid og;
	sensor_msgs::Image im;

	ros::NodeHandle nh;
	ros::Publisher pub;
	ros::Subscriber sub;
	//ros::Rate r;
	boost::mutex msg_lock;

public:
	OG2Im_node();
	~OG2Im_node();

	bool cm_rcv;

	void update_costmap(const boost::shared_ptr<nav_msgs::OccupancyGrid const>& msg);
	void copy_data();
	void publish_image();

};

OG2Im_node::OG2Im_node()
{
	cm_rcv = false;
	im.is_bigendian = 0;
	im.encoding = "8UC1";
	pub = nh.advertise<sensor_msgs::Image>("map_img",1000);
	sub = nh.subscribe<nav_msgs::OccupancyGrid>("/intersection/costmap_node/costmap/costmap",1000,boost::bind(&OG2Im_node::update_costmap,this,_1));
}

OG2Im_node::~OG2Im_node()
{
}

void OG2Im_node::update_costmap(const boost::shared_ptr<nav_msgs::OccupancyGrid const>& msg)
{
	boost::mutex::scoped_lock lock(msg_lock);
	og = *msg;
	ROS_INFO("I've receive a costmap!");
	cm_rcv = true;
}

void OG2Im_node::copy_data()
{
	im.header = og.header;
	im.height = og.info.height;
	im.width = og.info.width;
	im.step = og.info.height;
	im.data.clear();
	im.data.reserve(og.data.size());
	ROS_INFO("og.data minmax: %d,%d",*(std::min_element(og.data.begin(),og.data.end())),*(std::max_element(og.data.begin(),og.data.end())));
	//copy(og.data.begin(), og.data.end(), im.data.begin());
	//im.data = og.data;
	//im.data.swap(og.data);

	for (int i = 0;i < og.data.size(); i++)
	{
		int cell = og.data[i];

		if (cell < 0)
			cell = 0;
		im.data.push_back(2*cell);
		//ROS_INFO("data: %d<-%d",im.data[i],og.data[i]);
	}


	/*for (std::vector<int>::iterator it = og.data.begin() ; it != og.data.end(); ++it)
	{
		im.data.push_back(*it);
	}*/

	ROS_INFO("im.data minmax: %d,%d",*(std::min_element(im.data.begin(),im.data.end())),*(std::max_element(im.data.begin(),im.data.end())));
	ROS_INFO("im.data: %d,og.data: %d",im.data.size(),og.data.size());
}

void OG2Im_node::publish_image()
{
	pub.publish(im);
	ROS_INFO("Image Published");
}

int main(int argc, char** argv)
{
	ros::init(argc, argv, "OccGrid2Image");

	/*myImage.is_bigendian = 1;
	myImage.encoding = "mono8";

	ros::NodeHandle nh;
	ros::Publisher pub = nh.advertise<sensor_msgs::Image>("map_img",1000);
	ros::Subscriber sub = nh.subscribe("/intersection/costmap_node/costmap/costmap",1000,ogCallback);*/
	OG2Im_node og2im;
	ros::Rate r(10);

	while (ros::ok())
	{
		/*if(OG_rcvd = true)
		{
			myImage.header = myOG.header;
			myImage.height = myOG.info.height;
			myImage.width = myOG.info.width;

			myImage.step = myOG.info.height;

			//std::vector<int> data;
			//myImage.data = myOG.data;
			//std::memcpy(myImage.data, myOG.data, myImage.height*myImage.width);
			for (int i = 0;i < 255; i++)
			{
				myImage.data[i] = i;//myOG.data[i];
			}

			ROS_INFO("I've receive a costmap with size %d x %d: %d",myImage.height,myImage.width
					,sizeof(myOG.data));
			pub.publish(myImage);
			OG_rcvd = false;
		}*/
		if(og2im.cm_rcv)
		{
			og2im.copy_data();
			og2im.publish_image();

			og2im.cm_rcv = false;
		}

		ros::spinOnce();
		r.sleep();
	}
}
