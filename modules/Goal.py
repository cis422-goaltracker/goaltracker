"""
	Names
	CIS 422
	GoalTracker
"""

from datetime import datetime, timedelta
import datetime
import copy

class SubGoal(object):
	"""CONSTRUCTORS FOR SUBGOAL"""
	def __init__(self, _id):
		self.id = _id
		self.name = ""
		self.isCompleted = False

	"""METHODS FOR SUBGOAL"""
	def update(self, _subGoalInformation):
		self.name = _subGoalInformation["name"]

	def complete(self):
		self.isCompleted = True

	def isComplete(self):
		return self.isCompleted

	def toString(self):
		if self.isCompleted:
			return "Name: " + self.name + " | Status: Complete"
		else:
			return "Name: " + self.name + " | Status: Incomplete"

	"""GETTERS FOR SUBGOAL"""
	def getId(self):
		return self.id

	def getName(self):
		return self.name

class Goal(object):
	"""CONSTRUCTORS FOR GOAL"""
	def __init__(self, _id):
		#constant features
		self.id = _id #integer
		self.startDate = datetime.datetime.now() #DateTime

		#user updateable features
		self.name = "" #string
		self.category = "" #string
		self.priority = 1 #integer
		self.memo = "" #string
		self.dueDate = None #DateTime

		#programmatically updateable features
		self.initialDueDate = None #DateTime
		self.finishDate = None #DateTime/Null
		self.effortTracker = {} #dictionary of <finish datetime, start datetime> pairs
		self.subGoals = [] #list of SubGoals
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
		if not self.hasDueDate() and self.initialDueDate == None:
			self.initialDueDate = _goalInformation["dueDate"]
		self.dueDate = _goalInformation["dueDate"]

	def complete(self, _finishDate):
		self.finishDate = _finishDate #sets the finish date to the passed finish date

	def isComplete(self):
		return self.finishDate != None #if finish date is not null, it is complete

	def isOverDue(self):
		if self.hasDueDate():
			return self.dueDate < datetime.datetime.now() #if current date is greater than due date, its overdue
		else:
			return False

	'''Subgoal Operations'''
	def addSubGoal(self, _sgid):
		self.subGoals.append(SubGoal(_sgid))

	def updateSubGoal(self, _sgid, _subGoalInformation):
		self.subGoals[self.getIndex(_sgid)].update(_subGoalInformation)

	def completeSubGoal(self, _sgid):
		self.subGoals[self.getIndex(_sgid)].complete()

	def deleteSubGoal(self, _sgid):
		self.subGoals.pop(self.getIndex(_sgid))

	def getSubGoal(self, _sgid):
		return self.subGoals[self.getIndex(_sgid)]

	def getIndex(self, _sgid):
		for index, subgoal in enumerate(self.subGoals):
			if subgoal.getId() == _sgid:
				return index
		return -1

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
		else:
			priority = "Super High"

		status = None
		if self.isComplete():
			status = "Complete"
		else:
			status = "Incomplete"

		if self.hasDueDate():
			return "Name: " + self.name + " | Due Date: " + self.dueDate.toString("yyyy.MM.dd") + " | Category: " + self.category + " | Priority: " + priority + " | Status: " + status
		else:
			return "Name: " + self.name + "| Category: " + self.category + " | Priority: " + priority + " | Status: " + status

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
		return self.memo #returns the Goal Memo

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
	def setSortingMethod(self, _sortingMethod):
		self.sortingMethod = _sortingMethod