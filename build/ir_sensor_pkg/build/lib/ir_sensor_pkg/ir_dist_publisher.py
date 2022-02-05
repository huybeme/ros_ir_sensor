#!/usr/bin/env python3
import rclpy
from rclpy import Node
import spidev

"""
    source code for ir sensor and modified for ros implementation from:
    https://tutorials-raspberrypi.com/infrared-distance-measurement-with-the-raspberry-pi-sharp-gp2y0a02yk0f/
"""

ir_sensor = spidev.SpiDev()
ir_sensor.open(0,0)
ir_sensor.max_speed_hz = 1000000
     
class ir_dist_publisher_node(Node):
    def __init__(self):
        super().__init__("ir_dist_publisher")
        
        v = (self.ReadChannel(0) / 1023.0) * 2.8
        self.dist = 16.2537 * v**4 - 129.893 * v**3 + 382.268 * v**2 - 512.611 * v + 301.439

        self.publish_dist = self.create_publisher(
            msg_type=float, topic="ir_distance", qos_profile=10)
        self.timer = self.create_timer(1.0, self.publish_dist)

        self.get_logger().info("ir sensor publisher started.")

    def publish_distance(self):
        self.publish_dist.publish(str(self.dist))

    def ReadChannel(self, channel):
        val = ir_sensor.xfer2([1, (8+channel) << 4, 0])
        data = ((val[1]&3) << 8) + val[2]
        return data


def main(args=None):
    rclpy.init(args=args)
    node = ir_dist_publisher_node()
    rclpy.spin(node)
    rclpy.shutdown()
     
     
if __name__ == "__main__":
    main()