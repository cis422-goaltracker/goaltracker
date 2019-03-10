"""
    Authors: Weigang An, Isaac Lance
    Date: 03/09/2019
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

        @return: (Model)

        @purpose: Tries open shelve and extract the model, if can't find the data, generates a
        an empty model and returns that instead
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

        @return: None

        @purpose: Stores model in the shelve
        '''
        _fileName = self.fileName if _fileName == None else _fileName #defaults to original file name unless a new one is specified
        db = shelve.open(_fileName) #open file
        try:
            db['model'] = _model #store model in shelve
            db.close() #close file
        except:
            db.close() #close file
