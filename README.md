<h1>Safety-Aware Robot Navigation using RL</h1>

<h2>Description</h2>
This project focuses on the collision-avoidance capability of an autonomous mobile robot in a dynamic environment using the Reinforcement Learning (RL) technique, specifically the Deep Q-Network (DQN) model. This research experiment examines the extent to which safety is ensured in an environment where an unmanned ground robot is deployed alongside humans and other mobile or fixed equipment
<br />

<h2>Hardware</h2>

<p align="center">
Matrix Formula All Code Buggy Robot: <br/>
<img src="https://i.postimg.cc/QMz0Xb06/Buggy-Robot.webp" height="40%" width="60%" alt="Disk Sanitization Steps"/>
<br />
 

<h2>Languages and Utilities Used</h2>

- <b>Python</b> 
- <b>PyTorch Library</b>
- <b>NumPy Library</b>

<h2>Environment</h2>

- <b>Visual Studio</b>

<h2>Project walk-through:</h2>
<b>Step 1</b>

- <b>Create a rule-based navigation program</b>
- <b>Create rewards and penalties for navigation pathway and sensor levels</b>

<p align="center">
Buggy Robot with Obstacles on Navigation Pathway: <br/>
<img src="https://i.postimg.cc/QdWqfs0v/20260416-220249.jpg" height="60%" width="40%" alt="Disk Sanitization Steps"/>
<br />

<b>Step 2</b>

- <b>Train the DQN model with the data collected using a well-structured set of hyperparameters</b>
- <b>Ensure the reward functions are continuously tuned to improve stability and convergence</b>

<p align="center">
DQN Training Network Architecture: <br/>
<img src="https://i.postimg.cc/TY2Y6qSN/Picture1.png" height="60%" width="80%" alt="Disk Sanitization Steps"/>
<br />

<b>Step 3</b>

- <b>Perform testing to ensure that the robot learned the trajectory pathway and obstacle detection</b>
- <b>Evaluate the testing outcomes</b>

<p align="center">
Results - (a) Action-Distribution, (b) Sensor Over Time, (c) Robot Motion Trajectory: <br/>
<img src="https://i.postimg.cc/Hs2GTq54/Screenshot-2026-05-05-022659.png" height="60%" width="60%" alt="Disk Sanitization Steps"/>
<br />

<!--
 ```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```
--!>
