"""
    Names: Holly Hardin (HH)
    CIS 422
    GoalTracker
        Reference [0]: https://stackoverflow.com/questions/21213853/pyside-how-to-delete-widgets-from-gridlayout

"""
#System Imports
import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from datetime import datetime
from enum import Enum

#Module Imports
from Goal import Goal, SubGoal
from Model import Model
from FileManager import FileManager
from AnalysisGenerator import AnalysisGenerator

#UI Imports
from Dialogs import AddEditViewGoal, AddEditViewSubGoal, UncompletedAnalysis, Analysis

# Global variable for storing UI files (HH)
UI_PATHS = {"MainWindow": "../UI/MainWindow.ui", "AddEditViewGoal": "../UI/AddEditViewGoal.ui", "AddEditViewSubgoal": "../UI/AddEditViewSubgoal.ui", "Analysis": "../UI/Analysis.ui", "UncompletedAnalysis": "../UI/UncompletedAnalysis.ui"}

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
        self.selectedListItemId = None
        
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
        self.listWidget.itemSelectionChanged.connect(self.setChosenItem)

        # Update the window's title
        self.setWindowTitle('Goal Tracker')

        #instantiates window with current goals
        self.loadCurrentGoals()

    '''********************PYQTSLOT OPERATIONS********************'''
    @pyqtSlot()
    def loadCurrentGoals(self):
        '''
        @param:

        @return:

        @purpose:
        '''
        self.label_listTitle.setText("Current Goals") #set label
        self.state = State.CURRENT #set state
        self.refreshListView()

    @pyqtSlot()
    def loadOverdueGoals(self):
        '''
        @param:

        @return:

        @purpose:
        '''
        self.label_listTitle.setText("Overdue Goals") #set label
        self.state = State.OVERDUE #set state
        self.refreshListView()

    @pyqtSlot()
    def loadCompletedGoals(self):
        '''
        @param:

        @return:

        @purpose:
        '''
        self.label_listTitle.setText("Completed Goals") #set label
        self.state = State.COMPLETED #set state
        self.refreshListView()

    @pyqtSlot()
    def loadAllGoals(self):
        '''
        @param:

        @return:

        @purpose:
        '''
        self.label_listTitle.setText("All Goals") #set label
        self.state = State.ALL #set state
        self.refreshListView()

    @pyqtSlot()
    def loadCategorySort(self):
        '''
        @param:

        @return:

        @purpose:
        '''
        self.model.categorySort() #runs category sort on model
        self.refreshListView()

    @pyqtSlot()
    def loadPrioritySort(self):
        '''
        @param:

        @return:

        @purpose:
        '''
        self.model.prioritySort()#runs priority sort on model
        self.refreshListView()

    @pyqtSlot()
    def loadAddGoal(self):
        '''
        @param:

        @return:

        @purpose:
        '''
        window = AddEditViewGoal(self.model) #open add AddEditViewGoal window, pass it model
        if window.exec():
            self.refreshListView()
        else:
            self.model.deleteGoal(self.model.getCurrGID())

    @pyqtSlot()
    def loadCompleteGoal(self):
        '''
        @param:

        @return:

        @purpose:
        '''
        if self.goalIsSelected():
            goalid = self.selectedListItemId
            self.model.completeGoal(goalid)
            self.refreshListView()

    @pyqtSlot()
    def loadEditViewGoal(self):
        '''
        @param:

        @return:

        @purpose:
        '''
        if self.goalIsSelected():
            goalid = self.selectedListItemId
            window = AddEditViewGoal(self.model, goalid) #open AddEditViewGoal window, passes it model and goalid
            if window.exec():
                self.refreshListView()

    @pyqtSlot()
    def loadDeleteGoal(self):
        '''
        @param:

        @return:

        @purpose:
        '''
        if self.goalIsSelected():
            goalid = self.selectedListItemId
            if self.model.isEffortTracking(goalid):
                self.model.stopEffortTracker(goalid)
            self.model.deleteGoal(goalid)
            self.refreshListView()

    @pyqtSlot()
    def loadViewAnalysis(self): #FUNCTION NEEDS TO BE BUILT
        '''
        @param:

        @return:

        @purpose:
        '''
        if self.goalIsSelected():
            goalid = self.selectedListItemId
            if self.model.getGoal(goalid).isComplete() == True:
                window = Analysis(self.model, goalid) #open AddEditViewGoal window, passes it model and goalid
            else:
                window = UncompletedAnalysis(self.model)
            if window.exec():
                self.refreshListView()

    '''********************CLASS METHODS********************'''
    def goalIsSelected(self):
        '''
        @param:

        @return:

        @purpose:
        '''
        return self.selectedListItemId != None

    def setChosenItem(self):
        '''
        @param:

        @return:

        @purpose:
        '''
        selectedlist = [item.data(Qt.UserRole) for item in self.listWidget.selectedItems()]
        if not selectedlist:
            self.selectedListItemId = None
        else:
            self.selectedListItemId = selectedlist[0]

    def addToListView(self, _goalList):
        '''
        @param:

        @return:

        @purpose:
        '''
        self.listWidget.clear()
        for goal in _goalList:
            item = QListWidgetItem()
            item.setText(goal.toString())
            item.setData(Qt.UserRole, goal.getId())
            self.listWidget.addItem(item)

    def getGoalStateList(self):
        '''
        @param:

        @return:

        @purpose:
        '''
        if self.state == State.CURRENT:
            return self.model.getCurrentGoalList() #pulls current goal list from model
        elif self.state == State.OVERDUE:
            return self.model.getOverDueGoalList() #pulls overdue goal list from model
        elif self.state == State.COMPLETED:
            return self.model.getCompletedGoalList() #pulls completed goal list from model
        elif self.state == State.ALL:
            return self.model.getGoalList() #pulls all goal list from model
        else:
            return ["ERROR", "ERROR", "ERROR"]

    def refreshListView(self):
        '''
        @param:

        @return:

        @purpose:
        '''
        goalList = self.getGoalStateList()
        self.addToListView(goalList)

    
def main():
    '''
        @param:

        @return:

        @purpose:
        '''
    filemanager = FileManager("potato.gtd") #create FileManager object
    model = filemanager.load() #load File and store
    app = QApplication(sys.argv) # Initialize PyQT application
    window = MainWindow(model) # Create a window of the main display of the Goal Tracker
    window.show() # Show the window
    sys.exit(app.exec_()) # Exit the program

if __name__ == '__main__':
    main()
