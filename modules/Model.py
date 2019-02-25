"""
	Names
	CIS 422
	GoalTracker
"""

from Goal import Goal as Goal
from SubGoal import SubGoal as SubGoal
from Status import Status as Status

class Model(object):
	"""CONSTRUCTOR FOR MODEL"""
	def __init__(self, _goalList, _currGID, _currSGID, _effortTrackingData):
		self.goalList = _goalList
		self.currGID = _currGID
		self.currSGID = _currSGID
		self.effortTrackingData = _effortTrackingData

	"""METHODS FOR MODELVIEW"""
	'''GOAL OPERATIONS'''
	def getGoal(self, _gid): #FUNCTION NEEDS TO BE BUILT
		#cycles through goalList
		#if current goal's id is _gid, return goal
		#if not found, raise a goal not found error
		pass

	def setGoal(self, _goal): #FUNCTION NEEDS TO BE BUILT
		#cycles through goalList
		#if current goal's id is _goal's id, replace goal with _goal
		#if not found, raise a goal not found error
		pass

	'''SUBGOAL OPERATIONS'''
	def getSubGoal(self, _gid, _sgid): #FUNCTION NEEDS TO BE BUILT
		#cycles through goalList
		#if current goal's id is _gid, cycle through subgoals
		#if subgoal's id is _sgid, return subgoal
		#if not found, raise a subgoal not found error
		pass

	def setSubGoal(self, _gid, _subgoal): #FUNCTION NEEDS TO BE BUILT
		#cycles through goalList, if current goal's id is _gid, then cycle through subgoals
		#if current subgoal's id is _subgoal's id, replace subgoal with _subgoal
		#if not found, raise a subgoal not found error
		pass

	'''SUBGOALLIST OPERATIONS'''
	def getSubGoalList(self, _gid): #FUNCTION NEEDS TO BE BUILT
		#cycles through goalList
		#if current goal's id is _gid, return the subgoal list of that goal
		pass

	def setSubGoalList(self, _gid, _subgoalList): #FUNCTION NEEDS TO BE BUILT
		#cycles through goalList
		#if current goal's id is _gid, set the subgoallist to _subGoalList

		pass

	'''GID AND SGID OPERATIONS'''
	def getNewGID(self): #FUNCTION NEEDS TO BE BUILT
		#increment _currGID
		#return _currGID
		pass

	def getNewSGID(self): #FUNCTION NEEDS TO BE BUILT
		#increment _currSGID
		#return _currSGID
		pass

	"""GETTERS FOR MODELVIEW"""
	def getGoalList(self):
		return self.goalList.copy() #returns a copy of the Goal List

	def getCurrGID(self):
		return self.currGID #returns the current goal id

	def getCurrSGID(self):
		return self.currSGID #returns the current subgoal id

	def getEffortTrackingData(self):
		return self.effortTrackingData.copy() #returns the a copy of the effort tracking data

	"""SETTERS FOR MODELVIEW"""
	def setGoalList(self, _goalList):
		self.goalList = _goalList #sets the goal list to the passed _goalList

	def setCurrGID(self, _gid):
		self.currGID = _gid #sets the current goal id to the passed _gid

	def setCurrSGID(self, _sgid):
		self.currSGID = _sgid #sets the current subgoal id to the passed _sgid

	def setEffortTrackingData(self, _effortTrackingData):
		self.effortTrackingData = _effortTrackingData #sets the effort tracking data to the passed _effortTrackingData