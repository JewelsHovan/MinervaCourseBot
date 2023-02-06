from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QHBoxLayout
from PyQt6.QtGui import QPalette, QColor, QFont, QIcon

class CrnWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setWindowTitle("CRNs Input Window")
        self.setGeometry(500, 500, 400, 100)

    def initUI(self):
        # create CRN layout
        crn_layout = QVBoxLayout()
        input_layout = QHBoxLayout()
        # create CRN label
        self.crn_label = QLabel("CRNs")
        self.crn_label.setAutoFillBackground(True)
        self.crn_label.setStyleSheet("background-color: CadetBlue;")
        self.crn_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # create CRN inputs
        self.crn_inputs = []
        for i in range(6):
            crn_input = QLineEdit()
            self.crn_inputs.append(crn_input)
            input_layout.addWidget(crn_input)
        # create submit button
        self.submit_button = QPushButton("Save and Submit CRNs")
        self.submit_button.setStyleSheet("background-color: CadetBlue;")
        self.submit_button.clicked.connect(self.save_crn_clicked)

        # setting layout
        crn_layout.addWidget(self.crn_label)
        crn_layout.addLayout(input_layout)
        crn_layout.addWidget(self.submit_button)
        self.setLayout(crn_layout)

        #setting colors
        self.setWindowPalette()
    
    def setWindowPalette(self):
        palette = QPalette()
        black_color = QColor(73, 13, 13)
        palette.setColor(QPalette.ColorRole.Window, black_color)
        self.setPalette(palette)

    def save_crn_clicked(self):
        crn_list = []
        for i in range(6):
            crn_list.append(self.crn_inputs[i].text())
        with open("crns.txt", "w") as f:
            for crn in crn_list:
                f.write(crn + "\n")
        self.close()
