#!/usr/bin/env python3
import rospy
import sys
from study_pkg.srv import Poly, PolyRequest, PolyResponse
try:
        poly_srv = rospy.ServiceProxy('mujik', Poly)
        req = PolyRequest(x1=int(sys.argv[1]),x2=int(sys.argv[2]))
        resp = poly_srv(req)
        print('Response: %s' % resp.y) 
except rospy.ServiceException as e:
    rospy.logerr("Service call failed: %s" % e)

