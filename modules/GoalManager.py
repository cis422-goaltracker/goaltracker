"""
	Names
	CIS 422
	GoalTracker
"""

from Goal import Goal
from Status import Status
from Model import Model
import datetime as DateTime

class GoalManager(object):
	"""CONSTRUCTOR FOR GOALMANAGER"""
	def __init__(self):
		pass

	"""METHODS FOR GOALMANAGER"""
	'''Goal Modification Operations'''
	def addGoal(self, _model, _goalInformation, _startDate, _dueDate):
		goalList = _model.getGoalList() #retrieves goalList from the model
		gid = _model.getNewGID() #retreieves a new goal id from the model
		goal = Goal(gid, _goalInformation, _startDate, _dueDate) #create new Goal object using _goalInformation
		goalList.append(goal) #append new Goal to goalList
		_model.setGoalList(goalList) #sets the updated goallist in the model
		return _model #returns the model

	def editGoal(self, _gid, _model, _goalInformation):
		goal = _model.getGoal(_gid) #retrieves the goal from the model
		goal.update(_goalInformation) #updates the contents of goal
		_model.setGoal(goal) #replaces old goal with updated goal in model
		return _model #returns model

	def rescheduleGoal(self, _gid, _model, _dueDate):
		goal = _model.getGoal(_gid) #retrieves the goal from the model
		goal.reschedule(_dueDate) #reschedules goal to the new due date
		_model.setGoal(goal) #replaces old goal with update goal in the model
		return _model #returns model

	def deleteGoal(self, _gid, _model):
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
	