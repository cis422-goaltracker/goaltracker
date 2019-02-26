"""
	Names
	CIS 422
	GoalTracker
"""

from Goal import Goal as Goal
from Model import Model as Model

class SortManager(object):
	"""CONSTRUCTORS FOR SORTMANAGER"""
	def __init__(self):
		pass

	"""METHODS FOR SORTMANAGER"""
	def categorySort(self, _model): #FUNCTION NEEDS TO BE BUILT
		goalList = _model.getGoalList() #gets goallist from the model

		#sort goalList by category (alphabetically, if same category, then by priority)

		_model.setGoalList(goalList) #sets the updated goal list in the model
		return _model #returns the model

	def prioritySort(self, _model): #FUNCTION NEEDS TO BE BUILT
		goalList = _model.getGoalList() #gets goallist from the model

		#sort goalList by priority (numerically, if same priority, then by category)

		_model.setGoalList(goalList) #sets the updated goal list in the model
		return _model #returns the model

	def dueDateSort(self, _model): #FUNCTION NEEDS TO BE BUILT
		goalList = _model.getGoalList() #gets goallist from the model

		#sort goalList by anticipatedFinishDate (date, if the same anticipatedFinishDate, then by goal name [alphabetically])

		_model.setGoalList(goalList) #sets the updated goal list in the model
		return _model  #returns the model
	"""GETTERS FOR SORTMANAGER"""


	"""SETTERS FOR SORTMANAGER"""
	