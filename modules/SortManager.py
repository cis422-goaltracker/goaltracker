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

		return goalList #returns the category sorted list

	def prioritySort(self, _model): #FUNCTION NEEDS TO BE BUILT
		goalList = _model.getGoalList() #gets goallist from the model

		#sort goalList by priority (numerically, if same priority, then by category)

		return goalList #returns the priority sorted list

	"""GETTERS FOR SORTMANAGER"""


	"""SETTERS FOR SORTMANAGER"""
	