import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from datetime import datetime

UI_PATH = '../UI/EditGoal.ui'

# The view of editing a goal
class EditGoalWindow(QDialog):
    def __init__(self, _goalName = None, _category = None, _priority = None, _subGoals = None, _date = None):
        # ?
        super(EditGoalWindow, self).__init__()
        # Load the Edit Goal Window UI
        loadUi(UI_PATH, self)

        if _goalName == None and _category == None and _priority == None and _subGoals == None:
            self.setWindowTitle('Add Goal') # Update the window's title
            self.endDate.setDate(datetime.today()) # Set the QDateEdit widget to display a predetermined date (today's date)
            self.personalRadioButton.setChecked(True) # Set the RadioButton widget to be checked according to a predetermined category (personal)
            self.lowRadioButton.setChecked(True) # Set the RadioButton widget to be checked according to a predetermined priority (low)
        else:
            self.setWindowTitle('Edit Goal') # Update the window's title
            self.goalName.setText(_goalName)

            if _date == None:
                self.checkBox.setChecked(True)
                self.endDate.setDate(datetime.today()) # Set the QDateEdit widget to display a predetermined date (today's date)
            else:
                self.endDate.setDate(_date)

            if _category == "Personal":
                self.personalRadioButton.setChecked(True)
            elif _category == "Health":
                self.healthRadioButton.setChecked(True)
            elif _category == "Finance":
                self.financeRadioButton.setChecked(True)
            elif _category == "Work":
                self.workRadioButton.setChecked(True)
            else:
                self.otherRadioButton.setChecked(True)

            if _priority == 1:
                self.highRadioButton.setChecked(True)
            elif _priority == 2:
                self.mediumRadioButton.setChecked(True)
            else:
                self.lowRadioButton.setChecked(True)

        #load subgoals


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