#!/usr/bin/env python

import rospy
from std_msgs.msg import String


class Sending_node:
    def __init__(self):
        #variables
        self.coordinates = '1 2 3 4 5 6'
        #END - variables ----------------------------------------------

        #init_node
        rospy.init_node('sending_node', anonymous=False)
        rate = rospy.Rate(10)  # 100hz update rate.
        #END - init_node--------------------------------------------------

        #Publishers
        #pub_... = rospy.Publisher('Topic', String, queue_size=10)

        self.iiwa_pub = rospy.Publisher('coordinates_iiwa', String, queue_size=10) #send iiwa coordinates in the coordinates_iiwas topic

        #END - Publishers-------------------------------------------------


    #publish function for publishers
    def iiwa_publish(self, message):
        self.iiwa_pub.publish(message)

    #END - publish-----------------------------------------------------

if __name__ == '__main__':
    s_node = Sending_node()
    while not rospy.is_shutdown():
        s_node.iiwa_publish(s_node.coordinates)
        # print('inside while')
