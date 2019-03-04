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
UI_PATHS = {"MainWindow": "../UI/MainWindow.ui", "AddEditViewGoal": "../UI/AddEditViewGoal.ui", "AddEditViewSubGoal": "../UI/AddEditViewSubGoal.py"}

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

        # Update the window's title
        self.setWindowTitle('Goal Tracker');

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

        self.addToListView(goalList)
        self.addToComboBox(goalList)

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

        self.addToListView(goalList)
        self.addToComboBox(goalList)

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

        self.addToListView(goalList)
        self.addToComboBox(goalList)

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

        self.addToListView(goalList)
        self.addToComboBox(goalList)

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

        self.addToListView(goalList)
        self.addToComboBox(goalList)

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

        self.addToListView(goalList)
        self.addToComboBox(goalList)


    @pyqtSlot()
    def loadAddGoal(self):
        '''
        @param:

        @return:

        @purpose:
        '''
        #create default state of goal

        #open add AddEditViewGoal window, pass it model and state
	        # addDialog = EditGoalWindow(self.model)
	        # if addDialog.exec():
	        #     return(True)
	        # return False
        
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

        self.addToListView(goalList)
        self.addToComboBox(goalList)

    @pyqtSlot()
    def loadCompleteGoal(self):
        '''
        @param:

        @return:

        @purpose:
        '''
        goalid = self.getGIDFromComboBox() #get goalid from combobox

        #complete goal (model operation)

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

        self.addToListView(goalList)
        self.addToComboBox(goalList)

    @pyqtSlot()
    def loadEditViewGoal(self):
        '''
        @param:

        @return:

        @purpose:
        '''
        goalid = self.getGIDFromComboBox() #get goalid from combobox

        #get goal from model using goalid

        #create state of goal from goal

        #open AddEditViewGoal window, passes it model and state
        
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

        self.addToListView(goalList)
        self.addToComboBox(goalList)

    @pyqtSlot()
    def loadDeleteGoal(self):
        '''
        @param:

        @return:

        @purpose:
        '''
        goalid = self.getGIDFromComboBox() #get goalid from combobox

        #delete goal (model operation)

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

        self.addToListView(goalList)
        self.addToComboBox(goalList)

    @pyqtSlot()
    def loadViewAnalysis(self):
        '''
        @param:

        @return:

        @purpose:
        '''
        pass

    def addToListView(self, _goalList):
    	#cycle through list, to string every goal and place into listview
    	pass

    def addToComboBox(self, _goalList):
    	#cycle through list, get name and goalid of every goal and place into combobox
    	pass

    def getGIDFromComboBox(self):
    	#return the GID currently in combobox
    	pass

#@KELLIE HAWKS, EditGoalWindow is in "Dialogs.py" its called "AddEditViewGoal"
# class EditGoalWindow(QDialog):
#     def __init__(self, model):

#         super(EditGoalWindow, self).__init__()
#         # Load the Edit Goal Window UI
#         loadUi(UI_PATHS["AddEditViewGoal"], self)

#         self.push_save.clicked.connect(self.save_goal)
        
#         self.setWindowTitle('Add/Edit Goal') # Update the window's title
#         #self.endDate.setDate(datetime.today()) # Set the QDateEdit widget to display a predetermined date (today's date)
#         self.radio_priority_low.setChecked(True) # Set the RadioButton widget to be checked according to a predetermined priority (low)

#         self.model = model
#     @pyqtSlot()
#     def save_goal(self):

#         goalName = self.lineEdit_goal_name.text()
#         endDate = self.dateTimeEdit_due_date.date()
#         category = self.lineEdit_category.text()
#         priority = self.buttonGroup.checkedButton().text()
#         memo = self.textEdit.toPlainText()

#         self.model.addGoal({"name": goalName, "category": category, "priority": priority, "memo": memo}, [])
        
#         mylist = self.model.getGoalList()
#         for goal in mylist:
#             print(goal.getName(), goal.getCategory(), goal.getPriority(), goal.getMemo())

#         self.accept()
#         return 
    
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
