#! /usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from ultralytics import YOLO
import ros2_numpy

class YoloNode(Node):
    def __init__(self):
        super().__init__('yolo_node')
        self.subscription = self.create_subscription(Image, '/image_raw', self.callback, 10) 
        self.det_image_pub = self.create_publisher(Image, "/yolo/detection/image", 10)
        self.detection_model = YOLO("yolo26n.pt")

    def callback(self, data):
        array = ros2_numpy.numpify(data)
        if self.det_image_pub.get_subscription_count():
            det_result = self.detection_model(array)
            det_annotated = det_result[0].plot(show=False)
            self.det_image_pub.publish(ros2_numpy.msgify(Image, det_annotated, encoding="bgr8"))

def main(args=None):
    rclpy.init(args=args)
    yolo_node = YoloNode()
    rclpy.spin(yolo_node)
    yolo_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()