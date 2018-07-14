#!/usr/bin/env python
# license removed for brevity

import sys
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

def movebase_client():
    if (len(sys.argv) == 2):
        client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
        client.wait_for_server()

        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = "map"
        goal.target_pose.header.stamp = rospy.Time.now()
        
        if (sys.argv[1] == "room0"):
            goal.target_pose.pose.position.x = -0.222061890754
            goal.target_pose.pose.position.y = 8.77443683017
            goal.target_pose.pose.position.z = 0
            goal.target_pose.pose.orientation.z = 0.992164857537
            goal.target_pose.pose.orientation.w = 0.124935565268

        elif (sys.argv[1] == "room1"):
            goal.target_pose.pose.position.x = -0.561584992267
            goal.target_pose.pose.position.y = 1.82561917372
            goal.target_pose.pose.orientation.x = 0.0
            goal.target_pose.pose.orientation.y = 0.0
            goal.target_pose.pose.orientation.z = 0.993022598671
            goal.target_pose.pose.orientation.w = 0.117924206712

        elif (sys.argv[1] == "room2"):
            goal.target_pose.pose.position.x = 2.72958946936
            goal.target_pose.pose.position.y =  -0.080353884531

            goal.target_pose.pose.orientation.z = -0.0507704350695
            goal.target_pose.pose.orientation.w =0.998710349863

        elif (sys.argv[1] == "room3"):
            goal.target_pose.pose.position.x = 1.47831637257
            goal.target_pose.pose.position.y =  3.16523617561
            goal.target_pose.pose.orientation.z = 0.656558987464
            goal.target_pose.pose.orientation.w = 0.754274682049

        elif (sys.argv[1] == "room4"):
            goal.target_pose.pose.position.x =2.32607462446
            goal.target_pose.pose.position.y =5.5376365749
            goal.target_pose.pose.orientation.z = 0.656558987464
            goal.target_pose.pose.orientation.w = 0.754274682049

        else:
            rospy.logerr("Valid room are only room0, room1, room2, room3 and room4")

        client.send_goal(goal)
        wait = client.wait_for_result()
    else:
        rospy.logerr("Pass only one parameter to move to other room")
    if not wait:
        rospy.logerr("Action server not available!")
        rospy.signal_shutdown("Action server not available!")
    else:
        return client.get_result()

if __name__ == '__main__':
    try:
        rospy.init_node('movebase_client_py')
        result = movebase_client()
        if result:
            rospy.loginfo("Goal execution done!")
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")
