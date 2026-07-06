from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='pkg01_helloworld_cpp',
            executable='helloworld',
            name='helloworld_node_1',
            output='screen',
        ),
        Node(
            package='pkg01_helloworld_cpp',
            executable='helloworld',
            name='helloworld_node_2',
            output='screen',
        ),
        Node(
            package='pkg01_helloworld_cpp',
            executable='helloworld',
            name='helloworld_node_3',
            output='screen',
        ),
        Node(
            package='pkg01_helloworld_cpp',
            executable='helloworld',
            name='helloworld_node_4',
            output='screen',
        ),
    ])
