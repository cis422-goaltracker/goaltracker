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

from Goal import Goal
from Model import Model
from FileManager import FileManager
from AnalysisGenerator import AnalysisGenerator as AnalysisGenerator

from Dialogs import AddEditViewGoal, AddEditViewSubGoal

# Global variable for storing UI files (HH)
UI_PATHS = {"MainWindow": "../UI/MainWindow.ui", "AddEditViewGoal": "../UI/AddEditViewGoal.py", "AddEditViewSubGoal": "../UI/AddEditViewSubGoal.py"}

class MainWindow(QMainWindow):
    def __init__(self, _model):
        super(MainWindow, self).__init__()
        loadUi(UI_PATHS["MainWindow"], self) # Load the Main Window UI

        #Class Variables
        self.model = _model
        
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

    @pyqtSlot()
    def loadCurrentGoals(self):
        '''
        @param:

        @return:

        @purpose:
        '''
        self.label_Goals.setText("Current Goals")

    @pyqtSlot()
    def loadOverdueGoals(self):
        '''
        @param:

        @return:

        @purpose:
        '''
        self.label_Goals.setText("Overdue Goals")

    @pyqtSlot()
    def loadCompletedGoals(self):
        '''
        @param:

        @return:

        @purpose:
        '''
        self.label_Goals.setText("Completed Goals")

    @pyqtSlot()
    def loadAllGoals(self):
        '''
        @param:

        @return:

        @purpose:
        '''
        self.label_Goals.setText("All Goals")

    @pyqtSlot()
    def loadCategorySort(self):
        '''
        @param:

        @return:

        @purpose:
        '''
        pass

    @pyqtSlot()
    def loadPrioritySort(self):
        '''
        @param:

        @return:

        @purpose:
        '''
        pass

    @pyqtSlot()
    def loadAddGoal(self):
        '''
        @param:

        @return:

        @purpose:
        '''
        pass

    @pyqtSlot()
    def loadCompleteGoal(self):
        '''
        @param:

        @return:

        @purpose:
        '''
        pass

    @pyqtSlot()
    def loadEditViewGoal(self):
        '''
        @param:

        @return:

        @purpose:
        '''
        pass

    @pyqtSlot()
    def loadDeleteGoal(self):
        '''
        @param:

        @return:

        @purpose:
        '''
        pass

    @pyqtSlot()
    def loadViewAnalysis(self):
        '''
        @param:

        @return:

        @purpose:
        '''
        pass
    
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
