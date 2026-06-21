from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'myrosbot_one'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'config'), glob('config/*')),
        (os.path.join('share', package_name, 'description'), glob('description/*')),
        (os.path.join('share', package_name, 'launch'), glob('launch/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='root',
    maintainer_email='minsuu2@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'myrosbot_one = myrosbot_one.myrosbot_one:main',
            'robot_telemetry_publisher = myrosbot_one.robot_telemetry_publisher:main',
            'lidar_publisher = myrosbot_one.lidar_publisher:main',
            'teleop_twist_keyboard = myrosbot_one.teleop_twist_keyboard:main',
            'robot_patrol_waypoints = myrosbot_one.robot_patrol_waypoints:main',
            'mjpeg_camera_publisher = myrosbot_one.mjpeg_camera_publisher:main'
        ],
    },
)
