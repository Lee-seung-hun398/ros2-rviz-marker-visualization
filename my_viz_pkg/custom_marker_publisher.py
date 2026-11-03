#!/usr/bin/env python3

import math

import rclpy
from rclpy.node import Node
from rclpy.duration import Duration

from geometry_msgs.msg import Point
from visualization_msgs.msg import Marker, MarkerArray


class CustomMarkerPublisher(Node):

    def __init__(self):
        super().__init__('custom_marker_publisher')

        self.pub_markers = self.create_publisher(
            MarkerArray,
            '/visual_markers',
            10
        )

        # 10Hz
        self.timer = self.create_timer(0.1, self.publish_markers)

        self.get_logger().info('Custom Marker Publisher 시작')


    def publish_markers(self):

        now = self.get_clock().now().to_msg()

        # ==========================================================
        # 1. 예상 주행 경로 LINE_STRIP
        # ==========================================================

        path_marker = Marker()

        path_marker.header.frame_id = 'base_link'
        path_marker.header.stamp = now

        path_marker.ns = 'trajectory'
        path_marker.id = 0

        path_marker.type = Marker.LINE_STRIP
        path_marker.action = Marker.ADD

        path_marker.scale.x = 0.08

        path_marker.color.r = 0.0
        path_marker.color.g = 1.0
        path_marker.color.b = 0.0
        path_marker.color.a = 0.8

        path_marker.pose.orientation.w = 1.0

        path_marker.lifetime = Duration(seconds=0.2).to_msg()

        # 전방 약 5m S자 경로
        for i in range(40):

            p = Point()

            p.x = i * 0.125
            p.y = 0.4 * math.sin(i * 0.2)
            p.z = 0.05

            path_marker.points.append(p)


        # ==========================================================
        # 2. 장애물 CUBE
        # ==========================================================

        box = Marker()

        box.header.frame_id = 'base_link'
        box.header.stamp = now

        box.ns = 'obstacles'
        box.id = 1

        box.type = Marker.CUBE
        box.action = Marker.ADD

        box.pose.position.x = 3.0
        box.pose.position.y = 0.2
        box.pose.position.z = 0.4

        box.pose.orientation.w = 1.0

        box.scale.x = 0.8
        box.scale.y = 0.8
        box.scale.z = 0.8

        box.color.r = 1.0
        box.color.g = 0.0
        box.color.b = 0.0
        box.color.a = 0.6

        box.lifetime = Duration(seconds=0.2).to_msg()


        # ==========================================================
        # 3. 경고 TEXT
        # ==========================================================

        txt = Marker()

        txt.header.frame_id = 'base_link'
        txt.header.stamp = now

        txt.ns = 'labels'
        txt.id = 2

        txt.type = Marker.TEXT_VIEW_FACING
        txt.action = Marker.ADD

        txt.pose.position.x = 3.0
        txt.pose.position.y = 0.2
        txt.pose.position.z = 1.0

        txt.pose.orientation.w = 1.0

        txt.scale.z = 0.25

        txt.text = 'WARNING: OBSTACLE [3.0m]'

        txt.color.r = 1.0
        txt.color.g = 1.0
        txt.color.b = 1.0
        txt.color.a = 1.0

        txt.lifetime = Duration(seconds=0.2).to_msg()


        # ==========================================================
        # MarkerArray
        # ==========================================================

        marker_array = MarkerArray()

        marker_array.markers.append(path_marker)
        marker_array.markers.append(box)
        marker_array.markers.append(txt)

        self.pub_markers.publish(marker_array)


def main(args=None):

    rclpy.init(args=args)

    node = CustomMarkerPublisher()

    try:
        rclpy.spin(node)

    except KeyboardInterrupt:
        pass

    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()

