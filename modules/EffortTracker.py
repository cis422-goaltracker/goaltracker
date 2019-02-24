"""
	Names
	CIS 422
	GoalTracker
"""

from Goal import Goal as Goal

class EffortTracker(object):
	"""CONSTRUCTOR FOR EFFORTTRACKER"""
	def __init__(self):
		pass

	"""METHODS FOR EFFORTTRACKER"""
	def startEffortTracker(self, _goal, _trackingDict, _startTime):
		#create key-value pair <_goal, _startTime>

		#add pair to the tracking dictionary

		#return tracking dictionary
		pass

	def isEffortTracking(self, _goal, _trackingDict):
		#check if _goal is in the tracking dictionary by checking id, true if it is, false if it isn't
		pass

	def stopEffortTracker(self, _goal, _trackingDict, _finishTime):
		#pops the pair with the _goal as the key out of tracking dictionary

		#finds the elapsed time between _finishTime and _startTime

		#creates new entry in _goal's effort tracker with <date, elapsed time>
		#if date already exists, add new elapsed time to old time

		#return _goal
		pass

	"""GETTERS FOR EFFORTTRACKER"""

	"""SETTERS FOR EFFORTTRACKER"""
