"""
    Authors: Noah Palmer, Holly Hardin, Jiazhen Cao, Kellie Hawks, Isaac Lance, Weigang An
    Date: 03/09/2019
    CIS 422
    GoalTracker
    Reference [0]: https://stackoverflow.com/questions/41772092/how-can-i-get-all-selected-items-for-a-qlistwidget-when-the-user-interacts-with

"""
#System Imports
import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from datetime import datetime, timedelta
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
    CURRENT = 1 # Constant for when Main Window is displaying Current goals
    OVERDUE = 2 # Constant for when Main Window is displaying Overdue goals
    COMPLETED = 3 # Constant for when Main Window is displaying Completed goals
    ALL = 4 # Constant for when Main Window is displaying All goals

class MainWindow(QMainWindow):
    def __init__(self, _model):
        '''
        @param: _model (Model)

        @return: None

        @purpose: Initialize the main window.
        '''
        super(MainWindow, self).__init__() #Initializes parent constructor
        loadUi(UI_PATHS["MainWindow"], self) # Load the Main Window UI

        #Class Variables
        self.model = _model # Initialize model class
        self.state = State.CURRENT # Initialize the status of goals to display Current goals
        self.selectedListItemId = None # Initialize the selected goal to None
        
        #Signals
        self.push_CurrentGoals.clicked.connect(self.loadCurrentGoals) # Connect Current Goals button with loadCurrentGoals method
        self.push_OverdueGoals.clicked.connect(self.loadOverdueGoals) # Connect Overdue Goals button with loadOverdueGoals method
        self.push_CompleteGoals.clicked.connect(self.loadCompletedGoals) # Connect Complete GOals button with loadCompletedGoals method
        self.push_AllGoals.clicked.connect(self.loadAllGoals) # Connect All Goals button with loadAllGoals method
        self.push_sort_category.clicked.connect(self.loadCategorySort) # Connect Category button with loadCategorySort method
        self.push_sort_priority.clicked.connect(self.loadPrioritySort) # Connect Priority button with loadPrioritySort method
        self.push_add_goal.clicked.connect(self.loadAddGoal) # Connect Add Goal button with loadAddGoal method
        self.push_complete.clicked.connect(self.loadCompleteGoal) # Connect Complete button with loadComplete method
        self.push_edit_view.clicked.connect(self.loadEditViewGoal) # Connect Edit/View button with loadEditView method
        self.push_delete_goal.clicked.connect(self.loadDeleteGoal) # Connect Delete button with loadDeleteGoal method
        self.push_view_analysis.clicked.connect(self.loadViewAnalysis) # Connect View Analysis button with loadViewAnalysis method
        self.listWidget.itemSelectionChanged.connect(self.setChosenItem) # Connect clicking a goal from the list with setChosenItem method

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
        self.label_listTitle.setText("Current Goals") # Set label
        self.state = State.CURRENT # Set state
        self.refreshListView() # Refreshes list of goals

    @pyqtSlot()
    def loadOverdueGoals(self):
        '''
        @param: None

        @return: None

        @purpose: Update main window to display overdue goals. Update title to "Overdue Goals",
                  set the state of the main window to OVERDUE, and refresh the list of goals.
        '''
        self.label_listTitle.setText("Overdue Goals") # Set label
        self.state = State.OVERDUE # Set state
        self.refreshListView() # Refreshes list of goals

    @pyqtSlot()
    def loadCompletedGoals(self):
        '''
        @param: None

        @return: None

        @purpose: Update main window to display completed goals. Update title to "Completed Goals",
                  set the state of the main window to COMPLETED, and refresh the list of goals.
        '''
        self.label_listTitle.setText("Completed Goals") # Set label
        self.state = State.COMPLETED # Set state
        self.refreshListView() # Refreshes list of goals

    @pyqtSlot()
    def loadAllGoals(self):
        '''
        @param: None

        @return: None

        @purpose: Update main window to display all goals. Update title to "All Goals", set the
                  state of the main window to ALL, and refresh the list of goals.
        '''
        self.label_listTitle.setText("All Goals") # Set label
        self.state = State.ALL # Set state
        self.refreshListView() # Refreshes list of goals

    @pyqtSlot()
    def loadCategorySort(self):
        '''
        @param: None

        @return: None

        @purpose: Sort the goals according to their category. Sort the goals by their category and
                  refresh the page.
        '''
        self.model.categorySort() # Runs category sort on model
        self.refreshListView() # Refreshes list of goals

    @pyqtSlot()
    def loadPrioritySort(self):
        '''
        @param: None

        @return: None

        @purpose: Sort the goals according to their priority. Sort the goals by their priority and
                  refresh the page.
        '''
        self.model.prioritySort() # Runs priority sort on model
        self.refreshListView() # Refreshes list of goals

    @pyqtSlot()
    def loadAddGoal(self):
        '''
        @param: None

        @return: None

        @purpose: Open the Add Goal Window and add the user's goal to the model. If the user cancels
                  out of the window, then delete the goal from the model.
        '''
        window = AddEditViewGoal(self.model) # Opens AddEditViewGoal window, pass it model
        if window.exec(): # If successfully exits
            self.refreshListView() # Refresh list of goals
        else: # Otherwise...
            self.model.deleteGoal(self.model.getCurrGID()) # Delete the goal from the goal list

    @pyqtSlot()
    def loadCompleteGoal(self):
        '''
        @param: None

        @return: None

        @purpose: Update the status of the goal to complete. Update the status of the goal in the
                  model to complete and refresh the list of goals.
        '''
        if self.goalIsSelected(): # If a goal is selected
            goalid = self.selectedListItemId # Get the selected goal's ID
            if self.model.isEffortTracking(goalid): # If the model is keeping track of an effort's goal
                self.model.stopEffortTracker(goalid) # Stop the effort timer
            self.model.completeGoal(goalid) # Update the goal's status to Completed
            self.refreshListView() # Refresh the list of goals displayed

    @pyqtSlot()
    def loadEditViewGoal(self):
        '''
        @param: None

        @return: None

        @purpose: Open the Edit/View Goal Window and update the user's changes to the goal. Get the
                  selected goal's information and update the window to display this information, and
                  refresh the list of goals.
        '''
        if self.goalIsSelected(): # If a goal is selected
            goalid = self.selectedListItemId # Get the selected goal's ID
            window = AddEditViewGoal(self.model, goalid) # Open AddEditViewGoal window
            if window.exec(): # If successfully exits
                self.refreshListView() # Refresh the list of goals displayed

    @pyqtSlot()
    def loadDeleteGoal(self):
        '''
        @param: None

        @return: None

        @purpose: Delete the goal. Get the selected goal's information, delete the goal from the
                  model, and refresh the list of goals.
        '''
        if self.goalIsSelected(): # If a goal is selected
            goalid = self.selectedListItemId # Get the selected goal's ID
            if self.model.isEffortTracking(goalid): # If the model is keeping track of an effort's goal
                self.model.stopEffortTracker(goalid) # Stop the effort timer
            self.model.deleteGoal(goalid) # Delete the goal from the list
            self.refreshListView() # Refresh the list of goals displayed

    @pyqtSlot()
    def loadViewAnalysis(self): #FUNCTION NEEDS TO BE BUILT
        '''
        @param: None

        @return: None

        @purpose: Open the View Analysis Window. Get the selected goal's information and display the
                  analysis according to whether it's complete or not, and refresh the list of goals.
        '''
        if self.goalIsSelected(): # If a goal is selected
            goalid = self.selectedListItemId # Get the selected goal's ID
            if self.model.getGoal(goalid).isComplete() == True: # If the selected goal is completed
                window = Analysis(self.model, goalid) # Open Analysis window
            else: # Otherwise...
                window = UncompletedAnalysis(self.model, goalid) # Open UncompletedAnalysis window
            if window.exec(): # If sucessfully exits
                self.refreshListView() # Refresh the list of goals displayed

    def setChosenItem(self):
        '''
        @param: None

        @return: None

        @purpose: When a selection is made, it determines if it was selected on or off.
        If selected off, then sets list id to null, otherwise the corresponding goal id.
        '''
        selectedlist = [item.data(Qt.UserRole) for item in self.listWidget.selectedItems()] # Get the list of selected goals
        if not selectedlist: # If there isn't a list of selected goals
            self.selectedListItemId = None # Set the selected item ID to None
        else: # Otherwise... 
            self.selectedListItemId = selectedlist[0] # Set it to the first item in the selected goals

    '''********************CLASS METHODS********************'''
    def goalIsSelected(self):
        '''
        @param: None

        @return: (boolean)

        @purpose: returns if item is selected by checking if the selected list item id is null
        '''
        return self.selectedListItemId != None # Return the selected goal

    def addToListView(self, _goalList):
        '''
        @param: _goalList (List)

        @return: None

        @purpose: Add a list of goals to the main window. Create a new list item for
                  each goal, set the text and data of the item, and display this new
                  item in the list.
        '''
        self.listWidget.clear() # Clear the goals that are listed
        for goal in _goalList: # For every goal in the goal list
            item = QListWidgetItem() # Create an item for the list
            item.setText(goal.toString()) # Set the text of the item to the name of the goal
            item.setData(Qt.UserRole, goal.getId()) # Set the data of the item to the data of the goal
            self.listWidget.addItem(item) # Add the item to the list

    def getGoalStateList(self):
        '''
        @param: None

        @return: (List)

        @purpose: Get a list of goals that have a specific status. Check the status
                  of goals that should be displayed and return a list of goals with
                  that status.
        '''
        if self.state == State.CURRENT: # If the status of the goals to display is current
            return self.model.getCurrentGoalList() # Get the current goal list from model
        elif self.state == State.OVERDUE: # If the status of the goals to display is overdue
            return self.model.getOverDueGoalList() # Get the overdue goal list from model
        elif self.state == State.COMPLETED: # If the status of the goals to display is completed
            return self.model.getCompletedGoalList() # Get the completed goal list from model
        elif self.state == State.ALL: # If the status of the goals to display is all
            return self.model.getGoalList() # Get the goal list from model
        else: # Otherwise...
            return ["ERROR", "ERROR", "ERROR"] # Report an error

    def refreshListView(self):
        '''
        @param: None

        @return: None

        @purpose: Updates the goals that are displayed in the list of goals. Get the
                  goals according to their status and display them as a list.
        '''
        goalList = self.getGoalStateList() # Get the list of goals to display
        self.addToListView(goalList) # Add the goals to the list

    
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
    app.exec() # Execute the program
    filemanager.save(model) # Save the model
    sys.exit() # Exit the program

if __name__ == '__main__':
    main()
