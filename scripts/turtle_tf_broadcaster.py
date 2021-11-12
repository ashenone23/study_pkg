#!/usr/bin/env python
import rospy
import tf
import math
from tf.transformations import quaternion_from_euler
from turtlesim.msg import Pose

# Register node / fake node name - we will rename =)
rospy.init_node('tf_turtle')
# Get private parameter / make it global variable
turtlename = rospy.get_param('~turtle_tf_name')
# Callback function
def handle_turtle_pose(msg):
    # Get broadcaster object
    global counter
    br = tf.TransformBroadcaster()
    
    # Broadcast TF trasform (world -> turtlename)
    br.sendTransform((msg.x, msg.y, 0),
                     quaternion_from_euler(0, 0, msg.theta),
                     rospy.Time.now(),
                     turtlename,
                     "world")
    sattelite= tf.TransformBroadcaster()
    sattelite.sendTransform((math.sin(counter)*10, math.cos(counter)*10, 1),
                     quaternion_from_euler(0, 0, 0),
                     rospy.Time.now(),
                     sat,
                     "turtle1")
    counter+=0.01
rospy.init_node('tf_turtle')
# Get private parameter / make it global variable
turtlename = rospy.get_param('~turtle_tf_name')
# Callback function
sat='sat'
counter=0
# Subscribe to /input_pose topic - just gonna remap it to work with
rospy.Subscriber('input_pose',
                 Pose,
                 handle_turtle_pose)
# You spin my head right round, right round - Florida =)
# Just handle all topic messages until node (or ROS) is working
rospy.spin()

