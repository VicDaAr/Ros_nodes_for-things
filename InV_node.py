#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import std_msgs


class InV_node:
    def __init__(self):
        #variables
        self.received_coordinates = ([None,None,None,None,None,None])

        #END - variables ----------------------------------------------

        #init_node
        rospy.init_node('central_node', anonymous=False)
        rate = rospy.Rate(10)  # 100hz update rate.
        #END - init_node--------------------------------------------------


        #Subscribers
        #sub_... = rospy.Subscriber("Topic", String, self.callback)

        self.inV_sub = rospy.Subscriber('iiwa_coordinates', String, self.save_value)

        #END - Subscribers------------------------------------------------

    #callbacks for subscribers
    def callback(self,data): #data is the messege subscriber received
        return

    def save_value(self,data): #Temporary solution, immediately send message to inV_Node
        data.data

    #END - Callback---------------------------------------------------


if __name__ == '__main__':
    c_node = InV_node()
    rospy.spin()