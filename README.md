# Rob 599 Project 
The main idea of the project is to turn the ROS apple vision controller into a ROS2 apple vision controller. The vision components of the applevision controller were kept the same, but modified to run in ROS2. Additional functions were written to allow for correct movement and to utilize the UR5 forward position controller instead of moveit. Fake images are being published because the project is being run in simulation and not on the real robot with a real camera. There are three images that have been created where the apple is on the left, right, or center.  The images are being published every second and the left image is published first for about 6 seconds, the right image is published next for about 5 seconds, and the center image is being published for the rest of the time. This means that the robot arm will move right, then left, then stop moving. The next aspect is moving forward to get to the apple. This data is also fake because there are no TOF sensors hooked up to the simulation. The data is created by counting down from 50 to 0 and being published every second. 

# How to Run the Apple Vision Controller 
1. Start the UR5e in Rviz
     Run the following commands in seperate terminal (make sure to source ros2 in each terminal)
```
ros2 launch ur_robot_driver ur5e.launch.py robot_ip:=10.10.10.10 use_fake_hardware:=true
```
```
ros2 launch ur_moveit_config ur_moveit.launch.py ur_type:=ur5e
```  
2. In the rviz window move the robot to a sutable starting position (have to do before switching controller) 
   
3. Use the following command in a new terminal to switch to the forward_position_controller 
```
ros2 control switch_controllers --activate forward_position_controller --deactivate scaled_joint_trajectory_controller
```
4. Use the following command to start the servos
```
ros2 service call /servo_node/start_servo std_srvs/srv/Trigger
```

5. Use the folloing command to launch the apple vision controller
```
ros2 launch applevision_vision service.launch.py 
```
# Video 
There is a video showing the simulation and the code working. The voice over is explaining what is happening and how to run the code. 

# Things of Note 
## File Path changes
In image_pub.py, the images are provided by an abosulte path. This path will need to change to the path on your computer to run it correctly. 

In _init_.py, the model path is an absolute path. This path will need to change to the path on your computer to run it correctly. 

## Launch files
There are two launch files in the launch folder. The service.launch.py file is the one that is used for this project. It launchs the move with services set up to change the speed of the arm and the stopping distance to the apple. The other launch file move.launch.py has parameters that controllers the speed and stopping distance, instead of the services. 

## Running with Simulation 
To run the code with simulation, the UR5 drivers and moveit2 need to be installed. Otherwise, the launch file can be run and the messages showing speed being published can show how the system is working. 

## Singularities
The reason that it is important to move the UR5 arm before starting is because it starts close to a singularity (it can not move). When close to a singularity the E-stop will be engaged. Picking a starting position is important to avoiding singularities throughout the whole simulation. 


