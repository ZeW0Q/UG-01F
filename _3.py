from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *


class Ui_MainWindow(object):
  def setupUi(self, MainWindow):
    MainWindow.setObjectName("MainWindow")
    MainWindow.resize(649, 168)
    MainWindow.setMinimumSize(QtCore.QSize(0, 0))
    MainWindow.setMaximumSize(QtCore.QSize(999999, 999999))
    MainWindow.setStyleSheet("MainWindow\n""{\n""    background-color: rgb(37, 37, 37);\n""}")
    self.centralwidget = QtWidgets.QWidget(MainWindow)
    self.centralwidget.setMaximumSize(QtCore.QSize(99999, 999999))
    self.centralwidget.setStyleSheet("background-color: rgb(37, 37, 37)\n""")
    self.centralwidget.setObjectName("centralwidget")

    self.frame = QtWidgets.QFrame(self.centralwidget)
    self.frame.setGeometry(QtCore.QRect(0, -1, 641, 171))
    self.frame.setMinimumSize(QtCore.QSize(0, 0))
    self.frame.setMaximumSize(QtCore.QSize(99999, 999))
    self.frame.setStyleSheet("MainWindow\n""{\n""    background-color:rgb(46, 46, 46)\n""}")
    self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
    self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
    self.frame.setObjectName("frame")
    self.tabWidget = QtWidgets.QTabWidget(self.frame)
    self.tabWidget.setGeometry(QtCore.QRect(0, 0, 651, 161))
    self.tabWidget.setMinimumSize(QtCore.QSize(4, 0))
    font = QtGui.QFont()
    font.setFamily("Rio Glamour personal use")
    font.setPointSize(14)
    self.tabWidget.setFont(font)
    self.tabWidget.setStyleSheet(
    "QTabWidget::pane\n""{\n""    border: 1px;\n""    background: rgb(37, 37, 37);\n""}\n""\n""QTabBar::tab\n""{\n""    background: rgb(37, 37, 37);\n""    color:rgb(255, 255, 255);\n""}\n""\n""\n""QTabBar::tab:selected\n""{\n""    background:rgb(26, 26, 26);\n""    color:rgb(255, 255, 255);\n""}\n""\n""QTabBar::tab:hover\n""{\n""    background:rgb(57, 57, 57);\n""    color:rgb(255, 255, 255);\n""}\n""\n""")
    self.tabWidget.setObjectName("tabWidget")
    self.tab = QtWidgets.QWidget()
    font = QtGui.QFont()
    font.setPointSize(8)
    self.tab.setFont(font)
    self.tab.setObjectName("tab")
    self.label = QtWidgets.QLabel(self.tab)
    self.label.setGeometry(QtCore.QRect(-4, -8, 651, 141))
    self.label.setText("")
    self.label.setObjectName("label")
    self.tabWidget.addTab(self.tab, "")

    self.tab_2 = QtWidgets.QWidget()
    self.tab_2.setObjectName("tab_2")

    self.label_2 = QtWidgets.QLabel(self.tab_2)
    self.label_2.setGeometry(QtCore.QRect(0, 0, 661, 141))
    self.label_2.setText("")
    self.label_2.setObjectName("label_2")


    self.layout = QGridLayout(self.tab_2)  # !!! +++
    self.layout.addWidget(self.label_2, 0, 0, 1, 2)  # !!! +++


    self.tabWidget.addTab(self.tab_2, "")
    self.tab_3 = QtWidgets.QWidget()
    self.tab_3.setStyleSheet("background-color: rgb(37, 37, 37);\n""color: rgb(255, 255, 255);")
    self.tab_3.setObjectName("tab_3")
    self.label_3 = QtWidgets.QLabel(self.tab_3)
    self.label_3.setGeometry(QtCore.QRect(10, 0, 661, 141))
    self.label_3.setText("")
    self.label_3.setObjectName("label_3")
    self.tabWidget.addTab(self.tab_3, "")
    MainWindow.setCentralWidget(self.centralwidget)

    self.retranslateUi(MainWindow)
    self.tabWidget.setCurrentIndex(2)
    QtCore.QMetaObject.connectSlotsByName(MainWindow)

def retranslateUi(self, MainWindow):
    _translate = QtCore.QCoreApplication.translate
    MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
    self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Time"))
    self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Stopwatch"))
    self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Timer"))


class ManinWindow(QtWidgets.QMainWindow, Ui_MainWindow):
  def __init__(self):
    super().__init__()
    self.setupUi(self)

    self.tabWidget.currentChanged.connect(self.current_index)
    self.tabWidget.setCurrentIndex(0)


    self.working_clock = QtCore.QTimer()
    self.working_clock.setInterval(1000)
    self.working_clock.timeout.connect(self.display_clock)
    self.working_clock.start()


def add_functions(self):
    # ×àñû
    self.label.setText(QDateTime.currentDateTime().toString('HH:mm:ss\ndd MM yyyy'))
    self.label.setFont(QtGui.QFont("Capsuula", 40))
    self.label.setStyleSheet("color: #DADDFC;")
    self.label.setAlignment(Qt.AlignHCenter)

    self.temp = 0
    self.label_2.setText("00:00:00")
    self.label_2.setAlignment(Qt.AlignHCenter)
    self.label_2.setFont(QtGui.QFont("Capsuula", 40))
    self.label_2.setStyleSheet("color: #fff;")

    self.btn_start = QtWidgets.QPushButton("Start")
    self.btn_start.setStyleSheet("color: #fff; font-size: 15px; background-color: #555;")
    self.btn_start.clicked.connect(self.func_start)

    self.btn_continue = QtWidgets.QPushButton("Continue")
    self.btn_continue.setStyleSheet("color: #fff; font-size: 15px; background-color: #555;")
    self.btn_continue.clicked.connect(self.func_continue)

    self.btn_reset = QtWidgets.QPushButton("Reset")
    self.btn_reset.setStyleSheet("color: #fff; font-size: 15px; background-color: #555;")
    self.btn_reset.clicked.connect(self.func_reset)
    self.layout.addWidget(self.btn_start, 1, 0, 1, 2)
    self.layout.addWidget(self.btn_continue, 2, 0, 1, 1)
    self.layout.addWidget(self.btn_reset, 2, 1, 1, 1)

    self.btn_continue.hide()
    self.btn_reset.hide()

    self.timer = QtCore.QTimer()
    self.timer.setInterval(1000)
    self.timer.timeout.connect(self.display_time)

def func_start(self):
    if self.btn_start.text() == "Start":
        self.timer.start()
        self.btn_start.setText("Stop")
    else:
        self.timer.stop()
        self.btn_start.setText("Start")
        self.btn_start.hide()
        self.btn_continue.show()
        self.btn_reset.show()

def func_reset(self):
    self.temp = 0
    self.label_2.setText("00:00:00")
    self.btn_start.setText("Start")
    self.btn_start.show()
    self.btn_continue.hide()
    self.btn_reset.hide()

def display_time(self):
    f_temp = datetime.utcfromtimestamp(self.temp).strftime("%H:%M:%S")
    self.label_2.setText(f_temp)
    self.temp += 1

def current_index(self, index):
    if index == 0:
        self.add_functions()

def func_continue(self):
    self.timer.start()
    self.btn_start.setText('Ñòîï')
    self.btn_start.show()
    self.btn_continue.hide()
    self.btn_reset.hide()
    

def display_clock(self):        
    self.label.setText(QDateTime.currentDateTime().toString('HH:mm:ss\ndd MM yyyy'))        
from datetime import datetime, timedelta                                 # +++
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(649, 168)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(999999, 999999))
        MainWindow.setStyleSheet(
            "MainWindow\n""{\n""    background-color: rgb(37, 37, 37);\n""}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(99999, 999999))
        self.centralwidget.setStyleSheet("background-color: rgb(37, 37, 37)\n""")
        self.centralwidget.setObjectName("centralwidget")

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, -1, 641, 171))
        self.frame.setMinimumSize(QtCore.QSize(0, 0))
        self.frame.setMaximumSize(QtCore.QSize(99999, 999))
        self.frame.setStyleSheet(
            "MainWindow\n""{\n""    background-color:rgb(46, 46, 46)\n""}")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.tabWidget = QtWidgets.QTabWidget(self.frame)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 651, 161))
        self.tabWidget.setMinimumSize(QtCore.QSize(4, 0))
        font = QtGui.QFont()
        font.setFamily("Rio Glamour personal use")
        font.setPointSize(14)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet(
        "QTabWidget::pane\n"
        "{\n""    border: 1px;\n"
        "    background: rgb(37, 37, 37);\n"
        "}\n""\n"
        "QTabBar::tab\n""{\n""    background: rgb(37, 37, 37);\n"
        "    color:rgb(255, 255, 255);\n""}\n""\n""\n"
        "QTabBar::tab:selected\n""{\n"
        "    background:rgb(26, 26, 26);\n"
        "    color:rgb(255, 255, 255);\n""}\n""\n"
        "QTabBar::tab:hover\n""{\n""    background:rgb(57, 57, 57);\n"
        "    color:rgb(255, 255, 255);\n""}\n""\n""")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setPointSize(8)
        self.tab.setFont(font)
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(-4, -8, 651, 141))
        self.label.setText("")
        self.label.setObjectName("label")
        self.tabWidget.addTab(self.tab, "")

        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")

        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 661, 141))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")

        self.layout = QGridLayout(self.tab_2)  
        self.layout.addWidget(self.label_2, 0, 0, 1, 5)  

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setStyleSheet(
            "background-color: rgb(37, 37, 37);\n""color: rgb(255, 255, 255);")
        self.tab_3.setObjectName("tab_3")
        self.label_3 = QtWidgets.QLabel(self.tab_3)
        self.label_3.setGeometry(QtCore.QRect(10, 0, 661, 141))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Time"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Stopwatch"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Timer"))


class ManinWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.tabWidget.currentChanged.connect(self.current_index)
        self.tabWidget.setCurrentIndex(0)

        self.working_clock = QtCore.QTimer()
        self.working_clock.setInterval(1000)
        self.working_clock.timeout.connect(self.display_clock)
        self.working_clock.start()
        
    def add_functions(self):
        self.label.setText(QDateTime.currentDateTime().toString('HH:mm:ss\ndd MM yyyy'))
        self.label.setFont(QtGui.QFont("Capsuula", 40))
        self.label.setStyleSheet("color: #DADDFC;")
        self.label.setAlignment(Qt.AlignHCenter)

#        self.temp = 0
        
        self.label_2.setText("00:00:00")
        self.label_2.setAlignment(Qt.AlignHCenter)
        self.label_2.setFont(QtGui.QFont("Capsuula", 25))
        self.label_2.setStyleSheet("color: #fff;")

        self.btn_start = QtWidgets.QPushButton("Start")
        self.btn_start.setStyleSheet("color: #fff; font-size: 15px; background-color: #555;")
        self.btn_start.clicked.connect(self.func_start)

        self.btn_continue = QtWidgets.QPushButton("Continue")
        self.btn_continue.setStyleSheet("color: #fff; font-size: 15px; background-color: #555;")
        self.btn_continue.clicked.connect(self.func_continue)

        self.btn_reset = QtWidgets.QPushButton("Reset")
        self.btn_reset.setStyleSheet("color: #fff; font-size: 15px; background-color: #555;")
        self.btn_reset.clicked.connect(self.func_reset)
        
# +++ vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv        
        self.startDateTime = QDateTimeEdit()
        today = QDate.currentDate()
        DATETIME_FORMAT = "yyyy-MM-dd hh:mm:ss"
        self.startDateTime.setDateRange(today, today)
        self.startDateTime.setDisplayFormat(DATETIME_FORMAT)
        self.startDateTime.setStyleSheet('background-color: #ccc; font-size: 12px;')

        self.endDateTime = QDateTimeEdit() 
        self.endDateTime.setDateTime(QDateTime.currentDateTime())
        self.endDateTime.setDisplayFormat(DATETIME_FORMAT)
        self.endDateTime.setStyleSheet('background-color: #ccc; font-size: 12px;')

        startLabel = QLabel('Start', styleSheet ='color: #fff; font-size: 12px;')
        startLabel.setFixedSize(30, 25)
        self.layout.addWidget(startLabel, 1, 0, 1, 1, alignment=Qt.AlignRight)
        self.layout.addWidget(self.startDateTime, 1, 1, 1, 1)
        endLabel = QLabel("End:", styleSheet ='color: #fff; font-size: 12px;')
        endLabel.setFixedSize(30, 25)
        self.layout.addWidget(endLabel, 1, 2, 1, 1, alignment=Qt.AlignRight)        
        self.layout.addWidget(self.endDateTime, 1, 3, 1, 1)
        self.layout.addWidget(self.btn_start, 1, 4, 1, 1)
        
        self.layout.addWidget(self.btn_continue, 2, 1, 1, 1)
        self.layout.addWidget(self.btn_reset, 2, 3, 1, 1)

        self.btn_continue.hide()
        self.btn_reset.hide()

        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.display_time)

    def func_start(self):
        if self.btn_start.text() == "Start":
            self.timer.start()
            self.btn_start.setText("Stop")
            
            start_date = self.startDateTime.dateTime()
            self.start_date_py = start_date.toPyDateTime()
            end_date = self.endDateTime.dateTime()
            self.end_date_py = end_date.toPyDateTime()
            
            self.d = self.end_date_py - self.start_date_py                  # !!!
        else:
            self.timer.stop()
            self.btn_start.setText("Start")
            self.btn_start.hide()
            self.btn_continue.show()
            self.btn_reset.show()

    def func_reset(self):
        self.label_2.setText("00:00:00")
        self.btn_start.setText("Start")
        self.btn_start.show()
        self.btn_continue.hide()
        self.btn_reset.hide()
        
    def display_time(self):
        mm, ss = divmod(self.d.seconds, 60)                                 # !!!
        hh, mm = divmod(mm, 60)                                             # !!!
        
        self.label_2.setText(
            f'{self.d.days} äí. {hh:02} ÷àñ. {mm:02} ìèí. {ss:02} ñåê.'
        )     

        self.d = self.d - timedelta(seconds=1)                              # !!!
        
        if self.d.days < 0:                                                 # !!!
            self.timer.stop()

    def current_index(self, index):
        if index == 0:
            self.add_functions()

    def func_continue(self):
        if self.d.days < 0:
            return
    
        self.timer.start()
        self.btn_start.setText('Ñòîï')
        self.btn_start.show()
        self.btn_continue.hide()
        self.btn_reset.hide()

    def display_clock(self):        
        self.label.setText(QDateTime.currentDateTime().toString('HH:mm:ss\ndd MM yyyy'))        


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = ManinWindow()
    w.show()
    sys.exit(app.exec_())
