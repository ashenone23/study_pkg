#!/usr/bin/env python3
from std_msgs.msg import Int64MultiArray, Int64
from study_pkg.srv import Poly, PolyResponse, PolyRequest
import rospy
def handle_poly_srv(req):
    req.x1 =req.x1 ** 2
    poly_srv1 = rospy.ServiceProxy('bratan', Poly)
    req = PolyRequest(req.x1,req.x2)
    resp=poly_srv1(req)
    rospy.loginfo("prinyal otvet: %s" % resp.y)
    return resp

def poly_server():
    rospy.init_node('mujik')
    s = rospy.Service('mujik', Poly, handle_poly_srv)
    rospy.loginfo("Ready to calc polynomial.")
    rospy.spin() 
try:
    poly_server()
except (rospy.ROSInterruptException, KeyboardInterrupt):
    rospy.logerr('Exception catched')
