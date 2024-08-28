#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def callback(msg):
    rospy.loginfo(f"I recieved the following message [{msg.data}]")

def listener():

    rospy.init_node("listener", anonymous=True)

    sub = rospy.Subscriber("/chat", String, callback)

    
    rospy.spin()

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException():
        pass