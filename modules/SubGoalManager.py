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
	def addSubGoal(self, _gid, _model, _subGoalInformation, _startDate):
		subGoalList = _model.getSubGoalList(_gid) #gets the subgoal list from the model using the goal id
		sgid = _model.getNewSGID() #gets a new subgoal id from the model
		subGoal = SubGoal(sgid, _subGoalInformation, _startDate) #create new SubGoal object using _subGoalInformation
		subGoalList.append(subGoal) #append new SubGoal to subGoalList
		_model.setSubGoalList(subGoalList) #sets the updated subgoallist in the model
		return _model #returns model

	def editSubGoal(self, _gid, _sgid, _model, _subGoalInformation):
		subGoal = _model.getSubGoal(_gid, _sgid) #retrieves the subgoal from the model
		subGoal.update(_subGoalInformation) #updates the contents of subgoal
		_model.setSubGoal(_gid, subGoal) #replaces old subGoal with updated subgoal in model
		return _model #returns model

	def deleteSubGoal(self, _gid, _sgid, _model): #FUNCTION NEEDS TO BE BUILT
		subGoalList = _model.getSubGoalList(_gid) #retrieves subgoal from model using goal id
		for index, subGoal in enumerate(subGoalList): #cycles through subgoal list
			if subGoal.getId() == _sgid: #if subGoal's id matches _sgid
				subGoalList.pop(index) #remove subGoal from the list
		_model.setSubGoalList(_gid, subGoalList) #sets the updated subgoallist in the model using the goal id
		return _model #returns model

	def completeSubGoal(self, _gid, _sgid, _model, _finishDate):
		subGoal = _model.getSubGoal(_gid, _sgid) #retrieves the subgoal from the model
		subGoal.completeSubGoal(_finishDate) #calls _subgoal's complete subgoal and passes _finish date
		_model.setSubGoal(_gid, subGoal) #replaces old subgoal with updated subgoal in model
		return _model #returns model

	"""GETTERS FOR SUBGOALMANAGER"""

	"""SETTERS FOR SUBGOALMANAGER"""
		