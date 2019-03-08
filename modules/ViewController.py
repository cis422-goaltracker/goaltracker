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

# Global variable for storing UI files
UI_PATHS = {"MainWindow": "../UI/MainWindow.ui", "AddEditViewGoal": "../UI/AddEditViewGoal.ui", "AddEditViewSubgoal": "../UI/AddEditViewSubgoal.ui", "Analysis": "../UI/Analysis.ui", "UncompletedAnalysis": "../UI/UncompletedAnalysis.ui"}

# Different statuses of goals
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
        @param: None

        @return: None

        @purpose: Update main window to display current goals. Update title to "Current Goals",
                  set the state of the main window to CURRENT, and refresh the list of goals.
        '''
        self.label_listTitle.setText("Current Goals") #set label
        self.state = State.CURRENT #set state
        self.refreshListView()

    @pyqtSlot()
    def loadOverdueGoals(self):
        '''
        @param: None

        @return: None

        @purpose: Update main window to display overdue goals. Update title to "Overdue Goals",
                  set the state of the main window to OVERDUE, and refresh the list of goals.
        '''
        self.label_listTitle.setText("Overdue Goals") #set label
        self.state = State.OVERDUE #set state
        self.refreshListView()

    @pyqtSlot()
    def loadCompletedGoals(self):
        '''
        @param: None

        @return: None

        @purpose: Update main window to display completed goals. Update title to "Completed Goals",
                  set the state of the main window to COMPLETED, and refresh the list of goals.
        '''
        self.label_listTitle.setText("Completed Goals") #set label
        self.state = State.COMPLETED #set state
        self.refreshListView()

    @pyqtSlot()
    def loadAllGoals(self):
        '''
        @param: None

        @return: None

        @purpose: Update main window to display all goals. Update title to "All Goals", set the
                  state of the main window to ALL, and refresh the list of goals.
        '''
        self.label_listTitle.setText("All Goals") #set label
        self.state = State.ALL #set state
        self.refreshListView()

    @pyqtSlot()
    def loadCategorySort(self):
        '''
        @param: None

        @return: None

        @purpose: Sort the goals according to their category. Sort the goals by their category and
                  refresh the page.
        '''
        self.model.categorySort() #runs category sort on model
        self.refreshListView()

    @pyqtSlot()
    def loadPrioritySort(self):
        '''
        @param: None

        @return: None

        @purpose: Sort the goals according to their priority. Sort the goals by their priority and
                  refresh the page.
        '''
        self.model.prioritySort()#runs priority sort on model
        self.refreshListView()

    @pyqtSlot()
    def loadAddGoal(self):
        '''
        @param: None

        @return: None

        @purpose: Open the Add Goal Window and add the user's goal to the model. If the user cancels
                  out of the window, then delete the goal from the model.
        '''
        window = AddEditViewGoal(self.model) #open add AddEditViewGoal window, pass it model
        if window.exec():
            self.refreshListView()
        else:
            self.model.deleteGoal(self.model.getCurrGID())

    @pyqtSlot()
    def loadCompleteGoal(self):
        '''
        @param: None

        @return: None

        @purpose: Update the status of the goal to complete. Update the status of the goal in the
                  model to complete and refresh the list of goals.
        '''
        if self.goalIsSelected():
            goalid = self.selectedListItemId
            self.model.completeGoal(goalid)
            self.refreshListView()

    @pyqtSlot()
    def loadEditViewGoal(self):
        '''
        @param: None

        @return: None

        @purpose: Open the Edit/View Goal Window and update the user's changes to the goal. Get the
                  selected goal's information and update the window to display this information, and
                  refresh the list of goals.
        '''
        if self.goalIsSelected():
            goalid = self.selectedListItemId
            window = AddEditViewGoal(self.model, goalid) #open AddEditViewGoal window, passes it model and goalid
            if window.exec():
                self.refreshListView()

    @pyqtSlot()
    def loadDeleteGoal(self):
        '''
        @param: None

        @return: None

        @purpose: Delete the goal. Get the selected goal's information, delete the goal from the
                  model, and refresh the list of goals.
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
        @param: None

        @return: None

        @purpose: Open the View Analysis Window. Get the selected goal's information and display the
                  analysis according to whether it's complete or not, and refresh the list of goals.
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
        @param: None

        @return: 

        @purpose: 
        '''
        return self.selectedListItemId != None

    def setChosenItem(self):
        '''
        @param: None

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
        @param: (list) - A list of goals

        @return: None

        @purpose: Add a list of goals to the main window. Create a new list item for
                  each goal, set the text and data of the item, and display this new
                  item in the list.
        '''
        self.listWidget.clear()
        for goal in _goalList:
            item = QListWidgetItem()
            item.setText(goal.toString())
            item.setData(Qt.UserRole, goal.getId())
            self.listWidget.addItem(item)

    def getGoalStateList(self):
        '''
        @param: None

        @return: (list) - A list of goals with a specific status

        @purpose: Get a list of goals that have a specific status. Check the status
                  of goals that should be displayed and return a list of goals with
                  that status.
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
        @param: None

        @return: None

        @purpose: Updates the goals that are displayed in the list of goals. Get the
                  goals according to their status and display them as a list.
        '''
        goalList = self.getGoalStateList()
        self.addToListView(goalList)

    
def main():
    '''
        @param: None

        @return: None

        @purpose: Launches the program. Sets up the File Manager to save information about
                  the user's goal information, creates a Model with the goal information,
                  executes the program, and then quits.
        '''
    filemanager = FileManager("potato.gtd") #create FileManager object
    model = filemanager.load() #load File and store
    app = QApplication(sys.argv) # Initialize PyQT application
    window = MainWindow(model) # Create a window of the main display of the Goal Tracker
    window.show() # Show the window
    app.exec_()
    filemanager.save(model)
    sys.exit() # Exit the program

if __name__ == '__main__':
    main()
