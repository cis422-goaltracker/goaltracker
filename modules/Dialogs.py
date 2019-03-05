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

from Goal import Goal, SubGoal
from Model import Model
from FileManager import FileManager
from AnalysisGenerator import AnalysisGenerator

# Global variable for storing UI files (HH)
UI_PATHS = {"MainWindow": "../UI/MainWindow.ui", "AddEditViewGoal": "../UI/AddEditViewGoal.ui", "AddEditViewSubgoal": "../UI/AddEditViewSubgoal.ui"}

class AddEditViewGoal(QDialog):
    def __init__(self, _model, _goalid = None): #FUNCTION NEEDS TO BE BUILT
        '''
        @param:

        @return:

        @purpose:
        '''
        super(AddEditViewGoal, self).__init__()
        
        loadUi(UI_PATHS["AddEditViewGoal"], self) # Load the AddEditViewGoal UI

        #Class Variables
        self.model = _model
        self.goalid = _goalid
        self.comboIndex = -1

        #Signals
        self.push_effort.clicked.connect(self.toggleEffortTracker)
        self.checkBox_due_date.clicked.connect(self.toggleDueDate)
        self.push_add_subgoal.clicked.connect(self.loadAddSubGoal)
        self.push_complete_subgoal.clicked.connect(self.loadCompleteSubGoal)
        self.push_edit_view_subgoal.clicked.connect(self.loadEditViewSubGoal)
        self.push_delete_subgoal.clicked.connect(self.loadDeleteSubGoal)
        self.push_save.clicked.connect(self.loadSaveGoal)
        self.push_cancel.clicked.connect(self.loadCancelGoal)

        self.refreshListViewAndComboBox()

        if self.goalid == None:
            self.setWindowTitle('Add Goal')
            self.goalid = self.model.addGoal()

            #load default information (@WEIGANG DO HERE)

        else:
            self.setWindowTitle('Edit/View Goal')
            
            #load goal information (@WEIGANG DO HERE)
            

    '''********************PYQTSLOT OPERATIONS********************'''
    @pyqtSlot()
    def toggleEffortTracker(self): #FUNCTION NEEDS TO BE BUILT
        pass

    @pyqtSlot()
    def toggleDueDate(self): #FUNCTION NEEDS TO BE BUILT
        pass

    @pyqtSlot()
    def loadAddSubGoal(self):
        '''
        @param:

        @return:

        @purpose:
        '''
        window = AddEditViewSubGoal(self, self.model, self.goalid) #open add AddEditViewGoal window, pass it model
        if window.exec():
            self.refreshListViewAndComboBox()

    @pyqtSlot()
    def loadCompleteSubGoal(self):
        '''
        @param:

        @return:

        @purpose:
        '''
        if moreThanZeroGoals():
            subgoalid = self.getSGIDFromComboBox() #get subgoalid from combobox
            self.model.completeSubGoal(self.goalid, subgoalid)
            self.refreshListViewAndComboBox()
        else:
            print("No Subgoals")

    @pyqtSlot()
    def loadEditViewSubGoal(self):
        '''
        @param:

        @return:

        @purpose:
        '''
        if moreThanZeroGoals():
            subgoalid = self.getSGIDFromComboBox() #get subgoalid from combobox
            window = AddEditViewSubGoal(self, self.model, self.goalid, subgoalid) #open AddEditViewSubGoal window, passes it model and subgoal id
            if window.exec():
                self.refreshListViewAndComboBox()
        else:
            print("No Subgoals")

    @pyqtSlot()
    def loadDeleteSubGoal(self):
        '''
        @param:

        @return:

        @purpose:
        '''
        if self.moreThanZeroGoals():
            subgoalid = self.getSGIDFromComboBox() #get subgoalid from combobox
            self.model.deleteSubGoal(self.goalid, subgoalid)
            self.refreshListViewAndComboBox()
        else:
            print("No Subgoals")

    @pyqtSlot()
    def loadSaveGoal(self): #FUNCTION NEEDS TO BE BUILT
        '''
        @param:

        @return:

        @purpose:
        '''
        #update goal information in model

        self.accept() #exit dialog

    @pyqtSlot()
    def loadCancelGoal(self):
        '''
        @param:

        @return:

        @purpose:
        '''
        self.model.deleteGoal(self.goalid) #delete goal from model
        self.close() #exit dialog

    '''********************CLASS METHODS OPERATIONS********************'''
    def moreThanZeroGoals(self):
        '''
        @param:

        @return:

        @purpose:
        '''
        return self.comboBox.count() != 0

    def setChosenItem(self, index):
        '''
        @param:

        @return:

        @purpose:
        '''
        self.comboIndex = index

    def getSGIDFromComboBox(self):
        '''
        @param:

        @return:

        @purpose:
        '''
        return self.comboBox.itemData(self.comboIndex) #return the SGID currently in combobox

    def addToListView(self, _subGoalList):
        '''
        @param:

        @return:

        @purpose:
        '''
        #cycle through list, to string every goal and place into listview
        self.listWidget.clear()
        for subGoal in _subGoalList:
            self.listWidget.addItem(subGoal.toString())

    def addToComboBox(self, _subGoalList):
        '''
        @param:

        @return:

        @purpose:
        '''
        #cycle through list, get name and goalid of every goal and place into combobox
        self.comboBox.clear()
        for subGoal in _subGoalList:
            self.comboBox.addItem(subGoal.getName(), subGoal.getId())

    def refreshListViewAndComboBox(self):
        goalList = self.model.getGoalList()
        if len(goalList) != 0:
            subGoalList = self.model.getSubGoalList(self.goalid)
            self.addToListView(subGoalList)
            self.addToComboBox(subGoalList)


class AddEditViewSubGoal(QDialog):
    def __init__(self, _parent, _model, _goalid, _subgoalid = None): #FUNCTION NEEDS TO BE BUILT
        '''
        @param:

        @return:

        @purpose:
        '''
        super(AddEditViewSubGoal, self).__init__()
        
        loadUi(UI_PATHS["AddEditViewSubgoal"], self) # Load the AddEditViewSubGoal UI

        #Class Variables
        self.parent = _parent
        self.model = _model
        self.goalid = _goalid
        self.subgoalid = _subgoalid

        #Signals
        self.push_save.clicked.connect(self.loadSaveSubGoal)
        self.push_cancel.clicked.connect(self.loadCancelSubGoal)

        if self.subgoalid == None:
            self.setWindowTitle('Add Subgoal')
            self.subgoalid = self.model.addSubGoal(self.goalid)

            #load default information
            
        else:
            self.setWindowTitle('Edit/View Subgoal')

            #load subgoal information

    @pyqtSlot()
    def loadSaveSubGoal(self): #FUNCTION NEEDS TO BE BUILT
        '''
        @param:

        @return:

        @purpose:
        '''
        #update subGoal information model

        self.accept() #exit dialog

    @pyqtSlot()
    def loadCancelSubGoal(self):
        '''
        @param:

        @return:

        @purpose:
        '''
        self.model.deleteSubGoal(self.goalid, self.subgoalid)
        self.close() #exit dialog
