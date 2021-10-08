#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int64
rospy.init_node('mujik')
pub = rospy.Publisher('my_chat_topic', Int64, queue_size=10)
def callback2(msg):
    rospy.loginfo("I heard %s", msg.data)
rospy.Subscriber('my_chat_topic2', Int64, callback2, queue_size=10)
rate = rospy.Rate(1)
def start_mujik():
    msg = Int64()
    i=0
    while not rospy.is_shutdown():
        hello_Int64 = "4islo: %d" % i
        rospy.loginfo(hello_Int64)

        msg.data = i
        pub.publish(msg)
        i+=2
        rate.sleep()

try:
    start_mujik()
 
except (rospy.ROSInterruptException, KeyboardInterrupt):
    rospy.logerr('Exception catched')
