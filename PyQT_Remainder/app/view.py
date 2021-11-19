from PyQt5.QtWidgets import QMainWindow, QPushButton,QHBoxLayout, QScrollArea, QFormLayout, QWidget, QLabel, QLineEdit,QCheckBox, QGridLayout, QVBoxLayout
from PyQt5.QtCore import Qt

class ReminderView(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('My Reminder')
        self.setFixedSize(400, 400)

        self._central_widget = QWidget(self)
        self.setCentralWidget(self._central_widget)

        self.main_layout = QVBoxLayout()
        self._central_widget.setLayout(self.main_layout)

        self._createline()
        self._create_buttons()
        self.my_dict ={}

    def _createline(self):
        self.titlel = QFormLayout()
        """окно для ввода заданий"""
        self.task_ = QLineEdit()
        self.task_.setFixedHeight(30)
        self.titlel.addRow("Task",self.task_)
        self.main_layout.addLayout(self.titlel)

        """окно с перечнем заданий"""
        # self.temp_ = QWidget()
        # self.temp_.setLayout(self.main_layout)

        self.task_area = QVBoxLayout()
        self.main_layout.addLayout(self.task_area)
        # self.temp_area = QWidget


        # self.main_layout.addWidget(self.task_list)
        # self.main_layout.addWidget(self.task_listEdit)

    def _create_buttons(self):
        self.buttons_l = QHBoxLayout()
        self.button1 = QPushButton('Add +', self)
        # self.button1.blockSignals(True)
        # self.button1.setDisabled(True)
        # self.button1.setFixedSize(200, 100)
        # self.button1.setStyleSheet('font-size: 25pt; color: green;')

        self.button2 = QPushButton('Remove -', self)
        # self.button2.setFixedSize(200, 100)
        # self.button2.setStyleSheet('font-size: 25pt; color: red;')


        self.button4 = QPushButton('No task for today')


        self.buttons_l.addWidget(self.button1)
        self.buttons_l.addWidget(self.button2)
        self.buttons_l.addWidget(self.button4)

        self.main_layout.addLayout(self.buttons_l)
    #
    def new_editline(self):

        self.check_box = QCheckBox()
        self.check_box.setText(self.task_.text())
        self.check_box2 = self.check_box
        self.task_area.addWidget(self.check_box)
        self.my_dict.update({(i for i in range(len(self.my_dict))): self.check_box2})






