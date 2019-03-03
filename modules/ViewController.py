"""
	Names: Holly Hardin (HH)
	CIS 422
	GoalTracker
        Reference [0]: https://stackoverflow.com/questions/21213853/pyside-how-to-delete-widgets-from-gridlayout

"""

from Goal import Goal as Goal
from Model import Model as Model
# from SubGoal import SubGoal as SubGoal
# from Status import Status as Status

# from GoalManager import GoalManager as GoalManager
# from SubGoalManager import SubGoalManager as SubGoalManager
from FileManager import FileManager as FileManager
# from EffortTracker import EffortTracker as EffortTracker
# from ActiveTimer import ActiveTimer as ActiveTimer
# from SortManager import SortManager as SortManager
# from ProgressTracker import ProgressTracker as ProgressTracker
# from AnalysisViewer import AnalysisViewer as AnalysisViewer
# from AnalysisGenerator import AnalysisGenerator as AnalysisGenerator

#Commented the line below out because it caused an error
#from ModelView import ModelView as ModelView

import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from datetime import date

# Global variable for storing UI files (HH)
ui = ['../UI/GoalTracker.ui', '../UI/AddGoal.ui', '../UI/EditGoal.ui', '../UI/ViewGoal.ui']

# The view of adding a goal
class AddGoalWindow(QDialog):
    def __init__(self):
        # ?
        super(AddGoalWindow, self).__init__()
        # Load the Add Goal Window UI
        loadUi(ui[1], self)

        # Update the window's title
        self.setWindowTitle('Add Goal');

        # Set the QDateEdit widget to display a predetermined date (today's date)
        self.endDate.setDate(date.today())

        # ?
        super(AddGoalWindow, self).__init__()
        # Load the Add Goal Window UI
        loadUi(ui[1], self)

        # Update the window's title
        self.setWindowTitle('Add Goal');

        # Set the QDateEdit widget to display a predetermined date (today's date)
        self.endDate.setDate(date.today())

        # Hide all of the subgoals
        self.subgoal1.hide()
        self.subgoal2.hide()
        self.subgoal3.hide()
        self.subgoal4.hide()
        self.subgoal5.hide()

        # Hide all of the delete buttons
        self.deleteButton1.hide()
        self.deleteButton2.hide()
        self.deleteButton3.hide()
        self.deleteButton4.hide()
        self.deleteButton5.hide()
        # Set up the methods for when a button is clicked
        self.deleteButton1.clicked.connect(self.deleteSubgoal1)
        self.deleteButton2.clicked.connect(self.deleteSubgoal2)
        self.deleteButton3.clicked.connect(self.deleteSubgoal3)
        self.deleteButton4.clicked.connect(self.deleteSubgoal4)
        self.deleteButton5.clicked.connect(self.deleteSubgoal5)

        # Create buttons for adding subgoals
        self.addButton1 = QPushButton()
        self.addButton2 = QPushButton()
        self.addButton3 = QPushButton()
        self.addButton4 = QPushButton()
        self.addButton5 = QPushButton()
        # Set the text of the buttons
        self.addButton1.setText("+")
        self.addButton2.setText("+")
        self.addButton3.setText("+")
        self.addButton4.setText("+")
        self.addButton5.setText("+")
        # Set up methods for when a button is clicked
        self.addButton1.clicked.connect(self.addSubgoal1)
        self.addButton2.clicked.connect(self.addSubgoal2)
        self.addButton3.clicked.connect(self.addSubgoal3)
        self.addButton4.clicked.connect(self.addSubgoal4)
        self.addButton5.clicked.connect(self.addSubgoal5)
        # Add button to the grid layout
        self.gridLayout.addWidget(self.addButton1, 0, 2, Qt.AlignLeft)
        self.gridLayout.addWidget(self.addButton2, 1, 2, Qt.AlignLeft)
        self.gridLayout.addWidget(self.addButton3, 2, 2, Qt.AlignLeft)
        self.gridLayout.addWidget(self.addButton4, 3, 2, Qt.AlignLeft)
        self.gridLayout.addWidget(self.addButton5, 4, 2, Qt.AlignLeft)

    def addSubgoal1(self):
        self.subgoal1.show()
        self.addButton1.hide()
        self.deleteButton1.show()

    def addSubgoal2(self):
        self.subgoal2.show()
        self.addButton2.hide()
        self.deleteButton2.show()

    def addSubgoal3(self):
        self.subgoal3.show()
        self.addButton3.hide()
        self.deleteButton3.show()

    def addSubgoal4(self):
        self.subgoal4.show()
        self.addButton4.hide()
        self.deleteButton4.show()

    def addSubgoal5(self):
        self.subgoal5.show()
        self.addButton5.hide()
        self.deleteButton5.show()

    def deleteSubgoal1(self):
        self.subgoal1.hide()
        self.deleteButton1.hide()
        self.addButton1.show()

    def deleteSubgoal2(self):
        self.subgoal2.hide()
        self.deleteButton2.hide()
        self.addButton2.show()

    def deleteSubgoal3(self):
        self.subgoal3.hide()
        self.deleteButton3.hide()
        self.addButton3.show()

    def deleteSubgoal4(self):
        self.subgoal4.hide()
        self.deleteButton4.hide()
        self.addButton4.show()

    def deleteSubgoal5(self):
        self.subgoal5.hide()
        self.deleteButton5.hide()
        self.addButton5.show()

# The view of editing a goal
class EditGoalWindow(QDialog):
    def __init__(self):
        # ?
        super(EditGoalWindow, self).__init__()
        # Load the Edit Goal Window UI
        loadUi(ui[2], self)
        # Update the window's title
        self.setWindowTitle('Edit Goal');
        # Set the text of the LineEdit box to display a predetermined text
        self.goalName.setText("Exercise")
        # Set the QDateEdit widget to display a predetermined date (today's date)
        self.endDate.setDate(date.today())
        # Set the RadioButton widget to be checked according to a predetermined category (personal)
        self.personalRadioButton.setChecked(True)
        # Set the RadioButton widget to be checked according to a predetermined priority (low)
        self.lowRadioButton.setChecked(True)

        # Hide all of the subgoals
        self.subgoal1.hide()
        self.subgoal2.hide()
        self.subgoal3.hide()
        self.subgoal4.hide()
        self.subgoal5.hide()

        # Hide all of the delete buttons
        self.deleteButton1.hide()
        self.deleteButton2.hide()
        self.deleteButton3.hide()
        self.deleteButton4.hide()
        self.deleteButton5.hide()
        # Set up the methods for when a button is clicked
        self.deleteButton1.clicked.connect(self.deleteSubgoal1)
        self.deleteButton2.clicked.connect(self.deleteSubgoal2)
        self.deleteButton3.clicked.connect(self.deleteSubgoal3)
        self.deleteButton4.clicked.connect(self.deleteSubgoal4)
        self.deleteButton5.clicked.connect(self.deleteSubgoal5)

        # Create buttons for adding subgoals
        self.addButton1 = QPushButton()
        self.addButton2 = QPushButton()
        self.addButton3 = QPushButton()
        self.addButton4 = QPushButton()
        self.addButton5 = QPushButton()
        # Set the text of the buttons
        self.addButton1.setText("+")
        self.addButton2.setText("+")
        self.addButton3.setText("+")
        self.addButton4.setText("+")
        self.addButton5.setText("+")
        # Set up methods for when a button is clicked
        self.addButton1.clicked.connect(self.addSubgoal1)
        self.addButton2.clicked.connect(self.addSubgoal2)
        self.addButton3.clicked.connect(self.addSubgoal3)
        self.addButton4.clicked.connect(self.addSubgoal4)
        self.addButton5.clicked.connect(self.addSubgoal5)
        # Add button to the grid layout
        self.gridLayout.addWidget(self.addButton1, 0, 2, Qt.AlignLeft)
        self.gridLayout.addWidget(self.addButton2, 1, 2, Qt.AlignLeft)
        self.gridLayout.addWidget(self.addButton3, 2, 2, Qt.AlignLeft)
        self.gridLayout.addWidget(self.addButton4, 3, 2, Qt.AlignLeft)
        self.gridLayout.addWidget(self.addButton5, 4, 2, Qt.AlignLeft)

    def addSubgoal1(self):
        self.subgoal1.show()
        self.addButton1.hide()
        self.deleteButton1.show()

    def addSubgoal2(self):
        self.subgoal2.show()
        self.addButton2.hide()
        self.deleteButton2.show()

    def addSubgoal3(self):
        self.subgoal3.show()
        self.addButton3.hide()
        self.deleteButton3.show()

    def addSubgoal4(self):
        self.subgoal4.show()
        self.addButton4.hide()
        self.deleteButton4.show()

    def addSubgoal5(self):
        self.subgoal5.show()
        self.addButton5.hide()
        self.deleteButton5.show()

    def deleteSubgoal1(self):
        self.subgoal1.hide()
        self.deleteButton1.hide()
        self.addButton1.show()

    def deleteSubgoal2(self):
        self.subgoal2.hide()
        self.deleteButton2.hide()
        self.addButton2.show()

    def deleteSubgoal3(self):
        self.subgoal3.hide()
        self.deleteButton3.hide()
        self.addButton3.show()

    def deleteSubgoal4(self):
        self.subgoal4.hide()
        self.deleteButton4.hide()
        self.addButton4.show()

    def deleteSubgoal5(self):
        self.subgoal5.hide()
        self.deleteButton5.hide()
        self.addButton5.show()


# The view of viewing a goal
class ViewGoalWindow(QDialog):
    def __init__(self):
        # ?
        super(ViewGoalWindow, self).__init__()
        # Load the View Goal Window UI
        loadUi(ui[3], self)
        # Update the window's title
        self.setWindowTitle('View Goal');
 
# The main view of the Goal Tracker
class MainViewController(QMainWindow):
    def __init__(self, _model):
        # ?
        super(MainViewController, self).__init__()
        # Load the Main Window UI
        loadUi(ui[0], self)

        self.model = _model


        # Update the window's title
        self.setWindowTitle('Goal Tracker');
        # Set up layout for current goals
        self.setupLayout("current")
        # Set up method for when Add Event button is clicked
        self.addButton.clicked.connect(self.openAddGoalWindow)
        # Set up methods for displaying goals according to their status (overdue, current, completed)
        self.currentGoalsButton.clicked.connect(self.setupCurrentLayout)
        self.overdueGoalsButton.clicked.connect(self.setupOverdueLayout)
        self.completedGoalsButton.clicked.connect(self.setupCompletedLayout)

    # Returns a label with text set
    def createLabel(self, labelText):
        # Create a label
        label = QLabel()
        # Set the text of the label
        label.setText(labelText)
        # Return the label
        return label

    # Returns a button with text and method set
    def createButton(self, buttonText):
        # Create a button
        button = QPushButton()
        # Set the text of the button
        button.setText(buttonText)
        # Set up method for when button is clicked according to button's text
        if buttonText is "View":
            button.clicked.connect(self.openViewGoalWindow)
        elif buttonText is "Edit":
            button.clicked.connect(self.openEditGoalWindow)
        elif buttonText is "Delete":
            button.clicked.connect(self.deleteGoal)
        elif buttonText is "Reschedule":
            button.clicked.connect(self.openRescheduleWindow)
        elif buttonText is "Complete":
            button.clicked.connect(self.completeGoal)
        # Return the button
        return button

    # Sets up the main window's layout according to user's selection of goal status (current, overdue, complete)
    # Adds labels and buttons to grid for every goal
    def setupLayout(self, goalStatus):
        # Modify the goal label to display the appropriate status of the goal
        if goalStatus is "current":
            self.goalLabel.setText("Current Goals:")
        elif goalStatus is "overdue":
            self.goalLabel.setText("Overdue Goals:")
        elif goalStatus is "completed":
            self.goalLabel.setText("Completed Goals:")
        # Modify the font size and style of the goal label
        goalLabelFont = QFont("Arial", 24, QFont.Bold)
        self.goalLabel.setFont(goalLabelFont)

        # Create labels for current goal's name and end date
        goalLabel = self.createLabel("Exercise for 1 hour")
        endDateLabel = self.createLabel("02/28/2019")
        # Modify the font size of the labels
        font = QFont("Arial", 15)
        goalLabel.setFont(font)
        endDateLabel.setFont(font)
        # Add labels to the grid layout
        self.gridLayout.addWidget(goalLabel, 0, 0, Qt.AlignTop)
        self.gridLayout.addWidget(endDateLabel, 0, 1, Qt.AlignTop)

        # Create buttons according to the appropriate status
        # Add buttons to the grid layout as far right as possible
        if goalStatus is "current":
            editButton = self.createButton("Edit")
            self.gridLayout.addWidget(editButton, 0, 2, Qt.AlignTop)
        elif goalStatus is "overdue":
            rescheduleButton = self.createButton("Reschedule")
            self.gridLayout.addWidget(rescheduleButton, 0, 2, Qt.AlignTop)
        viewButton = self.createButton("View")
        self.gridLayout.addWidget(viewButton, 0, 3, Qt.AlignTop)
        deleteButton = self.createButton("Delete")
        self.gridLayout.addWidget(deleteButton, 0, 4, Qt.AlignTop)

        # Modify the span of the columns by stretching the labels twice as much as the buttons
        self.gridLayout.setColumnStretch(0, 2)
        self.gridLayout.setColumnStretch(1, 2)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout.setColumnStretch(3, 1)
        self.gridLayout.setColumnStretch(4, 1)

    # Removes goal information in every row and column in the grid layout
    def removeRowsAndColumns(self):
        # Remove every row from grid layout [0]
        for index in range(self.gridLayout.columnCount()):
            row = self.gridLayout.getItemPosition(index)[0]
            for column in range(self.gridLayout.columnCount()):
                layout = self.gridLayout.itemAtPosition(row, column)
                if layout is not None:
                    layout.widget().deleteLater()
                    self.gridLayout.removeItem(layout)
 
    # Clears the grid layout and sets up a new layout with current goals
    def setupCurrentLayout(self):
        # Clear the grid layout
        self.removeRowsAndColumns()
        # Set up the new layout according to goal's status (current)
        self.setupLayout("current")

    # Clears the grid layout and sets up a new layout with overdue goals
    def setupOverdueLayout(self):
        # Clear the grid layout
        self.removeRowsAndColumns()
        # Set up the new layout according to goal's status (overdue)
        self.setupLayout("overdue")

    # Clears the grid layout and sets up a new layout with completed goals
    def setupCompletedLayout(self):
        # Clear the grid layout
        self.removeRowsAndColumns()
        # Set up the new layout according to goal's status (completed)
        self.setupLayout("completed")

    # Returns a goal's name according to user's input
    def getGoalName(self, window):
        return window.goalName.text()

    # Returns a goal's end date according to user's input
    def getEndDate(self, window):
        return window.endDate.text()

    # Returns a goal's category according to user's selection
    def getCategoryOption(self, window):
        if window.personalRadioButton.isChecked():
            return "Personal"
        elif window.healthRadioButton.isChecked():
            return "Health"
        elif window.financeRadioButton.isChecked():
            return "Finance"
        elif window.workRadioButton.isChecked():
            return "Work"
        elif window.otherRadioButton.isChecked():
            return "Other"

    # Returns a goal's priority according to user's selection
    def getPriorityOption(self, window):
        if window.lowRadioButton.isChecked():
            return "Low"
        elif window.mediumRadioButton.isChecked():
            return "Medium"
        elif window.highRadioButton.isChecked():
            return "High"

    # Return's a goal's subgoals according to user's input
    def getSubgoals(self, window):
        return [window.subgoal1.text(), window.subgoal2.text(), window.subgoal3.text(), window.subgoal4.text(), window.subgoal5.text()]

    # Open a new window and get the user's input for adding a goal
    def openAddGoalWindow(self):
        # Create a window of the Add Goal display
        window = AddGoalWindow()
        # Show the window
        window.exec_()
        # Get the goal's information
        goalName = self.getGoalName(window)
        endDate = self.getEndDate(window)
        category = self.getCategoryOption(window)
        priority = self.getPriorityOption(window)
        subgoals = self.getSubgoals(window)

        self.model.addGoal({"name": goalName, "category": category, "priority": priority}, [])
        mylist = self.model.getGoalList()
        for goal in mylist:
            print(goal.getName())
        # Print the goal's information
        # print(goalName, endDate, category, priority, subgoals[0], subgoals[1], subgoals[2], subgoals[3], subgoals[4])

    # Open a new window and get the user's input for editing a goal
    def openEditGoalWindow(self):
        # Create a window of the Edit Goal display
        window = EditGoalWindow()
        # Show the window
        window.exec_()
        # Get the goal's information
        goalName = self.getGoalName(window)
        endDate = self.getEndDate(window)
        category = self.getCategoryOption(window)
        priority = self.getPriorityOption(window)
        subgoals = self.getSubgoals(window)
        # Print the goal's information
        print(goalName, endDate, category, priority, subgoals[0], subgoals[1], subgoals[2], subgoals[3], subgoals[4])

    # Open a new window and display the goal information
    def openViewGoalWindow(self):
        # Create a window of the View Goal display
        window = ViewGoalWindow()
        # Show the window
        window.exec_()

    def openRescheduleGoalWindow(self):
        # Create a window of the View Goal display
        window = ViewGoalWindow()
        # Show the window
        window.exec_()

    def deleteGoal(self, index):
        # Remove the row with the goal's information [0]
        index = self.gridLayout.indexOf(self.sender())
        row = self.gridLayout.getItemPosition(index)[0]
        for column in range(self.gridLayout.columnCount()):
            layout = self.gridLayout.itemAtPosition(row, column)
            if layout is not None:
                layout.widget().deleteLater()
                self.gridLayout.removeItem(layout)

    def openRescheduleWindow(self):
        print("TODO: Reschedule Goal")

    def completeGoal(self):
        print("TODO: Complete Goal")

    def completeGoal(self):
        print("TODO: Complete Goal")
 
def main():
    filemanager = FileManager() #create FileManager object
    model = filemanager.load("potato.potato") #load File and store
    print(model.currGID)

    # Initialize PyQT application
    app = QApplication(sys.argv)
    # Create a window of the main display of the Goal Tracker
    window = MainViewController(model)
    # Show the window
    window.show()
    # Exit the program
    sys.exit(app.exec_())

    #Contact File Manager to Save File

if __name__ == '__main__':
	main()
