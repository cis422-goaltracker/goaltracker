import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from datetime import date

UI_PATH = '../UI/ViewGoal.ui'

# The view of viewing a goal
class ViewGoalWindow(QDialog):
    def __init__(self):
        # ?
        super(ViewGoalWindow, self).__init__()
        # Load the View Goal Window UI
        loadUi(UI_PATH, self)
        # Update the window's title
        self.setWindowTitle('View Goal');