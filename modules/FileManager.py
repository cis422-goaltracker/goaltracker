"""
	Names
	CIS 422
	GoalTracker
"""

from Goal import Goal as Goal
from SubGoal import SubGoal as SubGoal
from Status import Status as Status
from Model import Model as Model
import shelve

class FileManager(object):
	"""CONSTRUCTOR FOR FILEMANAGER"""
	def __init__(self):
		pass
		
	"""METHODS FOR FILEMANAGER"""
	'''Load Operations'''
	def load(self, _fileName):
		self.fileName = _fileName #sets default file name for FileManager
		try:
			db = shelve.open(self.fileName) #open file
			goalList = db['goalList'] #get list of goal objects from shelve
			currGID = db['currGID'] #get currGID from shelve
			currSGID = db['currSGID'] #get currSGID from shelve
			effortTrackingData = db['effortTrackingData'] #get Effort Tracking Data from shelve
			db.close() #close file
			model = Model(goalList, currGID, currSGID, effortTrackingData) #create a Model object which contains a list of Goal objects, currGID, currSGID, EffortTrackingData
		except:
			model = Model([], 0, 0, {}) #create an empty Model object where everything is set to 0 or empty
		return model #

	'''Save Operations'''
	def save(self, _model, _fileName=None):
		_fileName = self.fileName if _fileName == None else _fileName #defaults to original file name unless a new one is specified
		try:
			db = shelve.open(_fileName) #open file
			db['goalList'] = _model.getGoalList() #get goal list from model and store into shelve
			db['currGID'] = _model.getCurrGID() #get currGID from model and store into shelve
			db['currSGID'] = _model.getCurrSGID() #get currSGID from model and store into shelve
			db['effortTrackingData'] = _model.getEffortTrackingData() #get effort tracking data from model and store into shelve
			db.close() #close file
			return 0 #Success
		except:
			#return IO STATUS
			return 1 #IO ERROR

	"""GETTERS FOR FILEMANAGER"""
	def getFileName(self):
		return self.fileName #return the file name

	"""SETTERS FOR FILEMANAGER"""
