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
from enum import Enum

from Goal import Goal
from Model import Model
from FileManager import FileManager
from AnalysisGenerator import AnalysisGenerator as AnalysisGenerator

from Dialogs import AddEditViewGoal, AddEditViewSubGoal

# Global variable for storing UI files (HH)
UI_PATHS = {"MainWindow": "../UI/MainWindow.ui", "AddEditViewGoal": "../UI/AddEditViewGoal.py", "AddEditViewSubGoal": "../UI/AddEditViewSubGoal.py"}

class State(Enum):
	CURRENT = 1
	OVERDUE = 2
	COMPLETED = 3
	ALL = 4

class MainWindow(QMainWindow):
    def __init__(self, _model):
        super(MainWindow, self).__init__()
        loadUi(UI_PATHS["MainWindow"], self) # Load the Main Window UI

        #Class Variables
        self.model = _model
        self.state = State.CURRENT
        
        #Signals
        self.push_CurrentGoals.clicked.connect(self.loadCurrentGoals)
        self.push_OverdueGoals.clicked.connect(self.loadOverdueGoals)
        self.push_CompleteGoals.clicked.connect(self.loadCompletedGoals)
        self.push_AllGoals.clicked.connect(self.loadAllGoals)
        self.push_sort_category.clicked.connect(self.loadCategorySort)
        self.push_sort_priority.clicked.connect(self.loadPrioritySort)
        self.push_add_goal.clicked.connect(self.loadAddGoal)
        self.push_complete.clicked.connect(self.loadCompleteGoal)
        self.push_edit_view.clicked.connect(self.loadEditViewGoal)
        self.push_delete_goal.clicked.connect(self.loadDeleteGoal)
        self.push_view_analysis.clicked.connect(self.loadViewAnalysis)

    @pyqtSlot()
    def loadCurrentGoals(self):
        '''
        @param:

        @return:

        @purpose:
        '''
        self.label_Goals.setText("Current Goals") #set label
        self.state = State.CURRENT #set state

        #pulls current goal list from model

        #cycle through list, to string every goal and place into listview

        #cycle through list, get name and goalid of every goal and place into combobox

    @pyqtSlot()
    def loadOverdueGoals(self):
        '''
        @param:

        @return:

        @purpose:
        '''
        self.label_Goals.setText("Overdue Goals") #set label
        self.state = State.OVERDUE #set state

        #pulls overdue goal list from model

        #cycle through list, to string every goal and place into listview

        #cycle through list, get name and goalid of every goal and place into combobox

    @pyqtSlot()
    def loadCompletedGoals(self):
        '''
        @param:

        @return:

        @purpose:
        '''
        self.label_Goals.setText("Completed Goals") #set label
        self.state = State.COMPLETED #set state

        #pulls completed goal list from model

        #cycle through list, to string every goal and place into listview

        #cycle through list, get name and goalid of every goal and place into combobox

    @pyqtSlot()
    def loadAllGoals(self):
        '''
        @param:

        @return:

        @purpose:
        '''
        self.label_Goals.setText("All Goals") #set label
        self.state = State.ALL #set state

        #pulls all goal list from model

        #cycle through list, to string every goal and place into listview

        #cycle through list, get name and goalid of every goal and place into combobox

    @pyqtSlot()
    def loadCategorySort(self):
        '''
        @param:

        @return:

        @purpose:
        '''
        #runs category sort on model

        goalList = []
        if self.state == State.CURRENT:
        	#pulls current goal list from model
        	pass
        elif self.state == State.OVERDUE:
        	#pulls overdue goal list from model
        	pass
        elif self.state == State.COMPLETED:
        	#pulls completed goal list from model
        	pass
        elif self.state == State.ALL:
        	#pulls all goal list from model
        	pass
        else:
        	print("Error")

        #cycle through list, to string every goal and place into listview

        #cycle through list, get name and goalid of every goal and place into combobox

    @pyqtSlot()
    def loadPrioritySort(self):
        '''
        @param:

        @return:

        @purpose:
        '''
        #runs category sort on model

        goalList = []
        if self.state == State.CURRENT:
        	#pulls current goal list from model
        	pass
        elif self.state == State.OVERDUE:
        	#pulls overdue goal list from model
        	pass
        elif self.state == State.COMPLETED:
        	#pulls completed goal list from model
        	pass
        elif self.state == State.ALL:
        	#pulls all goal list from model
        	pass
        else:
        	print("Error")

        #cycle through list, to string every goal and place into listview

        #cycle through list, get name and goalid of every goal and place into combobox

    @pyqtSlot()
    def loadAddGoal(self):
        '''
        @param:

        @return:

        @purpose:
        '''
        #create default state of goal

        #put default state of goal in model

        #open add AddEditViewGoal window

        #if accept, add updated state of goal to model
        #if reject, discard state of goal
        
        goalList = []
        if self.state == State.CURRENT:
        	#pulls current goal list from model
        	pass
        elif self.state == State.OVERDUE:
        	#pulls overdue goal list from model
        	pass
        elif self.state == State.COMPLETED:
        	#pulls completed goal list from model
        	pass
        elif self.state == State.ALL:
        	#pulls all goal list from model
        	pass
        else:
        	print("Error")

        #cycle through list, to string every goal and place into listview

        #cycle through list, get name and goalid of every goal and place into combobox

    @pyqtSlot()
    def loadCompleteGoal(self):
        '''
        @param:

        @return:

        @purpose:
        '''
        #get goalid from combobox

        #complete goal (model operation)
        pass

    @pyqtSlot()
    def loadEditViewGoal(self):
        '''
        @param:

        @return:

        @purpose:
        '''
        #get goalid from combobox

        #get goal from model using goalid

        #create state of goal from goal

        #put state of goal in model

        #open add AddEditViewGoal window

        #if accept, add updated state of goal to model
        #if reject, discard state of goal
        
        goalList = []
        if self.state == State.CURRENT:
        	#pulls current goal list from model
        	pass
        elif self.state == State.OVERDUE:
        	#pulls overdue goal list from model
        	pass
        elif self.state == State.COMPLETED:
        	#pulls completed goal list from model
        	pass
        elif self.state == State.ALL:
        	#pulls all goal list from model
        	pass
        else:
        	print("Error")

        #cycle through list, to string every goal and place into listview

        #cycle through list, get name and goalid of every goal and place into combobox

    @pyqtSlot()
    def loadDeleteGoal(self):
        '''
        @param:

        @return:

        @purpose:
        '''
        #get goalid from combobox

        #delete goal (model operation)
        pass

    @pyqtSlot()
    def loadViewAnalysis(self):
        '''
        @param:

        @return:

        @purpose:
        '''
        pass
    
def main():
    '''
        @param:

        @return:

        @purpose:
        '''
    filemanager = FileManager() #create FileManager object
    model = filemanager.load("potato.gtd") #load File and store
    app = QApplication(sys.argv) # Initialize PyQT application
    window = MainWindow(model) # Create a window of the main display of the Goal Tracker
    window.show() # Show the window
    sys.exit(app.exec_()) # Exit the program

if __name__ == '__main__':
    main()
