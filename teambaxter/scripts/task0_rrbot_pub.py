#!/usr/bin/env python

import rospy 
from std_msgs.msg import Float64

def rrbot_talker():
    pub = rospy.Publisher('/rrbot/joint2_position_controller/command', Float64, queue_size=10)
    rospy.init_node('rrbot_talker', anonymous=True)
    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        joint_control = -1.5
        pub.publish(joint_control)
        rospy.sleep(1)

if __name__ == '__main__':
    try:
        rrbot_talker()
    except rospy.ROSInterruptException:
        pass