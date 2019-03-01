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
from PyQt5.QtCore import QDate, Qt
from PyQt5.QtGui import *

# Global variable for storing UI files (HH)
ui = ['../UI/GoalTracker.ui', '../UI/AddGoal.ui', '../UI/EditGoal.ui', '../UI/ViewGoal.ui']

# The view of adding a goal
class AddGoalWindow(QDialog):
   def __init__(self):
      super(AddGoalWindow, self).__init__()
      loadUi(ui[1], self)
      self.endDate.setDate(QDate.currentDate())

# The view of editing a goal
class EditGoalWindow(QDialog):
   def __init__(self):
      super(EditGoalWindow, self).__init__()
      loadUi(ui[2], self)

# The view of viewing a goal
class ViewGoalWindow(QDialog):
   def __init__(self):
      super(ViewGoalWindow, self).__init__()
      loadUi(ui[3], self)

# The main view of the Goal Tracker
class MainViewController(QMainWindow):
   def __init__(self):
      # ?
      super(MainViewController, self).__init__()
      # Load the UI
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

   def getLabel(self, labelText):
      # Create a label
      label = QLabel()
      # Set the text of the label
      label.setText(labelText)
      # Return the label
      return label

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
          completeButton = self.getButton("Complete")
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

   def setupCurrentLayout(self):
       index = 0
       row = self.gridLayout.getItemPosition(index)[0]
       for column in range(self.gridLayout.columnCount()):
          layout = self.gridLayout.itemAtPosition(row, column)
          if layout is not None:
             layout.widget().deleteLater()
             self.gridLayout.removeItem(layout)
       self.setupLayout("current")

   def setupOverdueLayout(self):
       index = 0
       row = self.gridLayout.getItemPosition(index)[0]
       for column in range(self.gridLayout.columnCount()):
          layout = self.gridLayout.itemAtPosition(row, column)
          if layout is not None:
             layout.widget().deleteLater()
             self.gridLayout.removeItem(layout)
       self.setupLayout("overdue")

   def setupCompletedLayout(self):
       index = 0
       row = self.gridLayout.getItemPosition(index)[0]
       for column in range(self.gridLayout.columnCount()):
          layout = self.gridLayout.itemAtPosition(row, column)
          if layout is not None:
             layout.widget().deleteLater()
             self.gridLayout.removeItem(layout)
       self.setupLayout("completed")

   def openAddGoalWindow(self):
       window = AddGoalWindow()
       window.exec_()
       goalName = self.getGoalName(window)
       endDate = self.getEndDate(window)
       category = self.getCategoryOption(window)
       priority = self.getPriorityOption(window)
       subgoals = self.getSubgoals(window)
       print(goalName, endDate, category, priority, subgoals[0], subgoals[1], subgoals[2])

   def getGoalName(self, window):
       return window.goalName.text()

   def getEndDate(self, window):
       return window.endDate.text()

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

   def getPriorityOption(self, window):
       if window.lowRadioButton.isChecked():
          return "Low"
       elif window.mediumRadioButton.isChecked():
          return "Medium"
       elif window.highRadioButton.isChecked():
          return "High"

   def getSubgoals(self, window):
       return [window.subgoal1.text(), window.subgoal2.text(), window.subgoal3.text()]

   def openEditGoalWindow(self):
       window = EditGoalWindow()
       return window.exec_()

   def openViewGoalWindow(self):
       window = ViewGoalWindow()
       return window.exec_()

   def openRescheduleGoalWindow(self):
       window = RescheduleWindow()
       return window.exec_()

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
