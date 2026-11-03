import os

from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    pkg_dir = get_package_share_directory('my_viz_pkg')

    rviz_config = os.path.join(
        pkg_dir,
        'config',
        'integrated_view.rviz'
    )

    marker_node = Node(
        package='my_viz_pkg',
        executable='custom_marker_publisher',
        name='custom_marker_publisher',
        output='screen'
    )

    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        arguments=['-d', rviz_config],
        output='screen'
    )

    return LaunchDescription([
        marker_node,
        rviz_node
    ])
