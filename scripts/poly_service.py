#!/usr/bin/env python3
from std_msgs.msg import Int64MultiArray, Int64
from study_pkg.srv import Poly, PolyResponse, PolyRequest
import rospy
pub = rospy.Publisher('my_chat_topic', Int64MultiArray, queue_size=10)
def callback2(msg):
    rospy.loginfo("poly_service: Polu4il %s" % msg.data)
rospy.Subscriber("my_chat_topic2", Int64,callback2,queue_size=10)
def start_mujik(x1,x2):
    msg = Int64MultiArray()
    poly_srv1 = rospy.ServiceProxy('bratan', Poly)
    req = PolyRequest(x1,x2)
    value_after_poly = "poly_service: 4islo posle vozvedeniya v stepen: %s, slagaemoe: %s" % (x1,x2)
    rospy.loginfo(value_after_poly)

    msg.data = [x1,x2]
    pub.publish(msg)
        
    
        
def handle_poly_srv(req):
    x1 =req.x1 ** 2
    x2=req.x2
    start_mujik(x1,x2)
    poly_srv1 = rospy.ServiceProxy('bratan', Poly)
    req = PolyRequest(x1,x2)
    resp=poly_srv1(req)
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
rospy.spin()
