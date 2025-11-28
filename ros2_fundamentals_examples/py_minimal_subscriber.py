#! /usr/bin/env python3

'''
  Desctiption:
    This ROS 2 node subscribes to "Hello World" messagers.

  ------
  Publishing Topics:
    None
  -----
  Subscription Topics: 
    The channel containing the "Hello World Messages".
    /py_example_topic - std_msgs/string
  
  Author: Sujal Maharjan
  Date: Nov 27, 2025
  '''
import rclpy
from rclpy.node import Node

from std_msgs.msg import String

class MinimalPyPublisher(Node):
  def __init__(self):
    super().__init__('minimal_py_subscriber')

    self.subscriber_1 = self.create_subscription(
      String,
      'py_example_topic',
      self.listner_callback,
      10
    )
  
  def listner_callback(self,  msg):
    self.get_logger().info(f'I heard: "{msg.data}"')


def main(args=None):
  rclpy.init(args=args)

  minimal_py_subscriber = MinimalPyPublisher()
  rclpy.spin(minimal_py_subscriber)

  minimal_py_subscriber.destroy_node()

  rclpy.shutdown()

if __name__ == '__main__':
  main()