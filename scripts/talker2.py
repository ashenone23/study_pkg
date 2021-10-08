#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32
from study_pkg.msg import Control
msg = Control()
msg.steer = 40
msg.speed = 10
rospy.init_node('talker2')
pub = rospy.Publisher('my_chat_topic2', Control, queue_size=10)
rate = rospy.Rate(1)
def topic_cb(msg):
    rospy.loginfo('Speed: %d / Steer: %d' % (msg.speed, msg.steer))

try:
    topic_cb(msg)
except (rospy.ROSInterruptException, KeyboardInterrupt):
    rospy.logerr('Exception catched')
