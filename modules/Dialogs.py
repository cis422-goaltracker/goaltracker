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
UI_PATHS = {"MainWindow": "../UI/MainWindow.ui", "AddEditViewGoal": "../UI/AddEditViewGoal.ui", "AddEditViewSubGoal": "../UI/AddEditViewSubGoal.ui"}

class AddEditViewGoal(QDialog):
    def __init__(self, _model, _goalState, _method): #FUNCTION NEEDS TO BE BUILT
        '''
        @param:

        @return:

        @purpose:
        '''
        super(AddEditViewGoal, self).__init__()
        
        loadUi(UI_PATHS["AddEditViewGoal"], self) # Load the AddEditViewGoal UI

        #Class Variables
        self.model = _model
        self.goalState = _goalState

        #Signals
        self.push_add_subgoal.clicked.connect(self.loadAddSubGoal)
        self.push_complete_subgoal.clicked.connect(self.loadCompleteSubGoal)
        self.push_edit_view_subgoal.clicked.connect(self.loadEditViewSubGoal)
        self.push_delete_subgoal.clicked.connect(self.loadDeleteSubGoal)
        self.push_save.clicked.connect(self.loadSaveGoal)
        self.push_cancel.clicked.connect(self.loadCancelGoal)

        #load components with the state information
        #subgoals will be loaded into listview with subgoal tostring
        #subgoal will be loaded into combo box with name and id

    @pyqtSlot()
    def loadAddSubGoal(self): #FUNCTION NEEDS TO BE BUILT
        '''
        @param:

        @return:

        @purpose:
        '''
        #create default state of subgoal

        #open add AddEditViewGoal window, pass it goal state and state

        #subgoals reloaded from state information into listview with subgoal tostring
        #subgoals reloaded from state information into combo box with name and id

        pass

    @pyqtSlot()
    def loadCompleteSubGoal(self): #FUNCTION NEEDS TO BE BUILT
        '''
        @param:

        @return:

        @purpose:
        '''
        #sets subgoal to complete
        pass

    @pyqtSlot()
    def loadEditViewSubGoal(self): #FUNCTION NEEDS TO BE BUILT
        '''
        @param:

        @return:

        @purpose:
        '''
        #get subgoalid from combobox

        #get subgoal from model using subgoalid

        #create state of subgoal from subgoal

        #open AddEditViewSubGoal window, passes it goal state and state

        #subgoals reloaded from state information into listview with subgoal tostring
        #subgoals reloaded from state information into combo box with name and id
        pass

    @pyqtSlot()
    def loadDeleteSubGoal(self): #FUNCTION NEEDS TO BE BUILT
        '''
        @param:

        @return:

        @purpose:
        '''
        #delete subgoal
        pass

    @pyqtSlot()
    def loadSaveGoal(self): #FUNCTION NEEDS TO BE BUILT
        '''
        @param:

        @return:

        @purpose:
        '''
        #update goal in model to accept the current state of subgoals and any changed information

        #exit dialog
        pass

    @pyqtSlot()
    def loadCancelGoal(self): #FUNCTION NEEDS TO BE BUILT
        '''
        @param:

        @return:

        @purpose:
        '''
        #discard state

        #exit dialog
        pass


class AddEditViewSubGoal(QDialog):
    def __init__(self, _goalState, _subGoalState, _method, _parent): #FUNCTION NEEDS TO BE BUILT
        '''
        @param:

        @return:

        @purpose:
        '''
        super(AddEditViewSubGoal, self).__init__()
        
        loadUi(UI_PATHS["AddEditViewSubGoal"], self) # Load the AddEditViewSubGoal UI

        #Class Variables
        self.goalState = _goalState
        self.state = _state
        self.parent = _parent

        #Signals
        self.push_save.clicked.connect(self.loadSaveSubGoal)
        self.push_cancel.clicked.connect(self.loadCancelSubGoal)

        #load components with state information

    @pyqtSlot()
    def loadSaveSubGoal(self): #FUNCTION NEEDS TO BE BUILT
        '''
        @param:

        @return:

        @purpose:
        '''
        #update subGoal information in goalState

        #exit dialog
        pass

    @pyqtSlot()
    def loadCancelSubGoal(self): #FUNCTION NEEDS TO BE BUILT
        '''
        @param:

        @return:

        @purpose:
        '''
        #discard subGoal state

        #exit dialog
        pass