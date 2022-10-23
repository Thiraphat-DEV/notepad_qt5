# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\notepadClonebyBoat.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from base64 import encode
from importlib.resources import path
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog

from formatter import NullWriter

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1107, 626)
        MainWindow.setMaximumSize(QtCore.QSize(1107, 626))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.showText = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.showText.setGeometry(QtCore.QRect(0, 0, 1111, 521))
        self.showText.setMaximumSize(QtCore.QSize(1111, 521))
        self.showText.setObjectName("showText")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(480, 520, 171, 16))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1107, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setCheckable(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\../../../Downloads/opne.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setCheckable(True)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(".\\../../../Downloads/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon1)
        self.actionSave.setObjectName("actionSave")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(".\\../../../Downloads/copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCopy.setIcon(icon2)
        self.actionCopy.setObjectName("actionCopy")
        self.actionUndo = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(".\\../../../Downloads/undo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUndo.setIcon(icon3)
        self.actionUndo.setObjectName("actionUndo")
        self.actionCut = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(".\\../../../Downloads/cut.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCut.setIcon(icon4)
        self.actionCut.setObjectName("actionCut")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(".\\../../../Downloads/paste.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPaste.setIcon(icon5)
        self.actionPaste.setObjectName("actionPaste")
        self.actionRedo = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(".\\../../../Downloads/redo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRedo.setIcon(icon6)
        self.actionRedo.setObjectName("actionRedo")
        self.actionSelectAll = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(".\\../../../Downloads/selectAll.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSelectAll.setIcon(icon7)
        self.actionSelectAll.setObjectName("actionSelectAll")
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addAction(self.actionCopy)
        self.toolBar.addAction(self.actionPaste)
        self.toolBar.addAction(self.actionCut)
        self.toolBar.addAction(self.actionUndo)
        self.toolBar.addAction(self.actionRedo)
        self.toolBar.addAction(self.actionSelectAll)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "THIRAPHAT-DEV !! BOATY !!"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setToolTip(_translate("MainWindow", "OpenFile"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setToolTip(_translate("MainWindow", "SaveFile"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionCopy.setToolTip(_translate("MainWindow", "CopyText"))
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C, Ctrl+X"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionUndo.setToolTip(_translate("MainWindow", "UndoText"))
        self.actionUndo.setShortcut(_translate("MainWindow", "Ctrl+Z, Ctrl+U"))
        self.actionCut.setText(_translate("MainWindow", "Cut"))
        self.actionCut.setToolTip(_translate("MainWindow", "CutText"))
        self.actionCut.setShortcut(_translate("MainWindow", "Ctrl+X"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionPaste.setToolTip(_translate("MainWindow", "PasteText"))
        self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.actionRedo.setText(_translate("MainWindow", "Redo"))
        self.actionRedo.setToolTip(_translate("MainWindow", "RedoText"))
        self.actionRedo.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.actionSelectAll.setText(_translate("MainWindow", "SelectAll"))
        self.actionSelectAll.setShortcut(_translate("MainWindow", "Ctrl+A"))
        #cut Text
        self.actionCut.triggered.connect(self.showText.cut)
        #copy Text
        self.actionCopy.triggered.connect(self.showText.copy)
        #undo
        self.actionUndo.triggered.connect(self.showText.undo)
        #redo
        self.actionRedo.triggered.connect(self.showText.redo)
        #selectAllText
        self.actionSelectAll.triggered.connect(self.showText.selectAll)
        #paste Text
        self.actionPaste.triggered.connect(self.showText.paste)

        #save
        self.actionSave.triggered.connect(self.save)

        #open
        self.actionOpen.triggered.connect(self.openFile)
    def save(self):
        # print('Hello Save')
        #save file to local folder
        pathFile = QFileDialog.getSaveFileName()
        # print(pathFile)
        # set text to save
        text = self.showText.toPlainText()

        try:
            #open local folder as write
            with open(pathFile[0], 'w', encoding='utf-8') as f:
                #write from showText to file
                f.write(text)
                #check error Exception
        except Exception as e:
            print(e)

    def openFile(self):
        # print("open FIle")
        #open file in local
        pathFile = QFileDialog.getOpenFileName()

        if pathFile:
            try:
                #read file
                with(open(pathFile[0], 'r', encoding='utf-8')) as f:
                    # set text to text_of_file variable
                    text_of_file = f.read()
                    #show text
                    self.showText.setPlainText(text_of_file)
                    #except file of null
            except Exception as e:
                print(e)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
