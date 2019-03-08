"""
	Names
	CIS 422
	GoalTracker
"""
#System Imports
import shelve

#Module Imports
from Model import Model

class FileManager(object):
	"""CONSTRUCTOR FOR FILEMANAGER"""
	def __init__(self, _fileName):
		self.fileName = _fileName #sets default file name for FileManager
		
	"""METHODS FOR FILEMANAGER"""
	def load(self):
		'''
        @param: None

        @return:

        @purpose:
        '''
		db = shelve.open(self.fileName) #open file
		try:
			model = db['model'] #gets model from shelve
			db.close() #close file
			return model #returns model
		except:
			db.close() #close file
			return Model([], 0, 0, {}) #create an empty Model object where everything is set to 0 or empty

	def save(self, _model, _fileName=None):
		'''
        @param: _model (Model)

        @return:

        @purpose:
        '''
		_fileName = self.fileName if _fileName == None else _fileName #defaults to original file name unless a new one is specified
		db = shelve.open(_fileName) #open file
		try:
			db['model'] = _model #store model in shelve
			db.close() #close file
			return _model #Success
		except:
			db.close() #close file
			return None #IO ERROR
