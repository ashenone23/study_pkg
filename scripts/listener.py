#!/usr/bin/env python3
import rospy
from study_pkg.srv import Poly, PolyResponse, PolyRequest
from std_msgs.msg import Int64MultiArray, Int64
pub2 = rospy.Publisher('my_chat_topic2', Int64, queue_size=10)
def start_bratan(resp):
    msg = Int64()
    
    result = "sum_service: Otpravil okon4atelniy otvet %s" % resp
    rospy.loginfo(result)

    msg.data = resp
    pub2.publish(msg)
        
def callback(msg):
    rospy.loginfo("sum_service: polu4il value_after_poly %s, slagaemoe %s" % msg.data)
    req=msg.data
rospy.Subscriber("my_chat_topic", Int64MultiArray,callback,queue_size=10)
def handle_sum_srv(req):
    result =req.x1 + req.x2
    resp=PolyResponse()
    resp.y=result
    start_bratan(resp.y)
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
rospy.spin()

