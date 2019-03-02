"""
	Names: Holly Hardin (HH)
	CIS 422
	GoalTracker
        Reference [0]: https://stackoverflow.com/questions/21213853/pyside-how-to-delete-widgets-from-gridlayout

"""

from Goal import Goal as Goal
from SubGoal import SubGoal as SubGoal
from Status import Status as Status

from GoalManager import GoalManager as GoalManager
from SubGoalManager import SubGoalManager as SubGoalManager
from FileManager import FileManager as FileManager
from EffortTracker import EffortTracker as EffortTracker
from ActiveTimer import ActiveTimer as ActiveTimer
from SortManager import SortManager as SortManager
from ProgressTracker import ProgressTracker as ProgressTracker
from AnalysisViewer import AnalysisViewer as AnalysisViewer

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
      # Variable for keeping track of the number of subgoals that the user wants to add
      self.numSubgoals = 0
      # Variable for keeping track of the maximum number of subgoals a user can have
      self.maxSubgoals = 5
      # Hide all of the subgoals
      self.subgoal1.hide()
      self.subgoal2.hide()
      self.subgoal3.hide()
      self.subgoal4.hide()
      self.subgoal5.hide()
      # Create a button for adding subgoals
      self.addButton = QPushButton()
      # Set the text of the button
      self.addButton.setText("Add")
      # Set up method for when button is clicked
      self.addButton.clicked.connect(self.addSubgoal)
      # Add button to the grid layout
      self.gridLayout.addWidget(self.addButton, 0, 1, Qt.AlignLeft)

   def addSubgoal(self):
      # If the user tries to add more than the maximum number of subgoals allowed, then return
      if self.numSubgoals == self.maxSubgoals:
         return
      # Increase the number of subgoals that the user is adding
      self.numSubgoals += 1
      # Add the button to the grid layout (one row below the LineEdit box)
      self.gridLayout.addWidget(self.addButton, self.numSubgoals + 1, 1)
      # Show the LineEdit box according to the number of subgoals that the user has
      # If the user has the maximum number of subgoals displaying, then remove the add button
      if self.numSubgoals == 1:
         self.subgoal1.show()
      elif self.numSubgoals == 2:
         self.subgoal2.show()
      elif self.numSubgoals == 3:
         self.subgoal3.show()
      elif self.numSubgoals == 4:
         self.subgoal4.show()
      elif self.numSubgoals == 5:
         self.subgoal5.show()
         self.addButton.hide()

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
   def __init__(self):
      # ?
      super(MainViewController, self).__init__()
      # Load the Main Window UI
      loadUi(ui[0], self)
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
   def getLabel(self, labelText):
      # Create a label
      label = QLabel()
      # Set the text of the label
      label.setText(labelText)
      # Return the label
      return label

   # Returns a button with text and method set
   def getButton(self, buttonText):
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
       goalLabel = self.getLabel("Exercise for 1 hour")
       endDateLabel = self.getLabel("02/28/2019")
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
          viewButton = self.getButton("View")
          editButton = self.getButton("Edit")
          deleteButton = self.getButton("Delete")
          self.gridLayout.addWidget(viewButton, 0, 2, Qt.AlignTop)
          self.gridLayout.addWidget(editButton, 0, 3, Qt.AlignTop)
          self.gridLayout.addWidget(deleteButton, 0, 4, Qt.AlignTop)
       elif goalStatus is "overdue":
          completeButton = self.getButton("View")
          rescheduleButton = self.getButton("Reschedule")
          self.gridLayout.addWidget(completeButton, 0, 3, Qt.AlignTop)
          self.gridLayout.addWidget(rescheduleButton, 0, 4, Qt.AlignTop)
       elif goalStatus is "completed":
          viewButton = self.getButton("View")
          self.gridLayout.addWidget(viewButton, 0, 4, Qt.AlignTop)

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
       # Print the goal's information
       print(goalName, endDate, category, priority, subgoals[0], subgoals[1], subgoals[2], subgoals[3], subgoals[4])

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
	#Contact File Manager to Load File


        # Initialize PyQT application
        app = QApplication(sys.argv)
        # Create a window of the main display of the Goal Tracker
        window = MainViewController()
        # Show the window
        window.show()
        # Exit the program
        sys.exit(app.exec_())

	#Contact File Manager to Save File



if __name__ == '__main__':
	main()
