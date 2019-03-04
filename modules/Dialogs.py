"""
    Names: Holly Hardin (HH)
    CIS 422
    GoalTracker
        Reference [0]: https://stackoverflow.com/questions/21213853/pyside-how-to-delete-widgets-from-gridlayout

"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from datetime import datetime

from Goal import Goal
from Model import Model
from FileManager import FileManager
from AnalysisGenerator import AnalysisGenerator as AnalysisGenerator

# Global variable for storing UI files (HH)
UI_PATHS = {"MainWindow": "../UI/MainWindow.ui", "AddEditViewGoal": "../UI/AddEditViewGoal.py", "AddEditViewSubGoal": "../UI/AddEditViewSubGoal.py"}

class AddEditViewGoal(QDialog):
    def __init__(self, _model):
        super(AddEditViewGoal, self).__init__()
        
        loadUi(UI_PATHS["AddEditViewGoal"], self) # Load the AddEditViewGoal UI

        #Class Variables
        self.model = _model

        #Signals
        self.push_add_subgoal.clicked.connect(self.loadAddSubGoal)
        self.push_complete_subgoal.clicked.connect(self.loadCompleteSubGoal)
        self.push_edit_view_subgoal.clicked.connect(self.loadEditViewSubGoal)
        self.push_delete_subgoal.clicked.connect(self.loadDeleteSubGoal)
        self.push_save.clicked.connect(self.loadSaveGoal)
        self.push_cancel.clicked.connect(self.loadCancelGoal)

    @pyqtSlot()
    def loadAddSubGoal(self):
        pass

    @pyqtSlot()
    def loadCompleteSubGoal(self):
        pass

    @pyqtSlot()
    def loadEditViewSubGoal(self):
        pass

    @pyqtSlot()
    def loadDeleteSubGoal(self):
        pass

    @pyqtSlot()
    def loadSaveGoal(self):
        pass

    @pyqtSlot()
    def loadCancelGoal(self):
        pass


class AddEditViewSubGoal(QDialog):
    def __init__(self, _model, _parent):
        super(AddEditViewSubGoal, self).__init__()
        
        loadUi(UI_PATHS["AddEditViewSubGoal"], self) # Load the AddEditViewSubGoal UI

        #Class Variables
        self.model = _model
        self.parent = _parent

        #Signals
        self.push_save.clicked.connect(self.loadSaveSubGoal)
        self.push_cancel.clicked.connect(self.loadCancelSubGoal)

    @pyqtSlot()
    def loadSaveSubGoal(self):
        pass

    @pyqtSlot()
    def loadCancelSubGoal(self):
        pass