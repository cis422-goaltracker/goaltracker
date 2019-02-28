"""
	Names: Holly Hardin (HH)
	CIS 422
	GoalTracker
        Reference [0]: https://github.com/mfitzp/15-minute-apps/blob/master/minesweeper/minesweeper.py

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

#Import sys (HH)
import sys
#Import widgets (labels, buttons, etc.) (HH)
from PyQt5.QtWidgets import *
#Import module that allows UI to be uploaded (HH)
from PyQt5.uic import loadUi


# Global variable for storing UI files (HH)
ui = ['../UI/GoalTracker.ui']

# The main view of the Goal Tracker
class MainViewController(QMainWindow):
   def __init__(self):
      # ?
      super(MainViewController, self).__init__()
      # Load the UI
      loadUi(ui[0], self)
      # Update the window's title
      self.setWindowTitle('Goal Tracker');
      # Set up layout for overdue goals
      self.setupOverdueLayout()
      # Set up layout for current goals
      self.setupCurrentLayout()
      # Set up layout for completed goals
      self.setupCompletedLayout()

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
      # Return the button
      return button

   def setupOverdueLayout(self):
      # Create labels for the overdue goal's name and end date
      goalLabel = self.getLabel("Exercise for 1 hour")
      endDateLabel = self.getLabel("02/26/2019")

      # Add the labels to the appropriate layout
      self.overdueGoalsLayout.addWidget(goalLabel)
      self.overdueEndDatesLayout.addWidget(endDateLabel)

      # Create buttons for completing and rescheduling these goals
      completeButton = self.getButton("Complete")
      rescheduleButton = self.getButton("Reschedule")

      # Add the buttons to the appropriate layout
      self.completeLayout.addWidget(completeButton)
      self.rescheduleLayout.addWidget(rescheduleButton)

   def setupCurrentLayout(self):
       # Create labels for current goal's name and end date
       goalLabel = self.getLabel("Exercise for 1 hour")
       endDateLabel = self.getLabel("02/28/2019")

       # Add the labels to the appropriate layout
       self.currentGoalsLayout.addWidget(goalLabel)
       self.currentEndDatesLayout.addWidget(endDateLabel)

       # Create buttons for viewing, editing, and deleting goals
       viewButton = self.getButton("View")
       editButton = self.getButton("Edit")
       deleteButton = self.getButton("Delete")

       # Add the buttons to the appropriate layout
       self.viewLayout.addWidget(viewButton)
       self.editLayout.addWidget(editButton)
       self.deleteLayout.addWidget(deleteButton)

   def setupCompletedLayout(self):
       # Create labels for completed goal's name and end date
       goalLabel = self.getLabel("Exercise for 1 hour")
       endDateLabel = self.getLabel("02/27/2019")

       # Add the labels to the appropriate layout
       self.completedGoalsLayout.addWidget(goalLabel)
       self.completedEndDatesLayout.addWidget(endDateLabel)

       # Create a button for viewing goal
       viewButton = self.getButton("View")

       # Add the button to the appropriate layout
       self.viewLayout2.addWidget(viewButton)

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
