#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def talker():

    rospy.init_node("talker", anonymous=True)

    pub = rospy.Publisher("/chat", String, queue_size=10)

    rate = rospy.Rate(1)

    counter = 0
    while not rospy.is_shutdown():
        
        msg = f"message numer {counter}"
        log_msg = f"i sent a message:{counter}"
        counter = counter + 1

        rospy.loginfo(log_msg)
        pub.publish(msg)

        rate.sleep()
    
if __name__ == '__main__':
    
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
        