#!/usr/bin/env python

import rospy
from std_msgs.msg import String

class Central_node:
    def __init__(self):
        #variables
        self.received_coordinates = ''
        #END - variables ----------------------------------------------

        #init_node
        rospy.init_node('central_node', anonymous=False)
        rate = rospy.Rate(10)  # 10hz update rate.
        #END - init_node--------------------------------------------------

        #Publishers
        #pub_... = rospy.Publisher('Topic', String, queue_size=10)

        self.inV_pub = rospy.Publisher('coordinates_inV', String, queue_size=10) #send iiwa coordinates in the iiwa_coordinates topic

        #END - Publishers-------------------------------------------------

        #Subscribers
        #sub_... = rospy.Subscriber("Topic", String, self.callback)
        sub_test = rospy.Subscriber('connection', String, self.callback_test)
        iiwa_sub = rospy.Subscriber('coordinates_iiwa', String, self.iiwa_callback)
        #END - Subscribers------------------------------------------------

    #callbacks for subscribers
    #def callback(self,data): #data is the messege subscriber received
        #return

    def callback_test(self,data):
        print(data.data)
    def iiwa_callback(self,data):
        self.inV_publish(data.data)
        print(data.data)

    #END - Callback---------------------------------------------------

    #publish function for publishers
    def inV_publish(self, message):
        self.inV_pub.publish(message)

    #END - publish-----------------------------------------------------


if __name__ == '__main__':
    c_node = Central_node()
    rospy.spin()