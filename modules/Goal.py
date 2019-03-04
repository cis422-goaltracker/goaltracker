"""
	Names
	CIS 422
	GoalTracker
"""

from datetime import datetime, timedelta
import copy

class Goal(object):
	"""CONSTRUCTORS FOR GOAL"""
	def __init__(self, _id, _goalInformation, _subGoals, _dueDate):
		self.id = _id #integer
		self.name = _goalInformation["name"] #string
		self.category = _goalInformation["category"] #string
		self.priority = _goalInformation["priority"] #integer
		self.memo = _goalInformation["memo"] #string
		self.startDate = datetime.now() #DateTime
		self.dueDate = _dueDate #DateTime
		self.initialDueDate = _dueDate #DateTime
		self.finishDate = None #DateTime/Null
		self.effortTracker = {} #dictionary of <finish datetime, start datetime> pairs
		self.subGoals = _subGoals #dictionary of SubGoals
		self.sortingMethod = "category" #string
	
	"""Special Methods"""
	#Override less than, aka "<", so self<right_goal
	def __lt__(self, other):
		if self.sortingMethod == "category":
			return (self.category.lower() < other.category.lower())
		if self.sortingMethod == "priority":
			return (self.priority < other.priority)
		return("ERROR: This should never happen (Sort error)")

	"""METHODS FOR GOAL"""
	'''Goal Operations'''
	def hasDueDate(self):
		return self.dueDate != None

	def reschedule(self, _dueDate):
		if not self.hasDueDate():
			self.initialDueDate = _dueDate
		self.dueDate = _dueDate #sets the due date to the new due date

	def hasBeenRescheduled(self):
		if self.hasDueDate():
			return self.dueDate != self.initialDueDate #if due date and initial due date are same, return false, otherwise true
		else:
			return None

	def update(self, _goalInformation):
		self.name = _goalInformation["name"] #sets the name to the passed name
		self.category = _goalInformation["category"] #sets the category to the passed category
		self.priority = _goalInformation["priority"] #sets the priority to the passed priority
		self.memo = _goalInformation["memo"]

	def complete(self, _finishDate):
		self.finishDate = _finishDate #sets the finish date to the passed finish date

	def isComplete(self):
		return self.finishDate != None #if finish date is not null, it is complete

	def isOverDue(self):
		if self.hasDueDate():
			return self.dueDate < datetime.now() #if current date is greater than due date, its overdue
		else:
			return False

	'''Effort Tracker Operations'''
	def addEffortTrack(self, _finishTime, _startTime):
		self.effortTracker[_finishTime] = _startTime #adds a key-value pair of <finish time, start time> to effort tracker

	'''To String Operations'''
	def toString(self):
		priority = None
		if self.priority == 3:
			priority = "Low"
		elif self.priority == 2:
			priority = "Medium"
		elif self.priority == 1:
			priority = "High"
		if self.hasDueDate():
			return "Name: " + self.name + " | Due Date: " + self.dueDate.strftime("%m/%d/%Y") + " | Category: " + self.category + " | Priority: " + priority
		else:
			return "Name: " + self.name + "| Category: " + self.category + " | Priority: " + priority

	"""GETTERS FOR GOAL"""
	def getId(self):
		return self.id #returns the Goal ID

	def getName(self):
		return self.name #returns the Goal Name

	def getCategory(self):
		return self.category #returns the Goal Category

	def getPriority(self):
		return self.priority #returns the Goal Priority

	def getMemo(self):
		return self.memor #returns the Goal Memo

	def getStartDate(self):
		return self.startDate #returns the Goal Start Date

	def getDueDate(self):
		return self.dueDate #returns the Goal Due Date

	def getInitialDueDate(self):
		return self.initialDueDate #returns the Goal Initial Due Date

	def getFinishDate(self):
		return self.finishDate #returns the Goal Finish Date

	def getEffortTracker(self):
		return copy.deepcopy(self.effortTracker) #returns a copy of the Effort Tracker of the Goal

	def getSubGoals(self):
		return copy.deepcopy(self.subGoals) #returns a copy of the Sub Goals of the Goal

	def getSortingMethod(self):
		return self.sortingMethod

	"""SETTERS FOR GOAL"""
	def setSubGoals(self, _subGoals):
		self.subGoals = _subGoals #sets the subGoals to the passed _subGoals

	def setSortingMethod(self, _sortingMethod):
		self.sortingMethod = _sortingMethod