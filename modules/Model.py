"""
	Names
	CIS 422
	GoalTracker
"""

from Goal import Goal
from SubGoal import SubGoal
from Status import Status

class Model(object):
	"""CONSTRUCTOR FOR MODEL"""
	def __init__(self, _goalList, _currGID, _currSGID, _effortTrackingData):
		self.goalList = _goalList #list of goal objects
		self.currGID = _currGID #integer
		self.currSGID = _currSGID #integer
		self.effortTrackingData = _effortTrackingData #dictionary goalid-starttime pairs

	"""METHODS FOR MODELVIEW"""
	'''GOALLIST OPERATIONS'''
	def getIncompleteGoalList(self):
		incompleteGoalList = [] #empty list to hold incomplete goals
		for goal in self.goalList: #cycles through goal list
			if not goal.isComplete(): #if the goal is not complete
				incompleteGoalList.append(goal) #append goal to incomplete goal list
		return incompleteGoalList #return incomplete goal list

	def getOverDueGoalList(self):
		overDueGoalList = [] #empty list to hold overdue goals
		for goal in self.goalList: #cycles through goal list
			if goal.isOverDue(): #if the goal is not complete
				overDueGoalList.append(goal) #append goal to incomplete goal list
		return overDueGoalList #return incomplete goal list

	'''GOAL OPERATIONS'''
	def getGoal(self, _gid):
		for goal in self.goalList: #cycles through goal list
			if goal.getId() == _gid: #if current goal's id matches _gid
				return goal #return the goal
		return None #if not found, return Null

	def setGoal(self, _goal):
		for index, goal in enumerate(self.goalList): #cycles through goalList
			if goal.getId() == _goal.getId(): #if current goal's id matches _goal's id
				self.goalList[index] = _goal #replace goal with _goal

	'''SUBGOALLIST OPERATIONS'''
	def getSubGoalList(self, _gid):
		for goal in self.goalList: #cycle through goalList
			if goal.getId() == _gid: #if current goal's id matches _gid
				return goal.getSubGoals() #return goal's subgoal list
		return None #if not found return Null

	def setSubGoalList(self, _gid, _subGoalList):
		for goal in self.goalList: #cycles through goalList
			if goal.getId() == _gid: #if current goal's id matches _goal's id
				goal.setSubGoals(_subGoalList) #replace subGoals with new _subGoalList

	'''SUBGOAL OPERATIONS'''
	def getSubGoal(self, _gid, _sgid):
		subGoals = self.getSubGoalList(_gid) #gets list of subgoals using _gid
		if subGoals != None: #if subgoals is not null
			for subGoal in subGoals: #cycles through subgoals
				if subGoal.getId() == _sgid: #if subgoal's id matches _sgid
					return subGoal #return subgoal
			return None #return null if subgoal not found
		else:
			return None #return null if goal not found

	def setSubGoal(self, _gid, _subGoal):
		subGoals = self.getSubGoalList(_gid) #gets list of subgoals using _gid
		if subGoals != None: #if subGoals is not null
			for index, subGoal in enumerate(subGoals): #cycles through subgoals
				if subGoal.getId() == _subGoal.getId(): #if subGoal's id matches _subGoal's id
					subGoals[index] = _subGoal #replaces subGoal with _subGoal in subGoals
					self.setSubGoalList(_gid, subGoals) #set subGoalList in goal with updated GoalList
		else:
			return None #returns null if goal not found

	'''GID AND SGID OPERATIONS'''
	def getNewGID(self):
		self.currGID = self.currGID + 1 #increments current goal id
		return self.currGID #returns current goal id

	def getNewSGID(self):
		self.currSGID = self.currSGID + 1 # increments current subgoal id
		return self.currSGID #returns current subgoal id

	'''SORT OPERATIONS'''
	def categorySort(self): #FUNCTION NEEDS TO BE BUILT
		Goal.sorting = "category"
		goalList = sorted(self.getGoalList())
		self.setGoalList(goalList)

	def prioritySort(self): #FUNCTION NEEDS TO BE BUILT
		Goal.sorting = "priority"
		goalList = sorted(self.getGoalList())
		self.setGoalList(goalList)

	def dueDateSort(self): #FUNCTION NEEDS TO BE BUILT
		Goal.sorting = "duedate"
		goalList = sorted(self.getGoalList())
		self.setGoalList(goalList)

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