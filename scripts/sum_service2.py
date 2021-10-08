#!/usr/bin/env python3
import rospy
from study_pkg.srv import Poly, PolyResponse, PolyRequest
from std_msgs.msg import Int64MultiArray, Int64
def handle_sum_srv(req):
    rospy.loginfo("prinyal 2 4isla: %s %s" % (req.x1,req.x2))
    result =req.x1 + req.x2
    rospy.loginfo("Otpravil otvet: %s " % result)
    resp=PolyResponse()
    resp.y=result
    return resp

def sum_server():
    rospy.init_node('bratan')
    s = rospy.Service('bratan', Poly, handle_sum_srv)
    rospy.loginfo("Ready to calc sum.")
    rospy.spin()
try:
    sum_server()
except (rospy.ROSInterruptException, KeyboardInterrupt):
    rospy.logerr('Exception catched')
