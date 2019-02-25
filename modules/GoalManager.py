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
	def addGoal(self, _model, _goalInformation, _startDate): #FUNCTION NEEDS TO BE BUILT
		goalList = _model.getGoalList() #retrieves goalList from the model
		gid = _model.getNewGID() #retreieves a new goal id from the model

		#use _goalInformation and gid to create new Goal object
		#_goalInformation contains {name, category, priority}

		#append new Goal object to goalList

		_model.setGoalList(goalList) #sets the updated goallist in the model
		return _model #returns the model

	def editGoal(self, _gid, _model, _goalInformation):
		goal = _model.getGoal() #retrieves the goal from the model
		goal.update(_goalInformation) #updates the contents of goal
		_model.setGoal(goal) #replaces old goal with updated subgoal in model
		return _model #returns model

	def deleteGoal(self, _gid, _model, _goal): #FUNCTION NEEDS TO BE BUILT
		goalList = _model.getGoalList() #gets the goallist from the model

		#find goal with matching id in goalList

		#remove goal from _goalList

		_model.setGoalList(goalList) #sets the updated goallist in the model
		return _model #returns the model

	def completeGoal(self, _gid, _model, _finishDate):
		goal = _model.getGoal(_gid) #gets the goal from the model using the goal id
		goal.completeGoal(_finishDate) #calls _goal's complete goal and passes _finish date
		_model.setGoal(goal) #sets the updated goal in the model
		return _model #returns the model

	"""GETTERS FOR GOALMANAGER"""


	"""SETTERS FOR GOALMANAGER"""
	