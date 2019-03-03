"""
	Names
	CIS 422
	GoalTracker
"""

from Goal import Goal
from datetime import datetime, timedelta
import copy

class Model(object):
	"""CONSTRUCTOR FOR MODEL"""
	def __init__(self, _goalList, _currGID, _currSGID, _effortTrackingData):
		'''
		@param: _goalList (list) - 
		@param: _currGID (integer) - 
		@param: _currSGID (integer) - 
		@param: _effortTrackingData (dictionary) - 

		@return: None

		@purpose
		'''
		self.goalList = _goalList #list of goal objects
		self.currGID = _currGID #integer
		self.currSGID = _currSGID #integer
		self.effortTrackingData = _effortTrackingData #dictionary goalid-starttime pairs

	"""METHODS FOR MODEL"""
	'''********************GOALLIST OPERATIONS********************'''
	def getCompleteGoalList(self):
		'''
		@param: None

		@return: (list) - 

		@purpose
		'''
		return [goal for goal in self.goalList if goal.isComplete()]

	def getCurrentGoalList(self):
		'''
		@param: None

		@return: (list) - 

		@purpose
		'''
		return [goal for goal in self.goalList if not goal.isComplete()]

	def getOverDueGoalList(self):
		'''
		@param: None

		@return: (list) - 

		@purpose
		'''
		return [goal for goal in self.goalList if goal.isOverDue()]

	def getGoalList(self):
		'''
		@param: None

		@return (list) - 

		@purpose
		'''
		return copy.deepcopy(self.goalList) #returns a copy of the Goal List

	'''********************GOAL OPERATIONS********************'''
	def addGoal(self, _goalInformation, _subGoalsNames, _dueDate = None):
		'''
		@param: _goalInformation (dictionary) - 
		@param: _subGoalsNames (list) - 
		@param: _dueDate (datetime) - 

		@return: None

		@purpose
		'''
		subGoals = {}
		for name in _subGoalsNames:
			subGoals[self.getNewSGID()] = {"name": name, "isComplete": False}
		goal = Goal(self.getNewGID(), _goalInformation, subGoals, _dueDate)
		self.goalList.append(goal)

	def editGoal(self, _gid, _goalInformation):
		'''
		@param: _gid (integer) - 
		@param: _goalInformation (dictionary) - 

		@return: None

		@purpose
		'''
		for index, goal in enumerate(self.goalList):
			if goal.getId() == _gid:
				self.goalList[index].update(_goalInformation)

	def completeGoal(self, _gid, _finishDate = datetime.now()):
		'''
		@param: _gid (integer) - 
		@param: _finishDate (datetime) - 

		@return: None

		@purpose
		'''
		for index, goal in enumerate(self.goalList):
			if goal.getId() == _gid:
				self.goalList[index].complete(_finishDate)
				for key in self.goalList[index].keys():
					self.goalList[index][key]["isComplete"] = True

	def rescheduleGoal(self, _gid, _newDueDate):
		'''
		@param: _gid (integer) - 
		@param: _newDueDate (datetime) - 

		@return: None

		@purpose
		'''
		for index, goal in enumerate(self.goalList):
			if goal.getId() == _gid:
				self.goalList[index].reschedule(_goalInformation)

	def deleteGoal(self, _gid):
		'''
		@param: _gid (integer) - 

		@return: None

		@purpose
		'''
		for index, goal in enumerate(self.goalList):
			if goal.getId() == _gid:
				self.goalList.pop(index)

	'''********************SUBGOAL OPERATIONS********************'''
	def addSubGoal(self, _gid, _sgid, _subGoalInformation):
		'''
		@param: _gid (integer) - 
		@param: _sgid (integer) - 
		@param: _subGoalInformation (dictionary) - 

		@return: None

		@purpose
		'''
		for index, goal in enumerate(self.goalList):
			if goal.getId() == _gid:
				self.goalList[index].subGoals[_sgid] = _subGoalInformation

	def editSubGoal(self, _gid, _sgid, _subGoalInformation):
		'''
		@param: _gid (integer) - 
		@param: _sgid (integer) - 
		@param: _subGoalInformation (dictionary) - 

		@return: None

		@purpose
		'''
		for index, goal in enumerate(self.goalList):
			if goal.getId() == _gid:
				self.goalList[index].subGoals[_sgid] = _subGoalInformation

	def completeSubGoal(self, _gid, _sgid):
		'''
		@param: _gid (integer) - 
		@param: _sgid (integer) - 

		@return: None

		@purpose
		'''
		for index, goal in enumerate(self.goalList):
			if goal.getId() == _gid:
				self.goalList[index].subGoals[_sgid]["isComplete"] = True

	def deleteSubGoal(self, _gid, _sgid):
		'''
		@param: _gid (integer) - 
		@param: _sgid (integer) - 

		@return: None

		@purpose
		'''
		for index, goal in enumerate(self.goalList):
			if goal.getId() == _gid:
				self.goalList[index].subGoals.pop(_sgid)

	'''********************EFFORT TRACKER OPERATIONS********************'''
	def startEffortTracker(self, _gid):
		'''
		@param: _gid (integer) - 

		@return: None

		@purpose
		'''
		self.effortTrackingData[_gid] = datetime.now()

	def isEffortTracking(self, _gid):
		'''
		@param: _gid (integer) - 

		@return: (boolean) - 

		@purpose
		'''
		return _gid in self.effortTrackingData

	def stopEffortTracking(self, _gid):
		'''
		@param: _gid (integer) - 

		@return: None

		@purpose
		'''
		for index, goal in enumerate(self.goalList):
			if goal.getId() == _gid:
				self.goalList[index].addEffortTrack(datetime.now(), self.effortTrackingData.pop(_gid))

	def manuallyInputEffort(self, _gid, _startTime, _finishTime):
		'''
		@param: _gid (integer) - 
		@param: _startTime (datetime) - 
		@param: _finishTime (datetime) - 

		@return: None

		@purpose
		'''
		for index, goal in enumerate(self.goalList):
			if goal.getId() == _gid:
				self.goalList[index].addEffortTrack(_finishTime, _startTime)

	def getEffortTrackingData(self):
		'''
		@param: None

		@return: (dictionary) - 

		@purpose
		'''
		return copy.deepcopy(self.effortTrackingData) #returns the a copy of the effort tracking data

	'''********************GID AND SGID OPERATIONS********************'''
	def getNewGID(self):
		'''
		@param: None

		@return: (integer) - 

		@purpose
		'''
		self.currGID = self.currGID + 1 #increments current goal id
		return self.currGID #returns current goal id

	def getNewSGID(self):
		'''
		@param: None

		@return: (integer) - 

		@purpose
		'''
		self.currSGID = self.currSGID + 1 # increments current subgoal id
		return self.currSGID #returns current subgoal id

	'''********************SORT OPERATIONS********************'''
	def categorySort(self):
		'''
		@param: None

		@return: None

		@purpose: This method sets the goal list to be sorted by the category attribute
		'''
		# Goal.sorting = "category"
		for index, goal in enumerate(self.goalList):
			self.goalList[index].setSortMethod("category")
		self.goalList = sorted(self.getGoalList())

	def prioritySort(self):
		'''
		@param: None

		@return: None

		@purpose: This method sets the goal list to be sorted by the priority attribute
		'''
		# Goal.sorting = "priority"
		for index, goal in enumerate(self.goalList):
			self.goalList[index].setSortMethod("priority")
		self.goalList = sorted(self.getGoalList())
