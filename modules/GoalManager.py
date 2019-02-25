"""
	Names
	CIS 422
	GoalTracker
"""

from Goal import Goal as Goal
from Status import Status as Status
from Model import Model as Model

class GoalManager(object):
	"""CONSTRUCTOR FOR GOALMANAGER"""
	def __init__(self):
		pass

	"""METHODS FOR GOALMANAGER"""
	def addGoal(self, _model, _goalInformation, _startDate, _anticipatedFinishDate):
		goalList = _model.getGoalList() #retrieves goalList from the model
		gid = _model.getNewGID() #retreieves a new goal id from the model
		goal = Goal(gid, _goalInformation, _startDate, _anticipatedFinishDate) #create new Goal object using _goalInformation
		goalList.append(goal) #append new Goal to goalList
		_model.setGoalList(goalList) #sets the updated goallist in the model
		return _model #returns the model

	def editGoal(self, _gid, _model, _goalInformation):
		goal = _model.getGoal(_gid) #retrieves the goal from the model
		goal.update(_goalInformation) #updates the contents of goal
		_model.setGoal(goal) #replaces old goal with updated subgoal in model
		return _model #returns model

	def rescheduleGoal(self, _gid, _model, _anticipatedFinishDate): #FUNCTION NEEDS TO BE BUILT
		goal = _model.getGoal(_gid)

		#reschedule goal to anticipatedFinishDate (function in Goal)

		_model.setGoal(goal)
		return _model

	def isOverDue(self, _gid, _model): #FUNCTION NEEDS TO BE BUILT
		goal = _model.getGoal(_gid)

		#check if goal is overdue (function in Goal)

		_model.setGoal(goal)
		return _model

	def deleteGoal(self, _gid, _model, _goal):
		goalList = _model.getGoalList() #gets the goallist from the model
		for index, goal in enumerate(goalList): #cycles through goal list
			if goal.getId() == _gid: #if goal's id matches _gid
				goalList.pop(index) #remove subGoal from the list
		_model.setGoalList(goalList) #sets the updated goallist in the model
		return _model #returns the model

	def completeGoal(self, _gid, _model, _finishDate):
		goal = _model.getGoal(_gid) #gets the goal from the model using the goal id
		goal.completeGoal(_finishDate) #calls _goal's complete goal and passes _finish date
		_model.setGoal(goal) #sets the updated goal in the model
		return _model #returns the model

	"""GETTERS FOR GOALMANAGER"""


	"""SETTERS FOR GOALMANAGER"""
	