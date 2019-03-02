"""
	Names
	CIS 422
	GoalTracker
"""

class Status(object):
	"""CONSTRUCTOR FOR STATUS"""
	def __init__(self):
		self.statuses = {
			0: "SUCCESS", #successful operation
			1: "IO ERROR - FILE NOT FOUND", #file read error
			2: "IO ERROR - CORRUPT FILE", #file read error
			3: "IO ERROR - FAILED TO WRITE", #file write error
			4: "IO ERROR - INVALID FILE NAME", #file write error
			5: "DG ERROR - GOAL NOT FOUND", #delete goal error
			6: "DSG ERROR - SUB GOAL NOT FOUND", #delete subgoal error
			7: "FG ERROR - GOAL NOT FOUND", #find goal error
			8: "FSG ERROR - SUB GOAL NOT FOUND", #find subgoal error
			9: "DD ERROR - DUE DATE DOES NOT EXIST" #due date error
		} #dictionary

	"""METHODS FOR STATUS"""


	"""GETTERS FOR STATUS"""
	def getStatus(self, _code):
		return self.statuses[_code]

	"""SETTERS FOR STATUS"""
