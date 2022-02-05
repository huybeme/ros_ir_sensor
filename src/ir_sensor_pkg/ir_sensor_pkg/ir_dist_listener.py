#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from example_interfaces.msg import String
from example_interfaces.msg import Float64


class ir_distance_listener_node(Node):
    def __init__(self):
        super().__init__("ir_dist_listener")
        self.distance = 0.0
        self.publisher_dist = self.create_publisher(
            Float64, "ir_distance_values", 10)


        self.subscriber_ = self.create_subscription(
            String, "ir_distance", self.callback_ir_distances, 10)
        self.get_logger().info("listening to ir sensor...")

    def callback_ir_distances(self, msg):
        # self.get_logger().info(msg.data)
        dist_msg = Float64()
        dist_msg.data = msg.data
        self.publisher_dist.publish(dist_msg)

def main(args=None):
    rclpy.init(args=args)
    node = ir_distance_listener_node()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
