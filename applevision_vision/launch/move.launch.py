from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='applevision_vision',
            executable='applevision_vision',
            name='applevision_vision'
        ),
        Node(
            package='applevision_vision',
            executable='pub_image',
            name='pub_image'
        ),
        Node(
            package='applevision_vision',
            executable='find_center',
            name='find_center',
        ), 
        Node(
            package='applevision_vision',
            executable='move',
            name='move',
        ), 
        Node(
            package='applevision_vision',
            executable='tof_fake',
            name='tof_fake',
        )
    ])