"""
	Names
	CIS 422
	GoalTracker
"""

from Goal import Goal, SubGoal
from datetime import datetime, timedelta
import copy

class Model(object):
	"""CONSTRUCTOR FOR MODEL"""
	def __init__(self, _goalList, _currGID, _currSGID, _effortTracker):
		'''
		@param: _goalList (list) - 
		@param: _currGID (integer) - 
		@param: _currSGID (integer) - 
		@param: _effortTracker (dictionary) - 

		@return: None

		@purpose
		'''
		self.goalList = _goalList #list of goal objects
		self.currGID = _currGID #integer
		self.currSGID = _currSGID #integer
		self.effortTracker = _effortTracker #dictionary goalid-starttime pairs

	"""METHODS FOR MODEL"""
	'''********************GOALLIST OPERATIONS********************'''
	def getCompletedGoalList(self):
		'''
		@param: None

		@return: (list) - A list of Goal objects that have been completed

		@purpose: This function filters the goalList leaving only Goals that have been completed.
		It then returns the filtered list.
		'''
		return [goal for goal in self.goalList if goal.isComplete()]

	def getCurrentGoalList(self):
		'''
		@param: None

		@return: (list) - A list of Goal objects that are currently active

		@purpose: This function filters the goalList leaving only Goals that have not been completed.
		It then returns the filtered list.
		'''
		return [goal for goal in self.goalList if not goal.isComplete()]

	def getOverDueGoalList(self):
		'''
		@param: None

		@return: (list) - A list of Goal objects that are over due

		@purpose: This function filters the goalList leaving only Goals that are over due.
		It then returns the filtered list.
		'''
		return [goal for goal in self.goalList if goal.isOverDue() and not goal.isComplete()]

	def getGoalList(self):
		'''
		@param: None

		@return (list) - A list of all Goal objects

		@purpose: This function makes a copy of the goalList. It then returns the copied list.
		'''
		return copy.deepcopy(self.goalList) #returns a copy of the Goal List

	'''********************GOAL OPERATIONS********************'''
	def addGoal(self):
		'''
		@param: None

		@return: None

		@purpose: Creates a Goal object and then appends it to the goalList
		'''
		newGID = self.getNewGID()
		self.goalList.append(Goal(newGID))
		return newGID

	def editGoal(self, _gid, _goalInformation):
		'''
		@param: _gid (integer) - a unique integer representing a goal
		@param: _goalInformation (dictionary) - a dictionary containing a "name" (string), 
		a "category" (string), a "priority" (integer), a "memo" (string), and a "dueDate" (DateTime)

		@return: None

		@purpose
		'''
		self.goalList[self.getIndex(_gid)].update(_goalInformation)

	def completeGoal(self, _gid, _finishDate = datetime.now()):
		'''
		@param: _gid (integer) - 
		@param: _finishDate (datetime) - 

		@return: None

		@purpose
		'''
		self.goalList[self.getIndex(_gid)].complete(_finishDate)
		#cycle through and complete all subgoals

	def deleteGoal(self, _gid):
		'''
		@param: _gid (integer) - 

		@return: None

		@purpose
		'''
		self.goalList.pop(self.getIndex(_gid))

	def getGoal(self, _gid):
		'''
		@param: _gid (integer) - 

		@return: (Goal) - 

		@purpose
		'''
		return self.goalList[self.getIndex(_gid)]

	'''********************SUBGOALLIST OPERATIONS********************'''
	def getSubGoalList(self, _gid):
		'''
		@param: _gid (integer) - 

		@return: None

		@purpose
		'''
		return self.goalList[self.getIndex(_gid)].getSubGoalList()

	'''********************SUBGOAL OPERATIONS********************'''
	def addSubGoal(self, _gid):
		'''
		@param: _gid (integer) - 

		@return: None

		@purpose
		'''
		newSGID = self.getNewSGID()
		self.goalList[self.getIndex(_gid)].addSubGoal(newSGID)
		return newSGID

	def editSubGoal(self, _gid, _sgid, _subGoalInformation):
		'''
		@param: _gid (integer) - 
		@param: _sgid (integer) - 
		@param: _subGoalInformation (dictionary) - 

		@return: None

		@purpose
		'''
		self.goalList[self.getIndex(_gid)].updateSubGoal(_sgid, _subGoalInformation)

	def completeSubGoal(self, _gid, _sgid):
		'''
		@param: _gid (integer) - 
		@param: _sgid (integer) - 

		@return: None

		@purpose
		'''
		self.goalList[self.getIndex(_gid)].completeSubGoal(_sgid)

	def deleteSubGoal(self, _gid, _sgid):
		'''
		@param: _gid (integer) - 
		@param: _sgid (integer) - 

		@return: None

		@purpose
		'''
		self.goalList[self.getIndex(_gid)].deleteSubGoal(_sgid)

	def getSubGoal(self, _gid, _sgid):
		'''
		@param: _gid (integer) - 
		@param: _sgid (integer) - 

		@return: None

		@purpose
		'''
		return self.goalList[self.getIndex(_gid)].getSubGoal(_sgid)

	'''********************EFFORT TRACKER OPERATIONS********************'''
	def startEffortTracker(self, _gid):
		'''
		@param: _gid (integer) - 

		@return: None

		@purpose
		'''
		self.effortTracker[_gid] = datetime.now()

	def isEffortTracking(self, _gid):
		'''
		@param: _gid (integer) - 

		@return: (boolean) - 

		@purpose
		'''
		return _gid in self.effortTracker

	def stopEffortTracker(self, _gid):
		'''
		@param: _gid (integer) - 

		@return: None

		@purpose: This method takes the _gid to find the goal in
		'''
		self.goalList[self.getIndex(_gid)].addEffortTrack(datetime.now(), self.effortTracker.pop(_gid))

	def manuallyInputEffort(self, _gid, _startTime, _finishTime):
		'''
		@param: _gid (integer) - 
		@param: _startTime (datetime) - 
		@param: _finishTime (datetime) - 

		@return: None

		@purpose: This method takes the _gid to find the goal in the goal list, then it adds an
		effort track to the goal with _startTime and _finishTime
		'''
		self.goalList[self.getIndex(_gid)].addEffortTrack(_finishTime, _startTime)

	def getEffortTracker(self):
		'''
		@param: None

		@return: (dictionary) - 

		@purpose: This method returns a copy of the effort tracking data
		'''
		return copy.deepcopy(self.effortTracker) #returns the a copy of the effort tracking data

	'''********************GID AND SGID OPERATIONS********************'''
	def getNewGID(self):
		'''
		@param: None

		@return: (integer) - 

		@purpose: This method generates a new goal id and then returns it
		'''
		self.currGID = self.currGID + 1 #increments current goal id
		return self.currGID #returns current goal id

	def getNewSGID(self):
		'''
		@param: None

		@return: (integer) - 

		@purpose: This method generates a new subgoal id and then returns it
		'''
		self.currSGID = self.currSGID + 1 # increments current subgoal id
		return self.currSGID #returns current subgoal id

	def getCurrGID(self):
		'''
		@param:

		@return:

		@purpose:
		'''
		return self.currGID

	def getCurrSGID(self):
		'''
		@param:

		@return:

		@purpose:
		'''
		return self.currSGID

	'''********************SORT OPERATIONS********************'''
	def categorySort(self):
		'''
		@param: None

		@return: None

		@purpose: This method sets the goal list to be sorted by the category attribute
		'''
		for index, goal in enumerate(self.goalList):
			self.goalList[index].setSortingMethod("category")
		self.goalList = sorted(self.getGoalList())

	def prioritySort(self):
		'''
		@param: None

		@return: None

		@purpose: This method sets the goal list to be sorted by the priority attribute
		'''
		for index, goal in enumerate(self.goalList):
			self.goalList[index].setSortingMethod("priority")
		self.goalList = sorted(self.getGoalList())

	'''********************MISCELLANEOUS OPERATIONS********************'''
	def getIndex(self, _gid):
		'''
		@param:

		@return:

		@purpose:
		'''
		for index, goal in enumerate(self.goalList):
			if goal.getId() == _gid:
				return index
		return -1