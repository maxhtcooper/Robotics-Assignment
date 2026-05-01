from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'yolo_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
        # If you want to try a different video file, add below before changing it in yolo_launch.py
        (os.path.join('share', package_name), ['test.mp4']),(os.path.join('share', package_name), ['flowers.mp4'])  
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='max',
    maintainer_email='max@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': ['yolo_node = yolo_pkg.yolo:main',
        ],  
    },
)
