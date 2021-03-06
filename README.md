# robotics
Robotics subject Cin-UFPE
TiaGO robot

## Get robocinV3 in installation folder: 
../tiago_public_ws/src/tiago_simulation/tiago_gazebo/worlds
Move robotics to ../tiago_public_ws
1º Step:

    `catkin build robotics`

2º Step:
     `Close terminal (troubleshoot of processes.`

3º Step: mapeamento
    `cd tiago_public_ws/`
    `source ./devel/setup.bash`

    `roslaunch robotics Mapping.launch robot:=titanium world:=robocinV3`

3.1º Step: navegação
    `cd tiago_public_ws/`
    `source ./devel/setup.bash`

   ` roslaunch robotics Navigation.launch robot:=titanium world:=robocinV3`

## Create and allow running scripts
1º Step:
	`catkin build robotics`
	`chmod +x goTo.py` (cd to folder of goTo.py [scripts])

2º Step:
	`rosrun robotics goTo.py room0` (Navigation.lauch must be running)


## Creating publisher and reading subscriber:
1º Step:
Create msg folder and create a file like PersonDistance.msg
Inside this file shows the name and type of variable


2º Step:
Add rows like are in CMakeLists.txt and package.xml from robotics package to recognize the folder msg at the import of the script pubSubs_example.py
chmod +x PersonDistance.msg

3º Step:
`catkin build` 

4º Step:
Open a second terminal
`source ./devel/setup.bash ` (Must run in all terminal tab or add this command to the .bashrc)
`rosrun robotics pubSubs_example.py`

5º Step:
Open third terminal
`source ./devel/setup.bash` (Must run in all terminal tab or add this command to the .bashrc)
rostopic list (check if the closest_person topic was created, if so is legen...waitforit...dary kk)

6º Step (Optional):

Move robot with `rosrun robotics goTo.py room[X]` or `rosrun key_teleop key_teleop.py` to see the rostopic echo closest_person showing the values of the topic

Detect people:

Must run:
`roslaunch pal_person_detector_opencv detector.launch image:=/xtion/rgb/image_raw`

`rosrun image_view image_view image:=/person_detector/debug`

`rosrun robotics person.py`

## Recognize objects

1º Step:
Be on: ../robotics/scripts folder

2º Step:
`rosrun robotics feat_match.py cocacola.jpg` (The jpg file is the object that he will try to compare)

3º Step
`rostopic echo vision_object`
Optional:
`rosrun robotics feat_match_bkp.py "cocacola.jpg" "image.png"` Compare two images
__________________
Links:
1. http://wiki.ros.org/Robots/TIAGo/Tutorials/Installation/TiagoSimulation
2. https://github.com/heitorrapela/at-my-home
3. http://wiki.ros.org/Robots/TIAGo/Tutorials
__________________


Show commands:(running gazebo)

`rostopic echo -c /amcl_pose `
`rostopic info /amcl_pose `
`rostopic list`
`rosnode info goTo.py `


rostopic type /amcl_pose
geometry_msgs/PoseWithCovarianceStamped
