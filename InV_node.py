#!/usr/bin/env python

import rospy
from std_msgs.msg import String


class InV_node:
    def __init__(self):
        #variables
        self.received_coordinates = ''

        #END - variables ----------------------------------------------

        #init_node
        rospy.init_node('inV_node', anonymous=False)
        rate = rospy.Rate(10)  # 10hz update rate.
        #END - init_node--------------------------------------------------


        #Subscribers
        #sub_... = rospy.Subscriber("Topic", String, self.callback)

        self.inV_sub = rospy.Subscriber('coordinates_inV', String, self.save_value)

        #END - Subscribers------------------------------------------------

    #callbacks for subscribers
    def callback(self,data): #data is the messege subscriber received
        return

    def save_value(self,data): #Temporary solution, immediately send message to inV_Node
        self.received_coordinates = data.data
        print(self.received_coordinates)

    #END - Callback---------------------------------------------------


if __name__ == '__main__':
    i_node = InV_node()
    rospy.spin()