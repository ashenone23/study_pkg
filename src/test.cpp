#include <study_pkg/Control.h>
#include <ros/ros.h>
#include <sstream>
study_pkg::Control msg;

msg.steer = 20;
msg.speed = 10;
void topicCallback(const study_pkg::Control::ConstPtr& msg)
{
    ROS_INFO("Speed: %d / Steer: %d", msg->speed, msg->steer);
}

