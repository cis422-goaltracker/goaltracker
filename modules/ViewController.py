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
UI_PATHS = {"MainWindow": "../UI/MainWindow.ui", "AddEditViewGoal": "../UI/AddEditViewGoal.ui", "AddEditViewSubGoal": "../UI/AddEditViewSubGoal.py"}

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

        # Update the window's title
        self.setWindowTitle('Goal Tracker');

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
        addDialog = EditGoalWindow(self.model)
        if addDialog.exec():
            return(True)
        return False

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

class EditGoalWindow(QDialog):
    def __init__(self, model):

        super(EditGoalWindow, self).__init__()
        # Load the Edit Goal Window UI
        loadUi(UI_PATHS["AddEditViewGoal"], self)

        self.push_save.clicked.connect(self.save_goal)
        
        self.setWindowTitle('Add/Edit Goal') # Update the window's title
        #self.endDate.setDate(datetime.today()) # Set the QDateEdit widget to display a predetermined date (today's date)
        self.radio_priority_low.setChecked(True) # Set the RadioButton widget to be checked according to a predetermined priority (low)

        self.model = model
    @pyqtSlot()
    def save_goal(self):

        goalName = self.lineEdit_goal_name.text()
        endDate = self.dateTimeEdit_due_date.date()
        category = self.lineEdit_category.text()
        priority = self.buttonGroup.checkedButton().text()
        memo = self.textEdit.toPlainText()

        self.model.addGoal({"name": goalName, "category": category, "priority": priority, "memo": memo}, [])
        
        mylist = self.model.getGoalList()
        for goal in mylist:
            print(goal.getName(), goal.getCategory(), goal.getPriority(), goal.getMemo())

        self.accept()
        return 
    
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
