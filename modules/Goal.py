"""
	Names
	CIS 422
	GoalTracker
"""

from SubGoal import SubGoal as SubGoal
import datetime as DateTime
import copy

class Goal(object):
	"""Class Variables"""
	#Sorting variable determines the sorting behavior of the goallist
	#This should be priority, category, or duedate (attributes of goals)
	sorting = "category"

	"""CONSTRUCTORS FOR GOAL"""
	def __init__(self, _id, _goalInformation, _startDate, _dueDate = None):
		self.id = _id #integer
		self.name = _goalInformation["name"] #string
		self.category = _goalInformation["category"] #string
		self.priority = _goalInformation["priority"] #integer
		self.startDate = _startDate #DateTime
		self.dueDate = _dueDate #DateTime
		self.initialDueDate = _dueDate #DateTime
		self.finishDate = None #DateTime/Null
		self.effortTracker = {} #dictionary of date-elapsedtime pairs
		self.subGoals = [] #list of SubGoals
	
	"""Special Methods"""
	#Override less than, aka "<", so self<right_goal
	def __lt__(self, other):
		sort = Goal.sorting
		if sort == "category": #sort by category		
			return (self.category.lower() < other.category.lower()) #returns the comparison operation for sorting
		if sort == "priority": #sort by priority
			return (self.priority < other.priority) #returns the comparison operation for sorting
		return("ERROR: This should never happen (Sort error)") #returns an error

	"""METHODS FOR GOAL"""
	'''Goal Operations'''
	def reschedule(self, _dueDate):
		self.dueDate = _dueDate #sets the due date to the new due date

	def hasDueDate(self):
		return self.dueDate != None

	def hasBeenRescheduled(self):
		return self.dueDate == self.initialDueDate #if due date and initial due date are same, return true, otherwise false

	def updateGoal(self, _goalInformation):
		self.name = _goalInformation["name"] #sets the name to the passed name
		self.category = _goalInformation["category"] #sets the category to the passed category
		self.priority = _goalInformation["priority"] #sets the priority to the passed priority

	def completeGoal(self, _finishDate):
		self.finishDate = _finishDate #sets the finish date to the passed finish date

	def isComplete(self):
		return self.finishDate != None #if finish date is not null, it is complete

	def isOverDue(self, _currentDate):
		return self.dueDate < _currentDate #if current date is greater than due date, its overdue

	'''Effort Tracker Operations'''
	def addEffortTrack(self, _date, _elapsedtime):
		if _date in self.effortTracker: #checks if date already exists in effort tracker
			self.effortTracker[_date] = self.effortTracker[_date] + _elapsedtime #if it already exists, add elapsed times together
		else:
			self.effortTracker[_date] = _elapsedtime #else adds a key-value pair of <date, elapsetime> to effort tracker

	"""GETTERS FOR GOAL"""
	def getId(self):
		return self.id #returns the Goal ID

	def getName(self):
		return self.name #returns the Goal Name

	def getCategory(self):
		return self.category #returns the Goal Category

	def getPriority(self):
		return self.priority #returns the Goal Priority

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

	"""SETTERS FOR GOAL"""
	def setSubGoals(self, _subGoals):
		self.subGoals = _subGoals #sets the subGoals to the passed _subGoals