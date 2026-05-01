from launch import LaunchDescription
from launch_ros.actions import Node
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    
    # Get the path to the video (change file name if you want to use a different video)
    video_path = os.path.join(get_package_share_directory('yolo_pkg'), 'test.mp4')

    return LaunchDescription([
        # Start the video publisher
        Node(
            package='image_publisher',
            executable='image_publisher_node',
            name='video_source',
            parameters=[{
                'filename': video_path,
                'repeat': True,
            }],
        ),
        # Start the YOLO node
        Node(
            package='yolo_pkg',
            executable='yolo_node',
            name='yolo_detector',
            output='screen'
        )
    ])
