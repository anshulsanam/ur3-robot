import vrep
import time
import numpy as np
from math import cos, sin
from scipy.linalg import expm,logm


# Get distances measurements from each joint center to base frame (useful for forward kinematics)
def get_joint():
	X = []
	Y = []
	Z = []
	result,vector=vrep.simxGetObjectPosition(clientID, joint_one_handle,base_handle,vrep.simx_opmode_blocking)
	X.append(vector[0])
	Y.append(vector[1])
	Z.append(vector[2])
	result,vector=vrep.simxGetObjectPosition(clientID, joint_two_handle,base_handle,vrep.simx_opmode_blocking)
	X.append(vector[0])
	Y.append(vector[1])
	Z.append(vector[2])
	result,vector=vrep.simxGetObjectPosition(clientID, joint_three_handle,base_handle,vrep.simx_opmode_blocking)
	X.append(vector[0])
	Y.append(vector[1])
	Z.append(vector[2])
	result,vector=vrep.simxGetObjectPosition(clientID, joint_four_handle,base_handle,vrep.simx_opmode_blocking)
	X.append(vector[0])
	Y.append(vector[1])
	Z.append(vector[2])
	result,vector=vrep.simxGetObjectPosition(clientID, joint_five_handle,base_handle,vrep.simx_opmode_blocking)
	X.append(vector[0])
	Y.append(vector[1])
	Z.append(vector[2])
	result,vector=vrep.simxGetObjectPosition(clientID, joint_six_handle,base_handle,vrep.simx_opmode_blocking)
	X.append(vector[0])
	Y.append(vector[1])
	Z.append(vector[2])
	result,vector=vrep.simxGetObjectPosition(clientID, end_handle,base_handle,vrep.simx_opmode_blocking)
	X.append(vector[0])
	Y.append(vector[1])
	Z.append(vector[2])
	X = np.round(X, decimals = 3)
	Y = np.round(Y, decimals = 3)
	Z = np.round(Z, decimals = 3)
	return X,Y,Z

# Function that used to move joints
def SetJointPosition(theta):
	vrep.simxSetJointTargetPosition(clientID, joint_one_handle, theta[0], vrep.simx_opmode_oneshot)
	time.sleep(0)
	vrep.simxSetJointTargetPosition(clientID, joint_two_handle, theta[1], vrep.simx_opmode_oneshot)
	time.sleep(0)
	vrep.simxSetJointTargetPosition(clientID, joint_three_handle, theta[2], vrep.simx_opmode_oneshot)
	time.sleep(0)
	vrep.simxSetJointTargetPosition(clientID, joint_four_handle, theta[3], vrep.simx_opmode_oneshot)
	time.sleep(0)
	vrep.simxSetJointTargetPosition(clientID, joint_five_handle, theta[4], vrep.simx_opmode_oneshot)
	time.sleep(0)
	vrep.simxSetJointTargetPosition(clientID, joint_six_handle, theta[5], vrep.simx_opmode_oneshot)
	time.sleep(3.6)


# Function that used to read joint angles
def GetJointAngle():
	result, theta1 = vrep.simxGetJointPosition(clientID, joint_one_handle, vrep.simx_opmode_blocking)
	if result != vrep.simx_return_ok:
		raise Exception('could not get 1 joint variable')
	result, theta2 = vrep.simxGetJointPosition(clientID, joint_two_handle, vrep.simx_opmode_blocking)
	if result != vrep.simx_return_ok:
		raise Exception('could not get 2 joint variable')
	result, theta3 = vrep.simxGetJointPosition(clientID, joint_three_handle, vrep.simx_opmode_blocking)
	if result != vrep.simx_return_ok:
		raise Exception('could not get 3 joint variable')
	result, theta4 = vrep.simxGetJointPosition(clientID, joint_four_handle, vrep.simx_opmode_blocking)
	if result != vrep.simx_return_ok:
		raise Exception('could not get 4 joint variable')
	result, theta5 = vrep.simxGetJointPosition(clientID, joint_five_handle, vrep.simx_opmode_blocking)
	if result != vrep.simx_return_ok:
		raise Exception('could not get 5 joint variable')
	result, theta6 = vrep.simxGetJointPosition(clientID, joint_six_handle, vrep.simx_opmode_blocking)
	if result != vrep.simx_return_ok:
		raise Exception('could not get 6 joint variable')
	theta = np.array([[theta1],[theta2],[theta3],[theta4],[theta5],[theta6]])
	return theta



# ======================================================================================================= #
# ======================================= Start Simulation ============================================== #
# ======================================================================================================= #

# Close all open connections (Clear bad cache)
vrep.simxFinish(-1)
# Connect to V-REP (raise exception on failure)
clientID = vrep.simxStart('127.0.0.1', 19997, True, True, 5000, 5)
if clientID == -1:
	raise Exception('Failed connecting to remote API server')

# ======================================== Setup "handle"  =========================================== #

'''
# Print object name list
result,joint_name,intData,floatData,stringData = vrep.simxGetObjectGroupData(clientID,vrep.sim_appobj_object_type,0,vrep.simx_opmode_blocking)
print(stringData)
'''

# Get "handle" to the base of robot
result, base_handle = vrep.simxGetObjectHandle(clientID, 'UR10_link1_visible', vrep.simx_opmode_blocking)
if result != vrep.simx_return_ok:
	raise Exception('could not get object handle for base frame')
	
# Get "handle" to the all joints of robot
result, joint_one_handle = vrep.simxGetObjectHandle(clientID, 'UR10_joint1', vrep.simx_opmode_blocking)
if result != vrep.simx_return_ok:
	raise Exception('could not get object handle for first joint')
result, joint_two_handle = vrep.simxGetObjectHandle(clientID, 'UR10_joint2', vrep.simx_opmode_blocking)
if result != vrep.simx_return_ok:
	raise Exception('could not get object handle for second joint')
result, joint_three_handle = vrep.simxGetObjectHandle(clientID, 'UR10_joint3', vrep.simx_opmode_blocking)
if result != vrep.simx_return_ok:
	raise Exception('could not get object handle for third joint')
result, joint_four_handle = vrep.simxGetObjectHandle(clientID, 'UR10_joint4', vrep.simx_opmode_blocking)
if result != vrep.simx_return_ok:
	raise Exception('could not get object handle for fourth joint')
result, joint_five_handle = vrep.simxGetObjectHandle(clientID, 'UR10_joint5', vrep.simx_opmode_blocking)
if result != vrep.simx_return_ok:
	raise Exception('could not get object handle for fifth joint')
result, joint_six_handle = vrep.simxGetObjectHandle(clientID, 'UR10_joint6', vrep.simx_opmode_blocking)
if result != vrep.simx_return_ok:
	raise Exception('could not get object handle for sixth joint')

# Get "handle" to the end-effector of robot
result, end_handle = vrep.simxGetObjectHandle(clientID, 'UR10_link7_visible', vrep.simx_opmode_blocking)
if result != vrep.simx_return_ok:
	raise Exception('could not get object handle for end effector')
# ==================================================================================================== #

# Start simulation
vrep.simxStartSimulation(clientID, vrep.simx_opmode_oneshot)

# ******************************** Your robot control code goes here  ******************************** #
time.sleep(0.1)
counter = vrep.simxGetFloatSignal(clientID, "counter", vrep.simx_opmode_streaming)[1]
vrep.simxSetFloatSignal(clientID, "RG2_open", 1, vrep.simx_opmode_oneshot)
previousCounter = counter
# Goal_joint_angles = np.array([[0,0,-0.5*np.pi,0.5*np.pi,-0.5*np.pi,-0.5*np.pi], \
# 							[0.5*np.pi,0,-0.5*np.pi,0.5*np.pi,0.5*np.pi,-0.5*np.pi],\
# 							[-0.5*np.pi,-0.5*np.pi,-0.5*np.pi,0,-0.5*np.pi,-0.5*np.pi]])
Goal_joint_angles = np.array([\
							[0,0,0,0,0,0], \
							[0.5*np.pi,0,0,0,0,0], \
							[0,0.25*np.pi,0,0,0,0], \
							[0,0,0.5*np.pi,0,0,0], \
							[0,0,0,0.5*np.pi,0,0], \
							[0,0,0,0,0.5*np.pi,0], \
							[0,0,0,0,0,0.5*np.pi], \
							# [0,0,0.45*np.pi,0,-0.5*np.pi,0], \
							[0,0.1*np.pi,0.35*np.pi,0.05*np.pi,-0.5*np.pi,0], \
							])
for i in range(len(Goal_joint_angles)):
	SetJointPosition(Goal_joint_angles[i])
	time.sleep(0.25)
	X,Y,Z = get_joint()
	vrep.simxAddStatusbarMessage(clientID, "end effector relative to base: (" + str(X[5]) + ", " + str(Y[5]) + ", " + str(Z[5]) + ").", vrep.simx_opmode_oneshot)
	time.sleep(0.25)
current_joint_angle = [0,0,0,0,0,0]
SetJointPosition(current_joint_angle)
# X,Y,Z = get_joint()
# print(X,Y,Z)
while counter < 10.0:
	break
	counter = vrep.simxGetFloatSignal(clientID, "counter", vrep.simx_opmode_buffer)[1]
	if counter != previousCounter:
		current_joint_angle[0] += np.pi * 2
		SetJointPosition(current_joint_angle)
		previousCounter = counter
	time.sleep(0.5)

# Wait two seconds
time.sleep(2)
# **************************************************************************************************** #

# Stop simulation
vrep.simxStopSimulation(clientID, vrep.simx_opmode_oneshot)
# Before closing the connection to V-REP, make sure that the last command sent out had time to arrive. You can guarantee this with (for example):
vrep.simxGetPingTime(clientID)
# Close the connection to V-REP
vrep.simxFinish(clientID)
print("==================== ** Simulation Ended ** ====================")

# ======================================================================================================= #
# ======================================== End Simulation =============================================== #
# ======================================================================================================= #