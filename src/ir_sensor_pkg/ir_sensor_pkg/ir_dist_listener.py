#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from example_interfaces.msg import String


class ir_distance_listener_node(Node):
    def __init__(self):
        super().__init__("ir_dist_listener")

        self.subscriber_ = self.create_subscription(
            String, "ir_distance", self.callback_ir_distances, 10)
        self.get_logger().info("listening to ir sensor...")

    def callback_ir_distances(self, msg):
        self.get_logger().info(msg.data)

def main(args=None):
    rclpy.init(args=args)
    node = ir_distance_listener_node()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
