#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import std_msgs


class Central_node:
    def __init__(self):
        #variables
        self.received_coordinates = ([None,None,None,None,None,None])
        #END - variables ----------------------------------------------

        #init_node
        rospy.init_node('central_node', anonymous=False)
        rate = rospy.Rate(10)  # 100hz update rate.
        #END - init_node--------------------------------------------------

        #Publishers
        #pub_... = rospy.Publisher('Topic', String, queue_size=10)

        self.inV_pub = rospy.Publisher('iiwa_coordinates', String, queue_size=10) #send iiwa coordinates in the iiwa_coordinates topic

        #END - Publishers-------------------------------------------------

        #Subscribers
        #sub_... = rospy.Subscriber("Topic", String, self.callback)

        self.sub_test = rospy.Subscriber('connection', String, self.test_callback)

        #END - Subscribers------------------------------------------------

    #callbacks for subscribers
    def callback(self,data): #data is the messege subscriber received
        return

    def test_callback(self,data):
        print(data.data)
    #END - Callback---------------------------------------------------

    #publish function for publishers
    def inV_publish(self, message):
        self.inV_pub.publish(message)

    #END - publish-----------------------------------------------------

if __name__ == '__main__':
    c_node = Central_node()
    rospy.spin()