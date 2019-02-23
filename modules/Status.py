"""
	Names
	CIS 422
	GoalTracker
"""

class Status(object):
	"""CONSTRUCTOR FOR STATUS"""
	def __init__(self):
		self.statuses = {
			0: "Success", #successful operation
			1: "IO ERROR - FILENOTFOUND", #file read error
			2: "IO ERROR - CORRUPTFILE", #file read error
			3: "IO ERROR - FAILEDTOWRITE", #file write error
			4: "IO ERROR - INVALIDFILENAME", #file write error
			5: "DG ERROR - GOALNOTFOUND", #delete goal error
			6: "DSG ERROR - SUBGOALNOTFOUND" #delete subgoal error
		}

	"""METHODS FOR STATUS"""


	"""GETTERS FOR STATUS"""
	def getStatus(self, _code):
		return self.statuses[_code]

	"""SETTERS FOR STATUS"""
