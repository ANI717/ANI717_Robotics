
<p align="center">
  <h1 align="center">ANI717 Robotics Workspace</h1>
</p>

<p align="justify">
Robotics workspace. Contains ROS2 packages to run robot cars controlled by gamepad, collects annotated camera images, and runs a robot car autonomously with a trained neural network.
</p>

## Quick Links
[Headless Jetbot Setup](https://github.com/ANI717/Headless-Jetson-Nano-Setup)<br/>
[Robot Workspace](https://github.com/ANI717/ANI717_Robotics/tree/main/robot_ws)<br/>
[Simulation Workspace](https://github.com/ANI717/ANI717_Robotics/tree/main/simulation_ws)<br/>
[Computer Vision & Deep Learning Repository](https://github.com/ANI717/Self_Driving_CV_Repository)<br/>

## Colaborators
[Computer Fusion Laboratory (CFL) - Temple University College of Engineering](https://sites.temple.edu/cflab/people/)
* [Animesh Bala Ani](https://www.linkedin.com/in/ani717/) (Software Development)<br/>
* [Michael Nghe](https://sites.temple.edu/cflab/people/) (Data Collection)<br/>
* [Dr. Li Bai](https://engineering.temple.edu/about/faculty-staff/li-bai-lbai) (Academic Advisor)<br/>

## Design Diagram
<img src="https://github.com/ANI717/ANI717_Robotics/blob/main/Robot%20Workspace.png" alt="Robot Workspace Diagram" class="inline"/><br/>
<img src="https://github.com/ANI717/ANI717_Robotics/blob/main/Simulation%20Workspace.png" alt="Simulation Workspace Diagram" class="inline"/><br/>

## Developed ROS2 Packages
#### Common Packages:<br/>
* [ros2_deep_learning_model_to_twist_message](https://github.com/ANI717/ANI717_Robotics/tree/main/robot_ws/src/ros2_deep_learning_to_twist_message)<br/>
* [ros2_save_camera_image](https://github.com/ANI717/ANI717_Robotics/tree/main/robot_ws/src/ros2_save_camera_image)<br/>

#### Robot Packages:<br/>
* [ros2_csi_camera_publish](https://github.com/ANI717/ANI717_Robotics/tree/main/robot_ws/src/ros2_csi_camera_publish)<br/>
* [ros2_gamepad_to_twist_message](https://github.com/ANI717/ANI717_Robotics/tree/main/robot_ws/src/ros2_gamepad_to_twist_message)<br/>
* [ros2_twist_message_to_robot_motion](https://github.com/ANI717/ANI717_Robotics/tree/main/robot_ws/src/ros2_twist_message_to_robot_motion)<br/>

#### Simulation Packages:<br/>
* [ros2_keyboard_to_twist_message](https://github.com/ANI717/ANI717_Robotics/tree/main/simulation_ws/src/ros2_keyboard_to_twist_message)<br/>
* [ros2_world_simulation](https://github.com/ANI717/ANI717_Robotics/tree/main/simulation_ws/src/ros2_world_simulation)<br/>
* [ros2_robot_simulation](https://github.com/ANI717/ANI717_Robotics/tree/main/simulation_ws/src/ros2_robot_simulation)<br/>

## Download Workspace
```
git clone https://github.com/ANI717/ANI717_Robotics
```

## [Robot Workspace](https://github.com/ANI717/ANI717_Robotics/tree/main/robot_ws)
#### Build, Source & Launch Package (Gamepad)
```
cd ~/ANI717_Robotics/robot_ws/
colcon build --symlink-install && source install/local_setup.bash && ros2 launch robot_app gamepad_launch.py
```

#### Build, Source & Launch Package (Self Driving)
```
cd ~/ANI717_Robotics/robot_ws/
colcon build --symlink-install && source install/local_setup.bash && ros2 launch robot_app autonomous_launch.py
```

## [Simulation Workspace](https://github.com/ANI717/ANI717_Robotics/tree/main/simulation_ws)
#### Build, Source & Launch Package (Keyboard)
Terminal 1
```
cd ANI717_Robotics/simulation_ws/
export DISPLAY=:0
colcon build --symlink-install && source install/local_setup.bash && ros2 launch simulation_app keyboard_launch.py
```

Terminal 2 (Run following commands and select `/image` as `Image View`
```
export DISPLAY=:0
rqt
```

Terminal 3
```
cd ANI717_Robotics/simulation_ws/
source install/local_setup.bash && ros2 run ros2_keyboard_to_twist_message execute
```

#### Build, Source & Launch Package (Self Driving)
```
cd ANI717_Robotics/simulation_ws/
export DISPLAY=:0
colcon build --symlink-install && source install/local_setup.bash && ros2 launch simulation_app autonomous_launch.py
```

## Acknowledgement
[Jetbot](https://jetbot.org/master/)<br/>
[Jetbot URDF Mesh](https://github.com/aws-samples/aws-robomaker-jetbot-ros)<br/>
[AWS Robomaker Racetrack World](https://github.com/aws-robotics/aws-robomaker-racetrack-world)<br/>
