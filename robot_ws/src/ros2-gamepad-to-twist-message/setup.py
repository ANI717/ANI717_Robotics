from setuptools import setup, find_packages
from glob import glob

PACKAGE_NAME = 'ros2_gamepad_to_twist_message'

setup(
    name=PACKAGE_NAME,
    version='0.0.0',
    packages=find_packages(),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + PACKAGE_NAME]),
        ('share/' + PACKAGE_NAME, ['package.xml']),
        ('share/' + PACKAGE_NAME + '/launch', ['launch/launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ANI717',
    maintainer_email='animesh.ani@live.com',
    description='Package to Publish Gamepad Data to Twist Message for Robot Running',
    license='MIT License',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'execute = ros2_gamepad_to_twist_message.gamepad_to_twist_function:main',
        ],
    },
)