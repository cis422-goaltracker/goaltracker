"""
	Names
	CIS 422
	GoalTracker
"""

from SubGoal import SubGoal as SubGoal
from Status import Status as Status
from Model import Model as Model

class SubGoalManager(object):
	"""CONSTRUCTOR FOR SUBGOALMANAGER"""
	def __init__(self):
		pass

	"""METHODS FOR SUBGOALMANAGER"""
	def addSubGoal(self, _gid, _model, _subGoalInformation, _startDate): #FUNCTION NEEDS TO BE BUILT
		subGoalList = _model.getSubGoalList(_gid) #gets the subgoal list from the model using the goal id
		sgid = _model.getNewSGID() #gets a new subgoal id from the model

		#use _subGoalInformation and sgid to create new SubGoal object
		#subGoalInformation includes {name}

		#append new SubGoal object to subGoalList

		_model.setSubGoalList(subGoalList) #sets the updated subgoallist in the model
		return _model #returns model

	def editSubGoal(self, _gid, _sgid, _model, _subGoalInformation):
		subGoal = _model.getSubGoal(_gid, _sgid) #retrieves the subgoal from the model
		subGoal.update(_subGoalInformation) #updates the contents of subgoal
		_model.setSubGoal(_gid, subGoal) #replaces old subGoal with updated subgoal in model
		return _model #returns model

	def deleteSubGoal(self, _gid, _sgid, _model): #FUNCTION NEEDS TO BE BUILT
		subGoalList = _model.getSubGoalList(_gid) #retrieves subgoal from model using goal id

		#find subGoal with matching id in subGoalList

		#remove subGoal from _subGoalList

		_model.setSubGoalList(_gid, subGoalList) #sets the updated subgoallist in the model using the goal id
		return _model #returns model

	def completeSubGoal(self, _gid, _sgid, _model, _finishDate):
		subGoal = _model.getSubGoal(_gid, _sgid) #retrieves the subgoal from the model
		subGoal.completeSubGoal(_finishDate) #calls _subgoal's complete subgoal and passes _finish date
		_model.setSubGoal(_gid, subGoal) #replaces old subgoal with updated subgoal in model
		return _model #returns model

	"""GETTERS FOR SUBGOALMANAGER"""

	"""SETTERS FOR SUBGOALMANAGER"""
		