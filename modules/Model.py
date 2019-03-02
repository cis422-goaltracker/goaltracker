"""
	Names
	CIS 422
	GoalTracker
"""

from Goal import Goal as Goal
import datetime as DateTime
import copy

class Model(object):
	"""CONSTRUCTOR FOR MODEL"""
	def __init__(self, _goalList, _currGID, _currSGID, _effortTrackingData):
		self.goalList = _goalList #list of goal objects
		self.currGID = _currGID #integer
		self.currSGID = _currSGID #integer
		self.effortTrackingData = _effortTrackingData #dictionary goalid-starttime pairs

	"""METHODS FOR MODEL"""
	'''GOALLIST OPERATIONS'''
	def getIncompleteGoalList(self):
		incompleteGoalList = [] #empty list to hold incomplete goals
		for goal in self.goalList: #cycles through goal list
			if not goal.isComplete(): #if the goal is not complete
				incompleteGoalList.append(goal) #append goal to incomplete goal list
		return incompleteGoalList #return incomplete goal list

	def getOverDueGoalList(self, _currentDate):
		overDueGoalList = [] #empty list to hold overdue goals
		for goal in self.goalList: #cycles through goal list
			if goal.isOverDue(_currentDate): #if the goal is not complete
				overDueGoalList.append(goal) #append goal to incomplete goal list
		return overDueGoalList #return incomplete goal list

	'''GOAL OPERATIONS'''
	def addGoal(self, _goalInformation, _startDate, _dueDate = None):
		goal = Goal(self.getNewGID(), _goalInformation, _startDate, _dueDate)
		self.goalList.append(goal)

	def editGoal(self, _gid, _goalInformation):
		for index, goal in enumerate(self.goalList):
			if goal.getId() == _gid:
				self.goalList[index].updateGoal(_goalInformation)

	def completeGoal(self, _gid, _finishDate):
		for index, goal in enumerate(self.goalList):
			if goal.getId() == _gid:
				self.goalList[index].completeGoal(_goalInformation)
				#also set all subgoals to complete

	def rescheduleGoal(self, _gid, _newDueDate):
		for index, goal in enumerate(self.goalList):
			if goal.getId() == _gid:
				self.goalList[index].reschedule(_goalInformation)

	def deleteGoal(self, _gid):
		for index, goal in enumerate(self.goalList):
			if goal.getId() == _gid:
				self.goalList.pop(index)

	'''SUBGOAL OPERATIONS'''
	def addSubGoal(self, _gid, _sgid, _subGoalInformation):
		for index, goal in enumerate(self.goalList):
			if goal.getId() == _gid:
				self.goalList[index].subGoals[_sgid] = _subGoalInformation

	def editSubGoal(self, _gid, _sgid, _subGoalInformation):
		for index, goal in enumerate(self.goalList):
			if goal.getId() == _gid:
				self.goalList[index].subGoals[_sgid] = _subGoalInformation

	def completeSubGoal(self, _gid, _sgid):
		for index, goal in enumerate(self.goalList):
			if goal.getId() == _gid:
				self.goalList[index].subGoals[_sgid]["isComplete"] = True

	def deleteSubGoal(self, _gid, _sgid):
		for index, goal in enumerate(self.goalList):
			if goal.getId() == _gid:
				self.goalList[index].subGoals.pop(_sgid)

	'''GID AND SGID OPERATIONS'''
	def getNewGID(self):
		self.currGID = self.currGID + 1 #increments current goal id
		return self.currGID #returns current goal id

	def getNewSGID(self):
		self.currSGID = self.currSGID + 1 # increments current subgoal id
		return self.currSGID #returns current subgoal id

	'''SORT OPERATIONS'''
	def categorySort(self):
		Goal.sorting = "category"
		goalList = sorted(self.getGoalList())
		self.setGoalList(goalList)

	def prioritySort(self):
		Goal.sorting = "priority"
		goalList = sorted(self.getGoalList())
		self.setGoalList(goalList)

	"""GETTERS FOR MODEL"""
	def getGoalList(self):
		return copy.deepcopy(self.goalList) #returns a copy of the Goal List

	def getCurrGID(self):
		return self.currGID #returns the current goal id

	def getEffortTrackingData(self):
		return copy.deepcopy(self.effortTrackingData) #returns the a copy of the effort tracking data

	def setEffortTrackingData(self, _effortTrackingData):
		self.effortTrackingData = _effortTrackingData #sets the effort tracking data to the passed _effortTrackingData