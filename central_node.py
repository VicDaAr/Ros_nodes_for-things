#!/usr/bin/env python

import rospy
from std_msgs.msg import String

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

        #END - Publishers-------------------------------------------------

        #Subscribers
        #sub_... = rospy.Subscriber("Topic", String, self.callback)
        sub_test = rospy.Subscriber('connection', String, self.callback_test)
        #END - Subscribers------------------------------------------------

    #callbacks for subscribers
    def callback(self,data): #data is the messege subscriber received
        return

    def callback_test(self,data):
        print(data)
    #END - Callback---------------------------------------------------

if __name__ == '__main__':
    c_node = Central_node()
    rospy.spin()